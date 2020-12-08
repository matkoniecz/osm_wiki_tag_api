import pywikibot
import mwparserfromhell
import urllib
import json

# https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Install_Pywikibot
# I followed it, run script, and recopied it here
# https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script

def get_data_item_id_from_page(page):
    """
    following fails:

    repo = site.data_repository()
    item = pywikibot.ItemPage(repo, "highway=motorway")
    print(item)

    repo = site.data_repository()
    item = pywikibot.ItemPage(repo, "Tag:highway=motorway")
    # fails with 'Tag:highway=motorway' is not a valid item page title
    print(item)

    # https://phabricator.wikimedia.org/T269635
    item = pywikibot.ItemPage(site, "Key:amenity")
    page = pywikibot.Page(pywikibot.Site(), "Key:amenity")
    item = pywikibot.ItemPage.fromPage(page)
    """

    """
    works but requires known id
    repo = site.data_repository()
    item = pywikibot.ItemPage(repo, "Q4980")
    print(item)
    """

    url = "https://wiki.openstreetmap.org/w/api.php?action=wbgetentities&sites=wiki&titles=" + page.title() + "&languages=en|fr&format=json"
    data = urllib.request.urlopen(url).read()
    print(data)
    parsed = json.loads(data)
    print(json.dumps(parsed, indent = 4))
    returned_ids = list(parsed['entities'].keys())
    if len(returned_ids) != 1:
        raise "unexpected"
    else:
        return returned_ids[0]
    raise "unexpected"

def get_data_item_from_page(site, page):
    data_item_id = get_data_item_id_from_page(page)
    repo = site.data_repository()
    return pywikibot.ItemPage(repo, data_item_id)

site = pywikibot.Site()
page = pywikibot.Page(pywikibot.Site(), "Key:bridge:movable")
print(get_data_item_from_page(site, page))

# https://wiki.openstreetmap.org/w/api.php?action=wbgetentities&sites=wiki&titles=Key:bridge:movable&languages=en|fr&format=json

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
        print(page)
        print(page.title())
        print(type(page).__name__)
        item = pywikibot.ItemPage(site, page.title())
        item = pywikibot.ItemPage.fromPage(page)
        print(item)



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