import pywikibot
import data_item_extractor
import extract_infobox_data

# https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Install_Pywikibot
# I followed it, run script, and recopied it here
# https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script


def compare_data(page_name):
    url = "https://wiki.openstreetmap.org/wiki/" + page_name
    url = url.replace(" ", "_")
    data_item = data_item_extractor.page_data(page_name)
    template = extract_infobox_data.page_data(page_name)
    if template == {}:
        return # for example, on pages where Template:Deprecated calls it internally
    for key in set(set(data_item.keys()) | set(template.keys())):
        in_data_item = data_item.get(key)
        normalized_in_data_item = in_data_item
        in_template = template.get(key)
        normalized_in_template = in_template

        if key == "wikidata":
            if normalized_in_template == None and normalized_in_data_item != None:
                normalized_in_template = valid_wikidata(page_name)

        if normalized_in_template == None:
            if key == "group":
                continue # do not report leaks here (for now - TODO!)
            if in_data_item != None:
                print(":", url, "-", key, "is from data item (", in_data_item, ")")
            if key == "wikidata":
                    print(': https://www.wikidata.org/wiki/' + in_data_item)
                    print("<pre>")
                    print('        "' + page_name.replace(" ", "_") + '": "' + in_data_item + '",')
                    print("</pre>")
        if in_template != None and in_data_item != None:
            if key == "image":
                normalized_in_template = normalized_in_template.removeprefix("Image:")
                normalized_in_template = normalized_in_template.removeprefix("File:")
                normalized_in_template = normalized_in_template.replace("_", " ")
                continue # do not report mismatches here
            if key == "status":
                normalized_in_template = normalized_in_template.lower()
            if key == "description":
                normalized_in_template = normalize_description(normalized_in_template)
                normalized_in_data_item = normalize_description(normalized_in_data_item)
                if normalized_in_template != normalized_in_data_item:
                    print(":", url, "-", key, "are mismatched between OSM Wiki and data item")
                    print("::", in_template)
                    print("::", in_data_item)
                continue # do not report mismatches here
            if normalized_in_template != normalized_in_data_item:
                if "?" not in in_data_item:
                    print(":", url, "-", key, "are mismatched between OSM Wiki and data item (", in_template, "vs", in_data_item, ")")

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
        "Tag:man made=pipeline": "Q16885408",
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
        "Tag:information=board": "Q76419950",
    }
    return wikidata.get(page_name)


site = pywikibot.Site()

for infobox in ["Template:ValueDescription", "Template:KeyDescription"]:
    root_page = pywikibot.Page(pywikibot.Site(), infobox)
    for page in root_page.getReferences(namespaces=[0], content=True):
        if page.title().find("Tag:") == 0 or page.title().find("Key:") == 0: #No translated pages as data items are borked there
            compare_data(page.title())

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