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
import webbrowser

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
    # removes some mismatches where mismatches are cosmetic
    # or would only improve data items, not OSM Wiki
    # or where reporting them would overload list

    normalized_in_data_item = in_data_item
    normalized_in_template = in_template
    if normalized_in_template != None:
        # for comparison skip comments in template
        normalized_in_template = re.sub('<!--.*-->', '', normalized_in_template)

    if normalized_in_template != None:
        normalized_in_template = normalized_in_template.strip()
        if normalized_in_template == "":
            normalized_in_template = None

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
            normalized_in_template = "File:" + normalized_in_template
        if normalized_in_data_item != None:
            normalized_in_data_item = "File:" + normalized_in_data_item

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


    if key in ["onNode", "onWay", "onArea", "onRelation"]:
        if normalized_in_template != None:
            if "status" in normalized_in_template:
                if normalized_in_template["status"] in ["obsolete", "deprecated"]:
                    if normalized_in_template == "no":
                        if normalized_in_data_item != None and normalized_in_data_item != "no":
                            # ignores cases where onNode, onWay etc all can be set to 'no'
                            # also in the data item
                            # may be worth special handling if someone cares about fixing data items
                            # but disabled for now
                            # TODO
                            normalized_in_data_item = "no"

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

def handle_missing_english_version(tag_docs, report):
    page_name = tag_docs.wiki_documentation[0]
    language = page_name.split(":")[0].lower()
    template = tag_docs.parsed_infobox(language)
    url = links.osm_wiki_page_link(page_name)
    if "status" not in template:
        print(url, "has no English version - and has unknown status", tag_docs)
        report["issues"].append({"page_name": page_name, "osm_wiki_url": url, "type": "missing English article about a tag with an unknown status"})
    elif normalize_status_string(template["status"]) in tag_docs.unimportant_tag_status():
        # not really important...
        #print(url, "has no English version - but it is a proposed/deprecated page anyway", tag_docs)
        report["issues"].append({"page_name": page_name, "osm_wiki_url": url, "type": "missing English article about a proposed/deprecated tag"})
    else:
        print(url, "has no English version", tag_docs)
        report["issues"].append({"page_name": page_name, "osm_wiki_url": url, "type": "missing English article"})
    return report

def compare_data(tag_docs):
    report = {"issues": []}
    for language in tag_docs.available_languages():
        report = compare_data_in_specific_language(tag_docs, report, language)
    return report
    
def compare_data_in_specific_language(tag_docs, report, language):
    # title_in_language("Pl")
    url = None

    page_name = tag_docs.title_in_language(language)
    if tag_docs.base_title() == None:
        report = handle_missing_english_version(tag_docs, report)
        return report
    else:
        url = links.osm_wiki_page_link(page_name)
    tag_docs.spot_issues_in_page_text(language)
    written_something = False
    template = tag_docs.parsed_infobox(language)
    if template == None:
        print("parsing failed on", page_name)
        return report
    page_name = tag_docs.title_in_language(language)
    if template == {}:
        text = tag_docs.language_page_text("en")
        wikicode = mwparserfromhell.parse(text)
        templates = wikicode.filter_templates()
        expected_regular_template_found = False
        deprecated_template_found = False
        for template in templates:
            if template.name.strip().lower() in ["valueDescription", "keydescription"]:
                print(page_name, "has", template.name, "but no content in it")
                expected_regular_template_found = True
            if template.name.strip().lower() in ["deprecated"]:
                deprecated_template_found = False
        if deprecated_template_found and not expected_regular_template_found:
            # Template:Deprecated calls it internally
            # TODO extract what little can be extracted from template Deprecated? maybe?
            return report
        if "seamark" in page_name:
            # many, many stub pages for basically unused tags
            # TODO: remove this
            return
        print("empty template parsing result for", links.osm_wiki_page_link(page_name), "from", page_name, "containing following templates", templates)
        for template in templates:
            if "ValueDescription" in template:
                print("""
{{ValueDescription
| key           = TODO: prefill key from the title
| value         = TODO: prefill value from the title

| image         = 
| description   = 
| group         = 
| onNode        = 
| onWay         = 
| onArea        = 
| onRelation    = 
| requires      = 
| implies       = 
| combination   = 
| seeAlso       = 
| status        = 
| statuslink    = 

}}""")

        return report
    #report = add_missing_parameters_and_missing_values_report(report, tag_docs, 'en') # it should be reported only when data item is leaking, TODO: fix it with bot
    #report = add_missing_parameters_and_missing_values_report(report, tag_docs, 'Pl') # it should be reported only when data item is leaking, TODO: fix it with bot

    for key in set(set(tag_docs.parsed_data_item().keys()) | set(template.keys())):
        if key in ["data_item_id"]:
            continue # not actual data
        if key == "seeAlso" or key == "combination":
            continue # TODO implement parsing that in future to make copying easier

        in_data_item = tag_docs.parsed_data_item().get(key)
        in_template = template.get(key)
        normalized_in_template, normalized_in_data_item = normalize(in_template, in_data_item, key)
        
        if normalized_in_template != None:
            if normalized_in_data_item == None:
                # ignore it! - I am improving OSM Wiki, not data items. 
                # And this is for https://wiki.openstreetmap.org/wiki/Proposed_features/remove_link_to_Wikidata_from_infoboxes
                data_item_url = None
            if key == "wikidata":
                report["issues"].append({"page_name": page_name, "osm_wiki_url": url, "type": "wikidata key present", "key": key, 'osm_wiki_value': in_template})

        if normalized_in_template == None:
            if key == "group":
                continue # do not report leaks here (for now - TODO!)
            if in_data_item == None:
                # do not report problems in data items
                continue
            print(":", url, "-", key, "is from data item (", in_data_item, ")")
            written_something = True
            if key == "wikidata":
                    print(': https://www.wikidata.org/wiki/' + in_data_item)
                    print("<pre>")
                    print('        "' + page_name.replace(" ", "_") + '": "' + in_data_item + '",')
                    print("</pre>")
            continue
        
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
        if issue["type"] == "wikidata key present":
            print(":", issue["osm_wiki_url"], "-", issue["key"], "wikidata key is present in infobox and should be removed (", issue['osm_wiki_value'], ")")
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

class TagWithDocumentation():
    def __init__(self, pages):
        self.wiki_documentation = pages # titles
        self.page_texts = {}
        self.data_item = None
    
    def register_wiki_page(self, page_title):
        self.wiki_documentation.append(page_title)
    
    def available_languages(self):
        returned = []
        base_title = self.base_title()
        for page_title in self.wiki_documentation:
            if page_title == base_title:
                returned.append(self.base_language())
            elif ":" in page_title:
                language_prefix = page_title.split(":")[0]
                title = page_title.removeprefix(language_prefix + ":")
                if title != base_title:
                    print("unexpected title mismatch", title, "vs", base_title, "in", page_title)
                returned.append(language_prefix.lower())
            else:
                print(page_title, "is an unexpected title")
        return returned

    def parsed_data_item(self):
        if self.data_item == None:
            self.data_item = extract_data_item.page_data(self.base_title())
        return self.data_item

    def parsed_infobox(self, language): # TODO handle multiple languages
        self.load_page_text(language)
        try:
            title = self.title_in_language(language, debug=True)
            if title == None:
                raise Exception("no title for language " + language)
            return extract_infobox_data.turn_page_text_to_parsed(self.page_texts[language], title)
        except ValueError:
            print(":", language, self.base_title(), "parsing failed")
            print()
            print("--..--..--")
            print()
            #print(links.osm_wiki_page_link(self.base_title()))
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

    def find_title_in_given_language_among_matching(self, lang_code, title_pool, debug=False):
        for candidate in title_pool:
            main_candidate_part = candidate.lower().removeprefix(lang_code.lower() + ":") # this allows to use both Pl and pl (and pL etc)
            if candidate.lower() != main_candidate_part.lower():
                if main_candidate_part.lower().find("tag:") == 0 or main_candidate_part.lower().find("key:") == 0:
                    return candidate
                else:
                    if debug:
                        print("main_candidate_part", main_candidate_part)
                        print("main_candidate_part.lower().find(\"tag:\")", main_candidate_part.lower().find("tag:"))
                        print("main_candidate_part.lower().find(\"key:\")", main_candidate_part.lower().find("key:"))
            else:
                if debug:
                    print(candidate.lower(), "vs", main_candidate_part.lower())
        if debug:
            print("searching for", lang_code, "in", title_pool, "search failed")

    def title_in_language(self, lang_code, debug=False):
        if lang_code == self.base_language():
            return self.base_title()
        returned = self.find_title_in_given_language_among_matching(lang_code, self.wiki_documentation)
        if returned != None:
            return returned
        if debug:
            if self.find_title_in_given_language_among_matching(lang_code, self.wiki_documentation, debug) != None:
                raise "should never happen"
        return None
    
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
            title = self.title_in_language(language, debug=True)
            if title == None:
                raise Exception("no page in language " + language)
            self.page_texts[language] = pywikibot.Page(connection, title).text

    def spot_issues_in_page_text(self, language):
        self.load_page_text(language)
        self.spot_issues_in_a_given_page(self.page_texts[language], self.title_in_language(language))
        if language.lower() in ["pl", "en"]:
            self.spot_issues_in_a_given_page_requiring_understanding_langage(self.page_texts[language], self.title_in_language(language), language)
    
    def spot_issues_in_a_given_page(self, text, page_name):
        url = links.osm_wiki_page_link(page_name)
        parsed_text = mwparserfromhell.parse(text)

        self.detect_magic_tag_lister_mentioning_common_tags(parsed_text, page_name) # detects {{Common tags to use in combination}}
        self.detect_repeated_parameters(parsed_text, page_name) # detects {{ambox|text=Ala|text=Kasia}}

        if "DISPLAYTITLE" in text:
            print(url, "has unneeded DISPLAYTITLE template")

    def spot_issues_in_a_given_page_requiring_understanding_langage(self, text, page_name, language):
        url = links.osm_wiki_page_link(page_name)
        # TODO detect_invalidly_disabled_linking can be run on all languages after less urgen issues were fixed
        # but maybe only on the most obvious cases or something?
        parsed_text = mwparserfromhell.parse(text)
        self.detect_invalidly_disabled_linking(parsed_text, page_name) # detects {{building|church}}

        # TODO specifically detect its presence in both how to tag section and in the sidebar
        if self.is_dying_tag() == False:
            #if self.parsed_infobox('en')['description'] == "???": # https://wiki.openstreetmap.org/wiki/Tag:shop=hobby
            base_page_name = remove_language_prefix_if_present(page_name)
            if base_page_name.find("Tag:shop=") == 0:
                if base_page_name not in ["Tag:shop=no", "Tag:shop=vacant", "Tag:shop=shopping_centre"]:
                    if "common tags to use in combination" not in text.lower(): # detected later
                        if "{{tag|opening_hours" not in text.lower():
                            if "{{key|opening_hours" not in text.lower():
                                if "{{deprecated" not in text.lower(): # see for example https://wiki.openstreetmap.org/w/index.php?title=Tag:shop%3Dfast_food&action=edit
                                    print(":", url, "Page describing shop should mention opening_hours tag! https://wiki.openstreetmap.org/w/index.php?title=Tag:shop%3Dnuts&action=edit&section=2 may be useful source of properties")

        unwanted_mapping_format = ["How to map as a node or area", "How to map as a building", "How to map as grounds"]
        for template in unwanted_mapping_format:
            if template in text:
                en_area_preferred = ":: <nowiki>Draw an [[area]] marking this feature. It is also OK to set a [[node]] at its center.</nowiki>"
                en_area_strongly_preferred = ":: <nowiki>Draw an [[area]] marking this feature. It is also OK to set a [[node]] at its center, if mapping as area is impossible.</nowiki>"
                en_node_preferred = ":: <nowiki>Set a [[node]] at the center of the feature or draw an [[area]] along its outline.</nowiki>"
                en_messages = [en_area_preferred, en_area_strongly_preferred, en_node_preferred]
                if "Tag:shop" in page_name:
                    en_messages = [en_node_preferred]
                messages = en_messages
                print(":", url, "has unwanted '" + template + "' template. Following text may be used as a base for replacement:")
                for message in messages:
                    print(message)
  
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
                        key = template.params[0]
                        value =  template.params[2]
                        if self.is_tag_linkable(key, value):
                            tag = str(template.params[0]) + "=" + str(value)
                            target = "Tag:" + tag.replace("_", " ")
                            if target != page_name: # TODO use remove_language_prefix_if_present
                                if tag not in missing_wiki_pages.blacklisted_tags_that_do_not_need_pages():
                                    if template.params[0] in missing_wiki_pages.keys_where_values_should_be_documented():
                                        print(":", url, 'has disabled link that should be active in <nowiki>{{Tag|' + str(key) + "||" + str(value) + "}}</nowiki> template (replace double line with single line to activate it)")
                                    else:
                                        pass # maybe enable in future
    def is_tag_linkable(self, key, value):
        if self.is_key_with_linkable_value(key):
            if self.is_tag_value_linkable(key, value):
                return True
        return False

    def is_tag_value_linkable(self, key, value):
        if "/" in value:
            return False
        # "*" is not included as in such case {{Tag|keyname}} is preferred
        if "*" in value and value != "*": # {{Tag|barrier||*_gate}} at https://wiki.openstreetmap.org/wiki/Tag:barrier=gate
            return False
        if ";" in value:
            # TODO still complain if page exists for such tag
            return False
        if "user defined" in value.lower():
            return False
        if "value" == value:
            return False
        if "type of" in value.lower():
            return False
        if "name of" in value.lower():
            return False
        return True

    def is_key_with_linkable_value(self, key):
        for banned_prefix in ['name', 'operator', 'description', 'maxspeed', 'species', 'genus', 'opening_hours', 'ref',
            'old_ref', "is_in", 'plant:output:', 'height', 'start_date', 'frequency', 'capacity', 'max_age', 'min_age',
            'width', 'brand', 'wikidata', 'wikipedia', 'maxheight', 'maxweight', 'created_by', 'population', 'addr:',
            'int_ref', 'old_ref', 'colour', 'incline']:
            if key.find(banned_prefix) == 0:
                return False
        for banned_anywhere in ['wikidata']:
            if banned_anywhere in key:
                return False
        if key in ["construction", # https://wiki.openstreetmap.org/w/index.php?title=Tag:construction%3Dprimary&redirect=no
            "location" # TODO - enable
            ]:
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
                                'Ar:مفتاح:طبيعي', 'Creating a page describing key or value', 'Seamarks/Virtual AtoNs',
                                'York Region Transit', 'Toronto Transit Commission', 'Sandbox Jemily1 sala 1',
                                'Simcoe County transit agencies', 'York Region Transit', 'Toronto Transit Commission', 'Simcoe County transit agencies',
                                "Fire Path", # quite not standard but I like it...
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

    group = TagWithDocumentation(["Tag:historic=castle", "Cs:Tag:historic=castle"])
    if "cs" not in group.available_languages():
        raise "cs missing"
    if "en" not in group.available_languages():
        raise "en missing"
    if len(group.available_languages()) != 2:
        raise "unwanted extra language(s)"
    compare_data(group)
 
 
    if TagWithDocumentation([]).find_title_in_given_language_among_matching('pl', ['Pl:Tag:wood=deciduous'], debug=True) != 'Pl:Tag:wood=deciduous':
        raise Exception("failed to extract correct title")

    # TODO - is key, value really skipped? why?
    text = """{{ValueDescription
    |key=skipped_apparently
    |value=skipped_apparently
    |group=arghhhj
    }}"""

    extracted = extract_infobox_data.turn_page_text_to_parsed(text, "dummy title")
    print(extracted)
    if extracted["group"] != "arghhhj":
        raise Exception("failed to extract correct parameter")

    extracted = extract_infobox_data.turn_page_text_to_parsed("{{Deprecated|oldkey=amenity|oldvalue=community_center|newtext=tag:amenity=community_centre}}", "dummy title")
    if extracted["status"] != "deprecated":
        raise Exception("failed to extract correct parameter")

    print("================================")
    print("https://wiki.openstreetmap.org/wiki/Pl:Tag:building%3Dkiosk - status mismatches main version, should be detected!")
    print("================================")
    # TODO what should happend here?
    compare_data(TagWithDocumentation(["Tag:amenity=trolley_bay"]))
    compare_data(TagWithDocumentation(["Key:right:country"]))
    entry = TagWithDocumentation(["Tag:utility=power"])
    text = entry.base_page_text()
    compare_data(entry)

    print("-000000000000000000000000")

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
                if count_appearances_from_wiki_page_title(group.base_title()) >= 5000:
                    if issue["key"] == "image":
                        if issue["embedded_image_present"] == False:
                            reports_for_display['missing_images_template_ready_for_adding'].append(issue)
                    if issue["key"] == "status":
                        reports_for_display['missing_status_template_ready_for_adding'].append(issue)
            if issue["type"] == "mismatch between OSM Wiki and data item":
                reports_for_display['mismatches_between_osm_wiki_and_data_items'].append(issue)
            if issue["type"] == "wikidata key present":
                reports_for_display['wikidata_key_present'].append(issue)

    return reports_for_display

def count_appearances_from_wiki_page_title(osm_wiki_page_title):
    key, value = tag_from_wiki_title(osm_wiki_page_title)
    if value != None:
        return taginfo.query.count_appearances_of_tag(key, value)
    else:
        return taginfo.query.count_appearances_of_key(key)

def tag_from_wiki_title(osm_wiki_page_title):
    title = osm_wiki_page_title.replace(" ", "_")
    if title.find("Tag:") == 0:
        cleaned = title.replace("Tag:", "")
        key, value = cleaned.split("=")
        return key, value
    elif title.find("Key:") == 0:
        key = title.replace("Key:", "")
        return key, None
    else:
        raise "unhandled"

def collect_reports():
    site = pywikibot.Site('en', 'osm')
    processed = 0
    reports_for_display = {
        'missing_images_template_ready_for_adding': [],
        'missing_status_template_ready_for_adding': [],
        'mismatches_between_osm_wiki_and_data_items': [],
        'wikidata_key_present': [],
    }
    pages = pages_grouped_by_tag()
    keys = list(pages.keys())
    random.shuffle(keys)
    for index in keys:
        group = pages[index]
        try:
            reports_for_display = update_reports(reports_for_display, group)
        except KeyError:
            print("failure while processing", index)
            raise
        processed += 1
        if processed % 1000 == 0:
            print("processed", processed, "out of", len(keys))
        if len(reports_for_display['missing_images_template_ready_for_adding']) > 10:
            if len(reports_for_display['missing_status_template_ready_for_adding']) > 10:
                if len(reports_for_display['mismatches_between_osm_wiki_and_data_items']) >= 1:
                    if len(reports_for_display['data_not_copied_to_data_items']) >= 1:
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
    print("=== Organised overview of major issues ===")
    print("==== Tags with quickly growing usage but without own page ====")
    print(missing_pages)
    display_reports(reports_for_display, mediawiki_url_formatter)

def display_reports(reports_for_display, url_formatter):
    # dump due to bug
    #print(reports_for_display)
    #pprint.pp(reports_for_display)
    # dump due to bug

    report = ""

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
        report += "====Missing status====\n"
        report += "missing status parameter in the infobox, adding it would be useful\n"
        report += "see https://wiki.openstreetmap.org/wiki/Template:Tag_status_values for documentation of meaning of values and their list\n"
        for issue in report_segment:
            try:
                report += "* " + url_formatter(issue["osm_wiki_url"]) + "\n"
            except KeyError:
                print(issue)
                raise
    report_segment = reports_for_display['mismatches_between_osm_wiki_and_data_items']
    if len(report_segment) > 0:
        report += "\n"
        report += "====Important mismatch of OSM Wiki and data items====\n"
        report += "Important mismatches between [[data item]]s and OSM Wiki that are worth spending time on fixing them (minor ones are skipped, see [[:Category:Data item issues]] if you want all of them):\n"
        for issue in report_segment:
            try:
                line = ""
                line += "* "
                line += url_formatter(issue["osm_wiki_url"]) + " "
                if issue["data_item_url"] == None:
                    line += "-missing data item-"
                else:
                    line += url_formatter(issue["data_item_url"]) + " "
                line += issue["key"]
                line += "( <code>" + issue['osm_wiki_value']
                line += "</code> vs <code>" + issue['data_item_value'] + "</code> )" 
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
    report_segment = reports_for_display['data_not_copied_to_data_items']
    if len(report_segment) > 0:
        report += "\n"
        report += "====Data not copied to data items====\n"
        report += "data can be copied from OSM Wiki to data items ([https://wiki.openstreetmap.org/wiki/Special:ItemByTitle?site=wiki you can use this page to create missing data items]):\n"
        for issue in report_segment:
            try:
                line = ""
                line += "* "
                line += url_formatter(issue["osm_wiki_url"]) + " "
                if issue["data_item_url"] == None:
                    line += "-misising data item-"
                else:
                    line += url_formatter(issue["data_item_url"]) + " "
                line += issue["key"]
                line += "( wiki has <code>" 
                line += issue['osm_wiki_value'] 
                line += "</code>)" 
                line += "\n"
                report += line
            except KeyError:
                print(issue)
                print("data_not_copied_to_data_items have incomplete data")
                raise
            except TypeError:
                print(issue)
                print("type handling bug")
                raise
    print(report)

main()
