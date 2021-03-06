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

# https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Install_Pywikibot
# I followed it, run script, and recopied it here
# https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script

# TODO: detect incomplete skeleton (distinguish missing parameter and no parameter set)

def unimportant_tag_status():
    return ["obsolete", "abandoned", "deprecated", "proposed", "draft", "discardable"]

def is_unimportant_tag_status(status):
    return normalize_status_string(status) in unimportant_tag_status()

def is_imported_tag_status(status):
    return normalize_status_string(status) in ["imported"]

def is_there_embedded_image(tag_docs):
    if tag_docs.base_page_text().find("[[Image:") != -1:
        return True
    if tag_docs.base_page_text().find("[[File:") != -1:
        return True
    return False

def is_adding_image_important(tag_docs):
    page_name = tag_docs.base_page()
    template = tag_docs.parsed_infobox()
    if "status" in template:
        if is_unimportant_tag_status(template["status"]):
            # TODO: detect marked as proposed with significant use
            return False
        if is_imported_tag_status(template["status"]):
            return False # TODO - for now at least
    banned_parts = ["source", "ref:", "is_in", "not:", "_ref", "tiger:", "description", "operator"]
    banned_parts += ["naptan:", "Tag:landmark=", "seamark", "code", "_id"] # TODO - for potential enabling
    banned_parts += ["Key:nvdb:"] # looks like an import, TODO verification after everything else
    banned_parts += ["Key:no"] # noaddress, noref etc - probably plenty of false positives...
    for ban in banned_parts:
        if ban.replace('_', ' ') in page_name.replace('_', ' '):
            return False
    if is_page_skipped_for_now_from_missing_parameters(tag_docs):
        return False
    return True

def is_page_skipped_for_now_from_missing_parameters(tag_docs):
    page_name = tag_docs.base_page()
    template = tag_docs.parsed_infobox()
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
    if "status" in template:
        if is_unimportant_tag_status(template["status"]):
            # TODO: detect marked as obsolete/abandoned with some real use (>100?)
            return True
    return False

def is_page_skipped_for_now_from_missing_description(tag_docs):
    page_name = tag_docs.base_page()
    if "Tag:crop=" or "Tag:wood=" in page_name: # give up with this group 
        return True
    if "Tag:mooring=" in page_name: # give up with this group 
        return True
    if is_unimportant_tag_status(status):
        return True # TODO - maybe consider as low importance?

def is_key_reportable_as_completely_missing_in_template(key, tag_docs):
    page_name = tag_docs.base_page()
    if is_page_skipped_for_now_from_missing_parameters(tag_docs):
        return False
    if "Tag:source=" in page_name:
        if key == "image":
            return False
    if key not in tag_docs.parsed_infobox().keys():
        return True
    return False

def is_key_reportable_as_missing_in_template(key, tag_docs):
    page_name = tag_docs.base_page()
    template = tag_docs.parsed_infobox()
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

    if key == "description":
        if normalized_in_template != None:
            normalized_in_template = normalize_description(normalized_in_template)
            normalized_in_data_item = normalize_description(normalized_in_data_item)

    return normalized_in_template, normalized_in_data_item

def compare_data(tag_docs):
    report = {"issues": []}
    page_name = tag_docs.base_page()
    url = None
    if page_name == None:
        print(tag_docs.wiki_documentation, "has no English version")
        page_name = tag_docs.wiki_documentation[0]
        report["issues"].append({"page_name": page_name, "osm_wiki_url": links.osm_wiki_page_link(page_name), "type": "missing English article"})
        return report
    else:
        url = links.osm_wiki_page_link(page_name)
    data_item = tag_docs.parsed_data_item()
    template = tag_docs.parsed_infobox()
    tag_docs.spot_issues_in_page_text()
    written_something = False
    if template == {}:
        return # for example, on pages where Template:Deprecated calls it internally
    mandatory = ["onNode", "onWay", "onArea", "onRelation", "image", "description", "status"]
    for key in mandatory:
        if key in data_item.keys():
            # it is in data item, warning about copying will appear
            continue
        if is_key_reportable_as_completely_missing_in_template(key, tag_docs):
            report["issues"].append({"page_name": page_name, "osm_wiki_url": url, "type": "missing_key_in_infobox", "key": key})
        elif is_key_reportable_as_missing_in_template(key, tag_docs) and key not in data_item:
            report["issues"].append({"page_name": page_name, "osm_wiki_url": url, "type": "missing_value_in_infobox_with_key_present", "key": key})
            if key == "image":
                report["issues"][-1]["embedded_image_present"] = is_there_embedded_image(tag_docs)
    for issue in report["issues"]:
        if issue["type"] == "missing_key_in_infobox":
            print(":", url, issue["key"], "is missing and not present even as empty parameter")
            written_something = True
        if issue["type"] == "missing_value_in_infobox_with_key_present":
            if issue["key"] == "image":
                if issue["embedded_image_present"]:
                    print(":", url, issue["key"], "value is missing in the infobox template, but article has an image already")
                else:
                    pass # try to delegate
            else:
                print(":", url, issue["key"], "value is missing in the infobox template")
            written_something = True
    for key in set(set(data_item.keys()) | set(template.keys())):
        if key in ["data_item_id"]:
            continue # not actual data
        if key == "seeAlso" or key == "combination":
            continue # TODO implement parsing that in future to make copying easier
        if key == "wikidata":
            continue # big time sing, it would be smarter to work on removal it from infoboxes

        in_data_item = data_item.get(key)
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
                if key == "description":
                    print(":", url, "https://wiki.openstreetmap.org/wiki/Item:" + data_item["data_item_id"], "-", key, "are mismatched between OSM Wiki and data item")
                    print("::", in_template)
                    print("::", in_data_item)
                    written_something = True
                elif "?" not in in_data_item:
                    print(":", url, "https://wiki.openstreetmap.org/wiki/Item:" + data_item["data_item_id"], "-", key, "are mismatched between OSM Wiki and data item (", in_template, "vs", in_data_item, ")")
                    written_something = True
    if written_something:
        print()
        report["written_something"] = written_something
    return report

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
        self.page_text = None
        self.data_item = None
    
    def register_wiki_page(self, page_title):
        self.wiki_documentation.append(page_title)

    def parsed_data_item(self):
        if self.data_item == None:
            self.data_item = extract_data_item.page_data(self.base_page())
        return self.data_item

    def parsed_infobox(self): # TODO handle multiple languages
        self.load_page_text()
        return extract_infobox_data.turn_page_text_to_parsed(self.page_text)

    def base_page(self):
        for page_title in self.wiki_documentation:
            if page_title.find("Tag:") == 0 or page_title.find("Key:") == 0:
                return page_title
    
    def base_page_text(self):
        self.load_page_text()
        return self.page_text

    def load_page_text(self):
        if self.page_text == None:
            self.page_text = pywikibot.Page(pywikibot.Site('en', 'osm'), self.base_page()).text

    def spot_issues_in_page_text(self):
        self.load_page_text()
        self.spot_issues_in_a_given_page(self.page_text, self.base_page())
    
    def spot_issues_in_a_given_page(self, text, page_name):
        url = links.osm_wiki_page_link(page_name)
        if "DISPLAYTITLE" in text:
            print(url, "has unneded DISPLAYTITLE template")
        unwanted = ['Common tags to use in combination', "How to map as a node or area", "How to map as a building"]
        for template in unwanted:
            if template in text:
                print(":", url, "has unwanted '" + template + "' template")

        wikicode = mwparserfromhell.parse(text)
        self.detect_invalidly_disabled_linking(wikicode, page_name)
        self.detect_repeated_parameters(wikicode, page_name)

    def detect_repeated_parameters(self, parsed_text, page_name):
        url = links.osm_wiki_page_link(page_name)
        templates = parsed_text.filter_templates()
        for template in templates:
            keys = []
            for param in template.params:
                if param != '' and "=" in param:
                    key = param.split("=")[0]
                    if key in keys:
                        print(url, template.name, "repeats parameter", key)
                    keys.append(key)

    def detect_invalidly_disabled_linking(self, parsed_text, page_name):
        url = links.osm_wiki_page_link(page_name)
        templates = parsed_text.filter_templates()
        for template in templates:
            if template.name.lower() == "tag":
                if len(template.params) > 2:
                    if template.params[1] == '':
                        if self.is_parameter_with_linkable_value(template.params[0]):
                            if "/" not in template.params[2] and "user defined" not in template.params[2]:
                                target = "Tag:" + str(template.params[0]) + ":" + str(template.params[2])
                                if target != page_name: # TODO use remove_language_prefix_if_present
                                    if template.params[0] in missing_wiki_pages.keys_where_values_should_be_documented():
                                        print(url, 'has invalidly not active link in Tag template', template.params)
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
                                'WikiProject Water leisure', 'Taginfo/Taglists']:
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
    print(supposedly_invalid_pages)
    print("above are supposedly invalid pages")
    return pages

def self_check_on_init():
    "ab".removeprefix("a") # quick check that we are running python 3.9+
    compare_data(TagWithDocumentation(["Tag:amenity=trolley_bay"]))
    compare_data(TagWithDocumentation(["Key:right:country"]))
    entry = TagWithDocumentation(["Tag:utility=power"])
    text = entry.base_page_text()
    print(compare_data(entry))
    print("is_key_reportable_as_missing_in_template(\"image\", entry) =", is_key_reportable_as_missing_in_template("image", entry))
    print("is_adding_image_important(entry) =", is_adding_image_important(entry))
    print(entry.parsed_infobox())
    print(entry.parsed_infobox()["status"])

def update_reports(reports_for_display, group):
    report = compare_data(group)
    if report != None:
        for issue in report["issues"]:
            if issue["type"] == "missing_value_in_infobox_with_key_present":
                if taginfo.count_appearances_from_wiki_page_title(group.base_page()) >= 5000:
                    if issue["key"] == "image":
                        if issue["embedded_image_present"] == False:
                            reports_for_display['missing_images_template_ready_for_adding'].append(issue)
                    if issue["key"] == "status":
                        reports_for_display['missing_status_template_ready_for_adding'].append(issue)
    return reports_for_display


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
    report += "(if you edit wiki - it is likely that this pages would benefit also from other improvements)\n"
    report += "jak ktoś podlinkuje dobre zdjęcie to na wiki mogę już dodać\n"
    return report

def collect_reports():
    site = pywikibot.Site('en', 'osm')
    processed = 0
    reports_for_display = {
        'missing_images_template_ready_for_adding': [],
        'missing_status_template_ready_for_adding': [],
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
    missing_pages = missing_wiki_pages.missing_pages()
    return header + missing_pages

def main():
    self_check_on_init()
    report = osm_wiki_improvements_prefix()
    report += missing_pages_report()
    reports_for_display = collect_reports()
    if len(reports_for_display['missing_images_template_ready_for_adding']) > 0:
        report = images_help_prefix()
        for issue in reports_for_display['missing_images_template_ready_for_adding']:
            report += "* " + issue["osm_wiki_url"] + "\n"
        report += images_help_suffix()
    if len(reports_for_display['missing_status_template_ready_for_adding']) > 0:
        print()
        report += "status info is missing and should be added (see https://wiki.openstreetmap.org/wiki/Tag_status ):\n"
        for issue in reports_for_display['missing_status_template_ready_for_adding']:
            report += "* " + issue["osm_wiki_url"] + "\n"
    print(report)

main()
