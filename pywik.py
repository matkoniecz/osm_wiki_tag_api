import pywikibot
import data_item_extractor
import template_extractor

# https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Install_Pywikibot
# I followed it, run script, and recopied it here
# https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script


def compare_data(page_name):
    url = "https://wiki.openstreetmap.org/wiki/" + page_name
    url = url.replace(" ", "%20")
    data_item = data_item_extractor.page_data(page_name)
    template = template_extractor.page_data(page_name)
    if template == {}:
        return # for example, on pages where Template:Deprecated calls it internally
    for key in set(set(data_item.keys()) | set(template.keys())):
        in_data_item = data_item.get(key)
        normalized_in_data_item = in_data_item
        in_template = template.get(key)
        normalized_in_template = in_template
        if in_template == None:
            if in_data_item != None:
                print(url, "-", key, "is from data item (", in_data_item, ")")
        if in_template != None:
            if key == "image":
                normalized_in_template = normalized_in_template.removeprefix("Image:")
                normalized_in_template = normalized_in_template.removeprefix("File:")
                normalized_in_template = normalized_in_template.replace("_", " ")
                continue
            if key == "status":
                normalized_in_template = normalized_in_template.lower()
            if key == "description":
                if normalized_in_template[-1] == ".":
                    normalized_in_template = normalized_in_template[:-1]
                if normalized_in_data_item[-1] == ".":
                    normalized_in_data_item = normalized_in_data_item[:-1]
            if in_data_item != None:
                if normalized_in_template != normalized_in_data_item:
                    if "?" not in in_data_item:
                        print(url, "-", key, "are mismatched between data item and OSM Wiki (", in_template, "vs", in_data_item, ")")



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