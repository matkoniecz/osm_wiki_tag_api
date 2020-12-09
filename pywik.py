import pywikibot
import data_item_extractor
import template_extractor

# https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Install_Pywikibot
# I followed it, run script, and recopied it here
# https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script


def compare_data(page_name):
    data_item = data_item_extractor.page_data(page_name)
    template = template_extractor.page_data(page_name)
    for key in set(set(data_item.keys()) | set(template.keys())):
        in_data_item = data_item.get(key)
        in_template = template.get(key)
        if in_template == None:
            if in_data_item != None:
                print("https://wiki.openstreetmap.org/wiki/" + page_name, "-", key, "is from data item")


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
    for page in root_page.getReferences(namespaces=[0], content=True): #namespaces=self.opt.namespaces
        print(data_item_extractor.page_data(page.title()))
        print(template_extractor.page_data(page.title()))


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