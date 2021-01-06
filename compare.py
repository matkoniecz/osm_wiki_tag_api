import pywikibot
import extract_data_item
import extract_infobox_data
import re

# https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Install_Pywikibot
# I followed it, run script, and recopied it here
# https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script

# TODO: detect incomplete skeleton (distinguish missing parameter and no parameter set)

def unimportant_tag_status():
    return ["obsolete", "abandoned", "deprecated", "proposed", "draft"]

def is_adding_image_important(page_name, template_data):
    if "status" in template_data:
        if template_data["status"] in unimportant_tag_status():
            # TODO: detect marked as proposed with significant use
            return False
    if "Tag:landmark=" in page_name or "seamark" in page_name or "source" in page_name:
        return False
    if is_page_skipped_for_now_from_missing_parameters(page_name, template_data):
        return False
    return True

def is_page_skipped_for_now_from_missing_parameters(page_name, template):
    if "Tag:seamark" in page_name or "Tag:pilotage" in page_name or "Tag:landmark" in page_name or "Tag:type=" in page_name: # skip seamark mess, at least for now
        return True
    if page_name in ["Tag:seamark:conspicuity=conspicuous", "Tag:waterway=deep well"]:
        return True
    if "status" in template:
        if template["status"] in unimportant_tag_status():
            # TODO: detect marked as obsolete/abandoned with some real use (>100?)
            return True
    return False

def is_page_skipped_for_now_from_missing_description(page_name, template):
    if "Tag:crop=" or "Tag:wood=" in page_name: # give up with this group 
        return True
    if "Tag:mooring=" in page_name: # give up with this group 
        return True
    if status in unimportant_tag_status():
        return True # TODO - maybe consider as low importance?

def is_key_reportable_as_completely_missing_in_template(key, page_name, template):
    if is_page_skipped_for_now_from_missing_parameters(page_name, template):
        return False
    if key not in template.keys():
        return True
    return False

def is_key_reportable_as_missing_in_template(key, page_name, template):
    if is_page_skipped_for_now_from_missing_parameters(page_name, template):
        return False
    if key in template.keys() and template[key].strip() != "":
        # it is not missing
        return False
    if key == "image":
        if is_adding_image_important(page_name, template) == False:
            return False
        return False # drop for now
    if key == "description":
        if is_page_skipped_for_now_from_missing_description(page_name, template):
            return False
    return True

def compare_data(page_name):
    url = "https://wiki.openstreetmap.org/wiki/" + page_name
    url = url.replace(" ", "_")
    data_item = extract_data_item.page_data(page_name)
    template = extract_infobox_data.page_data(page_name)
    written_something = False
    if template == {}:
        return # for example, on pages where Template:Deprecated calls it internally
    mandatory = ["onNode", "onWay", "onArea", "onRelation", "image", "description", "status"]
    report = {"issues": []}
    for key in mandatory:
        if key in data_item.keys():
            # it is in data item, warning about copying will appear
            continue
        if is_key_reportable_as_completely_missing_in_template(key, page_name, template):
            report["issues"].append({"type": "missing_key_in_infobox", "key": key})
        elif is_key_reportable_as_missing_in_template(key, page_name, template):
            report["issues"].append({"type": "missing_value_in_infobox_with_key_present", "key": key})
    for issue in report["issues"]:
        if issue["type"] == "missing_key_in_infobox":
            print(":", url, issue["key"], "is missing and not present even as empty parameter")
            written_something = True
        if issue["type"] == "missing_value_in_infobox_with_key_present":
            print(":", url, issue["key"], "value is missing in the infobox template")
            written_something = True
    for key in set(set(data_item.keys()) | set(template.keys())):
        if key in ["data_item_id"]:
            continue
        in_data_item = data_item.get(key)
        normalized_in_data_item = in_data_item
        in_template = template.get(key)
        normalized_in_template = in_template

        if key == "seeAlso" or key == "combination":
            # implement parsing that in future to make copying easier
            continue

        if normalized_in_template != None:
            # for comparison skip comments in template
            normalized_in_template = re.sub('<!--.*-->', '', normalized_in_template)

        if normalized_in_template != None:
            normalized_in_template = normalized_in_template.strip()
            if normalized_in_template == "":
                normalized_in_template = None

        if key == "wikidata":
            continue # big time sing, it would be smarter to work on removal it from infoboxes
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

        if key == "image":
            if normalized_in_template != None:
                normalized_in_template = normalized_in_template.removeprefix("Image:")
                normalized_in_template = normalized_in_template.removeprefix("File:")
                normalized_in_template = normalized_in_template.replace("_", " ")

        if key == "status":
            if normalized_in_template != None:
                normalized_in_template = normalized_in_template.lower()

            if normalized_in_template == "defacto":
                # do not bother, at least for now, with this
                normalized_in_template = "de facto"

            if normalized_in_template == "import":
                # do not bother, at least for now, with this
                normalized_in_template = "imported"

            if normalized_in_template == "inuse":
                # do not bother, at least for now, with this
                normalized_in_template = "in use"

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
"ab".removeprefix("a") # quick check that we are running python 3.9+

site = pywikibot.Site('en', 'osm')
compare_data("Tag:amenity=trolley_bay")
compare_data("Tag:cemetery=sector")
skip_until = "Tag:amenity=rescue_station" # None
processed = 0
reported_something = False
for infobox in ["Template:ValueDescription", "Template:KeyDescription"]:
    root_page = pywikibot.Page(site, infobox)
    for page in root_page.getReferences(namespaces=[0], content=True):
        if skip_until != None:
            if page.title() == skip_until.replace("_", " "):
                skip_until = None
            else:
                #print("skipped", page.title())
                continue
        if page.title().find("Tag:") == 0 or page.title().find("Key:") == 0: #No translated pages as data items are borked there
            if compare_data(page.title()) == True:
                if reported_something == False:
                    print("processed", processed, "before showing anything")
                reported_something = True
        processed += 1
        if processed % 1000 == 0:
            print("processed", processed)

"""
# list namespaces
for n in site.namespaces:
    print(n)
    print(site.namespaces[n])
    print(site.namespaces[n].canonical_prefix())
    print(site.namespaces[n].normalize_name(site.namespaces[n].canonical_prefix()))
    print(type(site.namespaces[n]))

# all pages in main namespace
for page in site.allpages(namespace = [0]):
    print(page)
    print(page.title())
"""