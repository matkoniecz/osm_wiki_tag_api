import pywikibot
import extract_data_item
import extract_infobox_data
import taginfo
import re
import links
import time
import missing_wiki_pages
import random
import mwparserfromhell
import pprint

# https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Install_Pywikibot
# I followed it, run script, and recopied it here
# https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script

# TODO: detect incomplete skeleton (distinguish missing parameter and no parameter set)

def is_adding_image_important(tag_docs):
    page_name = tag_docs.base_title()
    if page_name in ["Key:public_transport:version", "Key:import_uuid"]:
        # no idea what would fit as an image
        return False
    if tag_docs.is_dying_tag():
        return False
    if tag_docs.is_import_tag():
        return False
    banned_parts = []
    banned_parts += ["species:", "note:", "ref:", "tiger:"]
    banned_parts += ["source", "identifier", "import", "is_in", "_ref", "description", "operator", "Key:ISO3166"]
    banned_parts += ["naptan:", "Tag:landmark=", "seamark", "code", "_id"] # TODO - for potential enabling
    banned_parts += ["Key:nvdb:"] # looks like an import, TODO verification after everything else
    banned_parts += ["Key:no"] # noaddress, noref etc - probably plenty of false positives...
    banned_parts += ["IBGE:"] # chance for images, but Brazille specific
    banned_parts += ["Key:fvst:"] # not bothering for now - https://wiki.openstreetmap.org/wiki/Key:fvst:navnelbnr
    banned_parts += ["Key:old_"] # by definition unsigned...

    for ban in banned_parts:
        if ban.replace('_', ' ') in page_name.replace('_', ' '):
            return False
    if is_page_skipped_for_now_from_missing_parameters(tag_docs):
        return False
    return True

def is_page_skipped_for_now_from_missing_parameters(tag_docs):
    page_name = tag_docs.base_title()
    page_name = page_name.replace(" ", "_")
    if "Tag:seamark" in page_name or "Key:seamark" in page_name or "Tag:pilotage" in page_name or "Tag:landmark" in page_name or "Tag:type=" in page_name: # skip seamark mess, at least for now
        return True
    if ":route_ref" in page_name: # TODO skip for now
        return True
    if ":gnis:" in page_name: # TODO skip for now
        return True
    if ":ref:" in page_name: # TODO skip for now
        return True
    if ":yh:" in page_name: # TODO skip for now
        return True
    if "source:" in page_name: # TODO skip for now
        return True
    if page_name in ["Tag:seamark:conspicuity=conspicuous", "Tag:waterway=deep+well"]:
        return True
    if tag_docs.is_dying_tag():
        return True
    return False

def is_page_skipped_for_now_from_missing_description(tag_docs):
    root_page_name = tag_docs.base_title()
    if "Tag:crop=" or "Tag:wood=" or "Tag:mooring=" in root_page_name: # give up with this groups
        return True
    if "Tag:name=": # pages from failed NSI attempt done as wiki pages without editor integration
        return True
    if tag_docs.is_dying_tag():
        return True # TODO - maybe consider as low importance?

def is_key_reportable_as_completely_missing_in_template(key, tag_docs, language):
    root_page_name = tag_docs.base_title()
    if is_page_skipped_for_now_from_missing_parameters(tag_docs):
        return False
    if "Tag:source=" in root_page_name:
        if key == "image":
            return False
    if key not in tag_docs.parsed_infobox(language).keys():
        return True
    return False

def is_key_reportable_as_missing_in_template(key, tag_docs, language):
    page_name = tag_docs.base_title()
    template = tag_docs.parsed_infobox(language)
    if is_page_skipped_for_now_from_missing_parameters(tag_docs):
        return False
    if key in template.keys() and template[key].strip() != "":
        # it is not missing
        return False
    if key == "image":
        if is_adding_image_important(tag_docs) == False:
            return False
    if key == "description":
        if is_page_skipped_for_now_from_missing_description(tag_docs):
            return False
    return True

def normalize_status_string(status):
    if status == None:
        return None
    status = status.lower()

    if status == "defacto":
        return "de facto"

    if status == "import":
        return "imported"

    if status == "inuse":
        return "in use"

    if status in ["unspecified", "unknown", "undefined"]:
        return None
    return status

def normalize(in_template, in_data_item, key):
    normalized_in_data_item = in_data_item
    normalized_in_template = in_template
    if normalized_in_template != None:
        # for comparison skip comments in template
        normalized_in_template = re.sub('<!--.*-->', '', normalized_in_template)

    if normalized_in_template != None:
        normalized_in_template = normalized_in_template.strip()
        if normalized_in_template == "":
            normalized_in_template = None

    if key == "wikidata":
        if in_data_item == None and in_template != None:
            print(":", url, "Wikidata link is not mentioned in data item, it should be present there to make future elimination of wikidata from infobox easier")
            written_something = True
        if normalized_in_template == None and normalized_in_data_item != None:
            normalized_in_template = valid_wikidata(page_name)

    if key == "statuslink":
        if normalized_in_data_item != None:
            normalized_in_data_item = normalized_in_data_item.removeprefix("https://wiki.openstreetmap.org/wiki/")
            normalized_in_data_item = normalized_in_data_item.replace("%22", '"')
            normalized_in_data_item = normalized_in_data_item.replace("_", ' ')
        if normalized_in_template != None:
            normalized_in_template = normalized_in_template.replace("_", ' ')

    if key == "image":
        if normalized_in_template != None:
            normalized_in_template = normalized_in_template.removeprefix("Image:")
            normalized_in_template = normalized_in_template.removeprefix("File:")
            normalized_in_template = normalized_in_template.replace("_", " ")

    if key == "status":
        normalized_in_template = normalize_status_string(normalized_in_template)

        # obsolete and deprecated are not worth distinguishing
        if normalized_in_data_item != normalized_in_template:
            dead = ["obsolete", "deprecated", "abandoned"]
            if normalized_in_data_item in dead:
                if normalized_in_template in dead:
                    normalized_in_data_item = normalized_in_template
            proposed = ["proposed", "draft"]
            if normalized_in_data_item in proposed:
                if normalized_in_template in proposed:
                    normalized_in_data_item = normalized_in_template

    if key == "description":
        if normalized_in_template != None:
            normalized_in_template = normalize_description(normalized_in_template)
            normalized_in_data_item = normalize_description(normalized_in_data_item)

    return normalized_in_template, normalized_in_data_item

def add_missing_parameters_and_missing_values_report(report, tag_docs, language):
    mandatory = ["onNode", "onWay", "onArea", "onRelation", "image", "description", "status"]
    page_name = tag_docs.title_in_language(language)
    if page_name == None:
        return report # no page to check
    url = links.osm_wiki_page_link(page_name)
    for key in mandatory:
        if key in tag_docs.parsed_data_item().keys():
            # it is in data item, warning about copying will appear
            continue
        if is_key_reportable_as_completely_missing_in_template(key, tag_docs, language):
            report["issues"].append({"page_name": page_name, "osm_wiki_url": url, "type": "missing_key_in_infobox", "key": key})
        elif is_key_reportable_as_missing_in_template(key, tag_docs, language) and key not in tag_docs.parsed_data_item():
            report["issues"].append({"page_name": page_name, "osm_wiki_url": url, "type": "missing_value_in_infobox_with_key_present", "key": key})
            if key == "image":
                report["issues"][-1]["embedded_image_present"] = tag_docs.is_there_embedded_image(language) # which language should be used?
    return report

def compare_data(tag_docs):
    report = {"issues": []}
    page_name = tag_docs.base_title()
    # title_in_language("Pl")
    url = None
    if page_name == None:
        page_name = tag_docs.wiki_documentation[0]
        url = links.osm_wiki_page_link(page_name)
        print(url, "has no English version")
        report["issues"].append({"page_name": page_name, "osm_wiki_url": url, "type": "missing English article"})
        return report
    else:
        url = links.osm_wiki_page_link(page_name)
    tag_docs.spot_issues_in_page_text('en')
    written_something = False
    template = tag_docs.parsed_infobox('en')
    if template == {}:
        return # for example, on pages where Template:Deprecated calls it internally
    report = add_missing_parameters_and_missing_values_report(report, tag_docs, 'en')
    report = add_missing_parameters_and_missing_values_report(report, tag_docs, 'Pl')
    for key in set(set(tag_docs.parsed_data_item().keys()) | set(template.keys())):
        if key in ["data_item_id"]:
            continue # not actual data
        if key == "seeAlso" or key == "combination":
            continue # TODO implement parsing that in future to make copying easier
        if key == "wikidata":
            continue # big time sing, it would be smarter to work on removal it from infoboxes

        in_data_item = tag_docs.parsed_data_item().get(key)
        in_template = template.get(key)
        normalized_in_template, normalized_in_data_item = normalize(in_template, in_data_item, key)
        
        if normalized_in_template == None:
            if key == "group":
                continue # do not report leaks here (for now - TODO!)
            if in_data_item == None:
                continue
            print(":", url, "-", key, "is from data item (", in_data_item, ")")
            written_something = True
            if key == "wikidata":
                    print(': https://www.wikidata.org/wiki/' + in_data_item)
                    print("<pre>")
                    print('        "' + page_name.replace(" ", "_") + '": "' + in_data_item + '",')
                    print("</pre>")
            continue
        
        if key in ["onNode", "onWay", "onArea", "onRelation"]:
            if "status" in template:
                if template["status"] in ["obsolete", "deprecated"]:
                    if normalized_in_template == "no":
                        if normalized_in_data_item != None and normalized_in_data_item != "no":
                            # ignores cases where onNode, onWay etc all can be set to 'no'
                            # may be worth special handling if someone cares about fixing data items
                            # or to reduce risk of damage
                            # but disabled for now
                            # TODO
                            normalized_in_data_item = "no"

        if in_template != None and in_data_item != None:
            if key == "image":
                continue # do not report mismatches here
            if key == "description":
                continue # do not report mismatches here
            if normalized_in_template != normalized_in_data_item:
                if "?" not in in_data_item: # skip not parsed data items
                    data_item_url = "https://wiki.openstreetmap.org/wiki/Item:" + tag_docs.parsed_data_item()["data_item_id"]
                    report["issues"].append({"page_name": page_name, "osm_wiki_url": url, 'data_item_url': data_item_url, "type": "mismatch between OSM Wiki and data item", "key": key, 'osm_wiki_value': in_template, 'data_item_value': in_data_item})
    if print_report_to_stdout(report):
        written_something = True
    if written_something:
        print()
        report["written_something"] = written_something
    return report

def print_report_to_stdout(report):
    written_something = False
    for issue in report["issues"]:
        if issue["type"] == "missing_key_in_infobox":
            print(":", issue['osm_wiki_url'], issue["key"], "is missing and not present even as an empty parameter")
            written_something = True
        if issue["type"] == "missing_value_in_infobox_with_key_present":
            if issue["key"] == "image":
                if issue["embedded_image_present"]:
                    print(":", issue['osm_wiki_url'], issue["key"], "value is missing in the infobox template, but article has an image already")
                else:
                    pass # try to delegate
            else:
                print(":", issue['osm_wiki_url'], issue["key"], "value is missing in the infobox template")
            written_something = True
        if issue["type"] == "mismatch between OSM Wiki and data item":
            if issue["key"] == "description":
                print(":", issue["osm_wiki_url"], issue["data_item_url"], "-", issue["key"], "are mismatched between OSM Wiki and data item")
                print("::", issue['osm_wiki_value'])
                print("::", issue['data_item_value'])
                written_something = True
            else:
                print(":", issue["osm_wiki_url"], issue["data_item_url"], "-", issue["key"], "are mismatched between OSM Wiki and data item (", issue['osm_wiki_value'], "vs", issue['data_item_value'], ")")
                written_something = True
    return written_something

def normalize_description(description):
    if description == None:
        return description
    if description == "":
        return description
    if description[-1] != ".":
        return description
    return description[:-1]

def valid_wikidata(page_name):
    # why not added? Because I consider wikidata parameter as a mistake
    # why listed here? To detect invalid ones
    page_name = page_name.replace(" ", "_")
    wikidata = {
        "Tag:aerialway=chair_lift": "Q850767",
        "Tag:barrier=toll_booth": "Q1364150",
        "Tag:man_made=survey_point": "Q352956",
        "Tag:natural=wood": "Q4421",
        "Tag:highway=motorway_junction": "Q353070",
        "Tag:amenity=cafe": "Q30022",
        "Tag:barrier=hedge": "Q235779",
        "Tag:bicycle=no": "Q66361472",
        "Tag:barrier=city_wall": "Q16748868",
        "Tag:waterway=canal": "Q12284",
        "Tag:power=generator": "Q131502",
        "Tag:amenity=biergarten": "Q857909",
        "Tag:place=city": "Q515",
        "Tag:highway=mini_roundabout": "Q12037720",
        "Tag:highway=footway": "Q3352369",
        "Tag:man_made=pipeline": "Q16885408",
        "Tag:highway=residential": "Q97674120",
        "Tag:public_transport=stop_position": "Q548662",
        "Tag:landuse=farmland": "Q3395383",
        "Tag:sport=canoe": "Q20856109",
        "Tag:sport=cricket": "Q5375",
        "Tag:sport=croquet": "Q193387",
        "Tag:sport=korfball": "Q192937",
        "Tag:sport=pelota": "Q26261727",
        "Tag:sport=rowing": "Q159354",
        "Tag:sport=dog_racing": "Q1345388",
        "Tag:sport=hockey": "Q1622659",
        "Tag:sport=multi": "Q97324747",
        "Tag:sport=racquet": "Q2426135",
        "Tag:sport=rugby": "Q5378",
        "Tag:sport=cycling": "Q53121",
        "Tag:sport=shooting": "Q206989",
        "Tag:waterway=ditch": "Q2048319",
        "Tag:landuse=grass": "Q643352",
        "Tag:amenity=bbq": "Q853185",
        "Tag:man_made=water_works": "Q11849395",
        "Tag:service=siding": "Q21683257",
        "Tag:railway=funicular": "Q142031",
        "Tag:aerialway=mixed_lift": "Q3546684",
        "Tag:aerialway=gondola": "Q1576693",
        "Tag:natural=lake": "Q23397",
        "Tag:man_made=mineshaft": "Q556186",
        "Tag:man_made=cutline": "Q487843",
        "Tag:maritime=yes": "Q3089219", # one of two uses matches
        "Tag:boundary=maritime": "Q3089219",
        "Tag:information=board": "Q76419950",
        "Tag:route=ferry": "Q18984099",
        "Tag:aeroway=aerodrome": "Q62447",
        "Tag:amenity=grave_yard": "Q39614",
        "Tag:highway=path": "Q5004679",
        "Tag:highway=bridleway": "Q1639395",
        "Tag:amenity=bar": "Q187456",
        "Tag:highway=street_lamp": "Q503958",
        "Tag:boundary=political": "Q192611",
        "Tag:information=tactile_model": "Q25382084",
        "Tag:junction=jughandle": "Q2642279",
        "Tag:tower:type=observation": "Q1440300",
        "Tag:office=government": "Q327333",
        "Tag:man_made=monitoring_station": "Q6130002",
        "Tag:man_made=flagpole": "Q1971570",
        "Tag:sport=skating": "Q14300548",
        "Tag:landform=raised_beach": "Q17155155",
        "Tag:sport=rugby_league": "Q10962",
        "Tag:sport=rugby_union": "Q5849",
        "Tag:sport=gaelic_football": "Q204632",
        "Tag:sport=gaelic_games": "Q2447366",
        "Tag:microbrewery=yes": "Q5487333",
        "Tag:man_made=adit": "Q58917",
        "Tag:emergency=rescue_box": "Q40049164",
        "Tag:route=piste": "Q1281105",
        "Tag:landuse=plant_nursery": "Q155511",
        "Tag:emergency=water_tank": "Q6501028",
        "Tag:historic=tomb": "Q381885",
    }
    return wikidata.get(page_name)

class TagWithDocumentation():
    def __init__(self, pages):
        self.wiki_documentation = pages
        self.page_texts = {}
        self.data_item = None
    
    def register_wiki_page(self, page_title):
        self.wiki_documentation.append(page_title)

    def parsed_data_item(self):
        if self.data_item == None:
            self.data_item = extract_data_item.page_data(self.base_title())
        return self.data_item

    def parsed_infobox(self, language): # TODO handle multiple languages
        self.load_page_text(language)
        try:
            return extract_infobox_data.turn_page_text_to_parsed(self.page_texts[language], self.title_in_language(language))
        except ValueError:
            print(":", language, self.base_title(), "parsing failed")
            print(links.osm_wiki_page_link(self.base_title()))
            return None
    
    def is_there_embedded_image(self, language):
        text = self.language_page_text(language)
        if text.find("[[Image:") != -1:
            return True
        if text.find("[[File:") != -1:
            return True
        return False

    # TODO: detect marked as obsolete/abandoned with some real use (>100?)
    def is_dying_tag(self):
        template = self.parsed_infobox('en') # no matter what translation declares
        if template == None:
            print("failed to process template :(")
            return False
        if "status" in template:
            if template["status"] == None:
                return False
            return normalize_status_string(template["status"]) in self.unimportant_tag_status()
        return False

    def is_import_tag(self):
        template = self.parsed_infobox('en') # no matter what translation declares
        if "status" in template:
            return normalize_status_string(template["status"]) in ["imported"]
        return False

    def unimportant_tag_status(self):
        return ["obsolete", "abandoned", "deprecated", "proposed", "draft", "discardable"]

    def base_title(self):
        for page_title in self.wiki_documentation:
            if page_title.find("Tag:") == 0 or page_title.find("Key:") == 0:
                return page_title
    
    def title_in_language(self, lang_code):
        if lang_code == self.base_language():
            return self.base_title()
        for page_title in self.wiki_documentation:
            root_page_title = page_title.removeprefix(lang_code)
            if page_title != root_page_title:
                if root_page_title.find("Tag:") == 0 or root_page_title.find("Key:") == 0:
                    return page_title
    
    def base_page_text(self):
        self.load_page_text(self.base_language())
        return self.page_texts[self.base_language()]
    
    def language_page_text(self, language):
        self.load_page_text(language)
        return self.page_texts[language]

    def base_language(self):
        return 'en'

    def load_page_text(self, language):
        if language not in self.page_texts:
            connection = pywikibot.Site('en', 'osm')
            self.page_texts[language] = pywikibot.Page(connection, self.title_in_language(language)).text

    def spot_issues_in_page_text(self, language):
        self.load_page_text(language)
        self.spot_issues_in_a_given_page(self.page_texts[language], self.title_in_language(language))
    
    def spot_issues_in_a_given_page(self, text, page_name):
        url = links.osm_wiki_page_link(page_name)
        parsed_text = mwparserfromhell.parse(text)

        if "DISPLAYTITLE" in text:
            print(url, "has unneded DISPLAYTITLE template")

        unwanted_mapping_format = ["How to map as a node or area", "How to map as a building", "How to map as grounds"]
        for template in unwanted_mapping_format:
            if template in text:
                print(":", url, "has unwanted '" + template + "' template")
                print(":: Draw [[area]] marking this feature. It is also OK to set a [[node]] at its center.")
                print(":: Set a node at the center of the feature or [[area]] along its outline.")
  
        self.detect_magic_tag_lister_mentioning_common_tags(parsed_text, page_name) # detects {{Common tags to use in combination}}
        self.detect_invalidly_disabled_linking(parsed_text, page_name) # detects {{building|church}}
        self.detect_repeated_parameters(parsed_text, page_name) # detects {{ambox|text=Ala|text=Kasia}}

    def detect_magic_tag_lister_mentioning_common_tags(self, parsed_text, page_name):
        url = links.osm_wiki_page_link(page_name)
        for template in parsed_text.filter_templates():
            if template.name.lower() == "common tags to use in combination":
                template_is_not_weird = True
                print(":", url, 'Common tags to use in combination - unwanted template detected')
                print(":Edit description")
                parameters_available_in_common_tags_template = ['addr', 'name', 'opening_hours', 'wheelchair', 'phone', 'email', 'website', 'wikipedia', 'drive_through', 'operator', 'brand']
                for param in template.params:
                    if param != '' and "=" in param:
                        key = param.split("=")[0]
                        if key not in parameters_available_in_common_tags_template:
                            print(": Weird parameter", key)
                            template_is_not_weird = False
                        value = template.get(key).value
                        if value.strip() != "yes":
                            print(": Unexplained weird value")
                            print(":", url, param)
                            print(":", url, template.params)
                            template_is_not_weird = False
                    else:
                        print(": Unexplained weird positional parameters in", template.name.strip())
                        print(":", url, param)
                        print(":", url, template.params)
                        template_is_not_weird = False
                if template_is_not_weird:
                    # at this point we got standard template :)
                     print(":Making page easier to edit by turning magic template into standard tag list")
                     for parameter in parameters_available_in_common_tags_template:
                        value = template.get(key).value
                        if value.strip() != "yes":
                            raise
                        else:
                            # https://wiki.openstreetmap.org/wiki/User:Mateusz_Konieczny/improve_editability
                            print("* {{Tag|" + value + "}}")

    def detect_repeated_parameters(self, parsed_text, page_name):
        url = links.osm_wiki_page_link(page_name)
        templates = parsed_text.filter_templates()
        for template in templates:
            keys = []
            for param in template.params:
                if param != '' and "=" in param:
                    key = param.split("=")[0]
                    if key in keys:
                        print(url, template.name.strip(), "repeats parameter \"" + key + '"')
                    keys.append(key)

    def detect_invalidly_disabled_linking(self, parsed_text, page_name):
        url = links.osm_wiki_page_link(page_name)
        templates = parsed_text.filter_templates()
        for template in templates:
            if template.name.lower() == "tag":
                if len(template.params) > 2:
                    if template.params[1] == '' and len(template.params) == 3:
                        if self.is_parameter_with_linkable_value(template.params[0]):
                            if "/" in template.params[2]:
                                continue
                            if ";" in template.params[2]:
                                # TODO still complain if page exists for such tag
                                continue
                            if "user defined" in template.params[2]:
                                continue
                            if "type of" in template.params[2]:
                                continue
                            if "name of" in template.params[2]:
                                continue
                            tag = str(template.params[0]) + "=" + str(template.params[2])
                            target = "Tag:" + tag.replace("_", " ")
                            if target != page_name: # TODO use remove_language_prefix_if_present
                                if tag not in missing_wiki_pages.blacklisted_tags_that_do_not_need_pages():
                                    if template.params[0] in missing_wiki_pages.keys_where_values_should_be_documented():
                                        print(":", url, 'has disabled link that should be active in <nowiki>{{Tag|' + str(template.params[0]) + "||" + str(template.params[2]) + "}}</nowiki> template (replace double line with single line to activate it)")
                                    else:
                                        pass # maybe enable in future
                    else:
                        pass
                        #print(url, 'has weird tag template', template.params)

    def is_parameter_with_linkable_value(self, parameter):
        for banned_prefix in ['name', 'operator', 'description', 'maxspeed', 'species', 'genus', 'opening_hours', 'ref',
            'old_ref', "is_in", 'plant:output:', 'height', 'start_date', 'frequency', 'capacity', 'max_age', 'min_age',
            'width', 'brand', 'wikidata', 'wikipedia', 'maxheight', 'maxweight', 'created_by', 'population', 'addr:',
            'int_ref', 'old_ref', 'colour', 'incline']:
            if parameter.find(banned_prefix) == 0:
                return False
        for banned_anywhere in ['wikidata']:
            if banned_anywhere in parameter:
                return False
        return True

def pages_grouped_by_tag():
    titles = []
    site = pywikibot.Site('en', 'osm')
    for infobox in ["Template:KeyDescription", "Template:ValueDescription"]:
        root_page = pywikibot.Page(site, infobox)
        for page in root_page.getReferences(namespaces=[0], content=True):
            titles.append(page.title())
    return pages_grouped_by_tag_from_list(titles)


def remove_language_prefix_if_present(title):
    if title.find("Tag:") == 0 or title.find("Key:") == 0:
        return title
    language_prefix = title.split(":")[0]
    root = title.removeprefix(language_prefix + ":")
    if root.find("Tag:") == 0 or root.find("Key:") == 0:
        return root
    else:
        print("Invalid title:", title)
        return None

def pages_grouped_by_tag_from_list(titles):
    pages = {}
    supposedly_invalid_pages = []
    for title in titles:
        if title in ["Wiki organisation", "Pl:Struktura Wiki", 'Taginfo/Parsing the Wiki', 'Data items',
                                'Pl:Data items', 'Fa:Wiki organisation', 'Tag status', 'Uk:Data items',
                                'Fa:Data items', 'Taginfo/Embedding', 'Uk:Організація Вікі', 'Pt:Cycle routes',
                                "Machine-readable Map Feature list", 'Machine-readable Map Feature list/Archive',
                                'Machine-readable Map Feature list/Tagwatch-libs', 'Roles for recreational route relations',
                                'Fa:Wiki Translation', 'Pt:Organização da wiki', 'Philippines/Mapping Fire Hazard Zones',
                                'WikiProject Water leisure', 'Taginfo/Taglists', 'Public transport in Barrie',
                                'Ar:مفتاح:المجرى المائي', # instead of Ar:Key:waterway https://wiki.openstreetmap.org/wiki/Talk:Ar:%D9%85%D9%81%D8%AA%D8%A7%D8%AD:%D8%A7%D9%84%D9%85%D8%AC%D8%B1%D9%89_%D8%A7%D9%84%D9%85%D8%A7%D8%A6%D9%8A
                                'Ar:مفتاح:طبيعي',
                                ]:
            continue
        if title.find("Proposed features/") == 0:
            continue
        if title.find("POI:") == 0:
            continue
        root = remove_language_prefix_if_present(title)
        if root != None:
            index = root.replace("_", " ")
            if index not in pages:
                pages[index] = TagWithDocumentation([])
            if title not in pages[index].wiki_documentation: # why it is needed? HACK TODO
                pages[index].register_wiki_page(title)
        else:
            print("Invalid title:", title)
            supposedly_invalid_pages.append(title)
    if len(supposedly_invalid_pages) > 0:
        print(supposedly_invalid_pages)
        print("above are supposedly invalid pages")
    return pages

def self_check_on_init():
    "ab".removeprefix("a") # quick check that we are running python 3.9+
    compare_data(TagWithDocumentation(["Tag:amenity=townhall", "Tag:railway=subway"]))
    compare_data(TagWithDocumentation(["Tag:amenity=trolley_bay"]))
    compare_data(TagWithDocumentation(["Key:right:country"]))
    entry = TagWithDocumentation(["Tag:utility=power"])
    text = entry.base_page_text()
    print(compare_data(entry))
    print("is_key_reportable_as_missing_in_template(\"image\", entry) =", is_key_reportable_as_missing_in_template("image", entry, 'en'))
    print("is_adding_image_important(entry) =", is_adding_image_important(entry))
    print(entry.parsed_infobox('en'))
    print(entry.parsed_infobox('en')["status"])

def images_help_prefix():
    report = "\n"
    report += "images are missing in the infobox:\n"
    report += "------------\n"
    report += "Chcę się pochwalić że właśnie dodałem ilustracje do\n"
    report += "I just added images to\n"
    report += "\n"
    report += "\n"
    report += "Help with other would be appreciated, there are many other waiting\n"
    report += "Przy okazji OSM Wiki: gdyby ktoś dał radę znaleźć na https://commons.wikimedia.org/ ilustracje dla tych tagów to byłbym bardzo wdzięczny\n"
    report += "If someone want to help wiki a bit - you can help by finding a suitable image for one of articles listed below (if you want - you can just link something from https://commons.wikimedia.org/ and I will add it if you prefer to avoid editing part itself).\n"
    report += "https://wiki.openstreetmap.org/wiki/Creating_a_page_describing_key_or_value#Image has a bit more\n"
    return report

def images_help_suffix():
    report = ""
    report += "(if you edit wiki - it is likely that this pages would benefit also from other improvements)\n"
    report += "jak ktoś podlinkuje dobre zdjęcie to na wiki mogę już dodać\n"
    return report

def update_reports(reports_for_display, group):
    report = compare_data(group)
    if report != None:
        for issue in report["issues"]:
            if issue["type"] == "missing_value_in_infobox_with_key_present":
                if taginfo.count_appearances_from_wiki_page_title(group.base_title()) >= 5000:
                    if issue["key"] == "image":
                        if issue["embedded_image_present"] == False:
                            reports_for_display['missing_images_template_ready_for_adding'].append(issue)
                    if issue["key"] == "status":
                        reports_for_display['missing_status_template_ready_for_adding'].append(issue)
            if issue["type"] == "mismatch between OSM Wiki and data item":
                reports_for_display['mismatches_between_osm_wiki_and_data_items'].append(issue)

    return reports_for_display


def collect_reports():
    site = pywikibot.Site('en', 'osm')
    processed = 0
    reports_for_display = {
        'missing_images_template_ready_for_adding': [],
        'missing_status_template_ready_for_adding': [],
        'mismatches_between_osm_wiki_and_data_items': [],
    }
    pages = pages_grouped_by_tag()
    keys = list(pages.keys())
    random.shuffle(keys)
    for index in keys:
        group = pages[index]
        reports_for_display = update_reports(reports_for_display, group)
        processed += 1
        if processed % 1000 == 0:
            print("processed", processed, "out of", len(keys))
        if len(reports_for_display['missing_images_template_ready_for_adding']) > 10:
            if len(reports_for_display['missing_status_template_ready_for_adding']) > 10:
                if len(reports_for_display['mismatches_between_osm_wiki_and_data_items']) >= 1:
                    break
    return reports_for_display

def osm_wiki_improvements_prefix():
    header = ""
    header += "List of obviously needed improvements to OSM Wiki\n"
    header += "\n"
    header += "OSM Wiki includes plenty of useful documentation, but more is needed.\n"
    header += "Help would be highly welcomed - there is need to both improve existing wiki pages and to document tags that are not documented right now.\n"
    header += "\n"
    return header

def missing_pages_report():
    header = ""
    header += "Tags with quickly growing usage but without own page\n"
    header += "------------\n"
    header += "see https://wiki.openstreetmap.org/wiki/Creating_a_page_describing_key_or_value for some info how OSM Wiki pages are created\n"
    header += "note: linked page is in a very early draft, edits, contributions are greatly appreciated!\n"
    header += "Even comments about what is unclear or missing greatly increase chance of further improvements.\n"
    header += "For example comment which TODO is especially important is very likely to result in edit fixing it.\n"
    header += "\n"
    header += "------------\n"
    header += "\n"
    header += "Following are tags with growing usage without their wiki page. Either fixing that tagging or creating page documenting de facto use is needed.\n"
    header += "\n"
    header += "Note also that pages may exist as just redirects! If page redirects to place where it is explained it may be still useful to create a separate page for it.\n"
    missing_pages = missing_wiki_pages.undocumented_values_among_popular_tags_reports()
    return header + missing_pages

def ascii_url_formatter(url):
    return url

def mediawiki_url_formatter(url):
    human_readable = links.osm_wiki_page_name_from_link(url)
    if human_readable != None:
        return "[" + url + " " + human_readable + "]"

    human_readable = links.osm_data_entity_code_from_link(url)
    if human_readable != None:
        return "[" + url + " " + human_readable + "]"
    
    raise ValueError("impossible happened with " + url)        

def main():
    self_check_on_init()

    reports_for_display = collect_reports()
    missing_pages = missing_pages_report()

    print(osm_wiki_improvements_prefix())
    print(missing_pages)
    display_reports(reports_for_display, ascii_url_formatter)

    print()
    print()
    print()

    print(osm_wiki_improvements_prefix())
    print(missing_pages)
    display_reports(reports_for_display, mediawiki_url_formatter)

def display_reports(reports_for_display, url_formatter):
    # dump due to bug
    #print(reports_for_display)
    #pprint.pp(reports_for_display)
    # dump due to bug

    report = ""
    report += "== Organised overview of major issues =="

    report_segment = reports_for_display['missing_images_template_ready_for_adding']
    if len(report_segment) > 0:
        report += images_help_prefix()
        for issue in report_segment:
            try:
                report += "* " + url_formatter(issue["osm_wiki_url"]) + "\n"
            except KeyError:
                print(issue)
                raise
        report += images_help_suffix()
    report_segment = reports_for_display['missing_status_template_ready_for_adding']
    if len(report_segment) > 0:
        report += "\n"
        report += "missing status parameter in the infobox, adding it would be useful"
        report += "see https://wiki.openstreetmap.org/wiki/Template:Tag_status_values for documentation of meaning of values and their list"
        for issue in report_segment:
            try:
                report += "* " + url_formatter(issue["osm_wiki_url"]) + "\n"
            except KeyError:
                print(issue)
                raise
    report_segment = reports_for_display['mismatches_between_osm_wiki_and_data_items']
    if len(report_segment) > 0:
        report += "\n"
        report += "mismatch between [[data item]] and OSM Wiki:\n"
        for issue in report_segment:
            try:
                line = ""
                line += "* "
                line += url_formatter(issue["osm_wiki_url"]) + " "
                line += url_formatter(issue["data_item_url"]) + " "
                line += issue["key"] + "( <code>" + issue['osm_wiki_value'] + "</code> vs <code>" + issue['data_item_value'] + "</code> )" 
                line += "\n"
                report += line
            except KeyError:
                print(issue)
                print("mismatches_between_osm_wiki_and_data_items have incomplete data")
                raise
            except TypeError:
                print(issue)
                print("type handling bug")
                raise
    print(report)

main()
