import pywikibot
import data_item_extractor
import template_extractor

# https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Install_Pywikibot
# I followed it, run script, and recopied it here
# https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script


def compare_data(page_name):
    url = "https://wiki.openstreetmap.org/wiki/" + page_name
    url = url.replace(" ", "_")
    data_item = data_item_extractor.page_data(page_name)
    template = template_extractor.page_data(page_name)
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

        if in_template == None:
            if key == "group":
                continue # do not report leaks here (for now - TODO!)
            if in_data_item != None:
                print(url, "-", key, "is from data item (", in_data_item, ")")
            if key == "wikidata":
                    print('https://www.wikidata.org/wiki/' + in_data_item)
                    print('        "' + page_name + '": "' + in_data_item.replace(" ", "_") + '",')
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
                    print(url, "-", key, "are mismatched between OSM Wiki and data item")
                    print(in_template)
                    print(in_data_item)
                continue # do not report mismatches here
            if normalized_in_template != normalized_in_data_item:
                if "?" not in in_data_item:
                    print(url, "-", key, "are mismatched between OSM Wiki and data item (", in_template, "vs", in_data_item, ")")

def normalize_description(description):
    if description == None:
        return description
    if description == "":
        return description
    if description[-1] != ".":
        return description
    return description[:-1]

def valid_wikidata(page_name):
    # why not added? Because I consider adding them as mistake
    # why listed here? To detect invalid ones
    page_name = page_name.replace(" ", "_")
    wikidata = {
        "Tag:aerialway=chair_lift": "Q850767",
        "Tag:barrier=toll_booth": "Q1364150",
        "Tag:man_made=survey_point": "Q352956",
        "Tag:natural=wood": "Q4421",
        "Tag:highway=motorway_junction": "Q353070",
        "Tag:amenity=cafe": "Q30022",
    }
    return wikidata.get(page_name)


site = pywikibot.Site()
#print(template_extractor.tag_data("highway", "motorway"))
#print(data_item_extractor.tag_data("highway", "motorway"))

compare_data("Key:highway")
compare_data("Tag:building=yes")


"""
print(site.namespaces)
for n in site.namespaces:
    print(n)
    print(site.namespaces[n])
    print(site.namespaces[n].canonical_prefix())
    print(site.namespaces[n].normalize_name(site.namespaces[n].canonical_prefix()))
    print(type(site.namespaces[n]))
"""

"""
# all pages in main namespace
for page in site.allpages(namespace = [0]):
    print(page)
    print(page.title())
"""

for infobox in ["Template:ValueDescription", "Template:KeyDescription"]:
    root_page = pywikibot.Page(pywikibot.Site(), infobox)
    for page in root_page.getReferences(namespaces=[0], content=True):
        if page.title().find("Tag:") == 0 or page.title().find("Key:") == 0: #No translated pages as data items are borked there
            compare_data(page.title())
            #print(data_item_extractor.page_data(page.title()))
            #print(template_extractor.page_data(page.title()))


"""
print("aaaaa")
for namespace in site.namespaces:
    print(namespace)

site = pywikibot.Site()
for namespace in site.namespaces:
    print(namespace)
    for page in site.allpages(namespace = namespace):
        print(page)
        #// process page.title() and page.editTime()

page = pywikibot.Page(site, "Key:highway")
text = page.text
print(text)
wikicode = mwparserfromhell.parse(text)
templates = wikicode.filter_templates()
"""