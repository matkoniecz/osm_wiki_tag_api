import mwparserfromhell
import pywikibot
import links

def page_data(page_title):
    page = pywikibot.Page(pywikibot.Site('en', 'osm'), page_title)
    url = links.osm_wiki_page_link(page_title)
    if "DISPLAYTITLE" in page.text:
        print(url, "has unneded DISPLAYTITLE template")
    return turn_page_text_to_parsed(page.text)

def tag_data(key, value=None):
    if value == None:
        return page_data("Key:" + key)
    else:
        return page_data("Tag:" + key + "=" + value)

"""
parsing engines that were considered

(1)
mwparserfromhell - first tried, worked very well

(2)
pywikibot's harvest_template.py

(3)
https://github.com/5j9/wikitextparser

(4)
MediaWiki API - https://en.wikipedia.org/wiki/Special:ApiSandbox#action=parse&format=json&text=%7B%7B1x%7Carg%7D%7D&prop=parsetree&contentmodel=wikitext&formatversion=2
not sure is it actually a parser, not tested usefullness

(5)
https://www.mediawiki.org/wiki/Parsoid - PHP, old version in JS
"""

def turn_page_text_to_parsed(text):
    wikicode = mwparserfromhell.parse(text)
    templates = wikicode.filter_templates()
    returned = {}
    for template in templates:
        #print(template.name)
        #print(template.params)
        if template.name.strip() in ["ValueDescription", "KeyDescription"]:
            for fetched in ["image", "description", "status", "statuslink",
                            "onNode", "onWay", "onArea", "onRelation",
                            "requires", "implies", "combination", "seeAlso",
                            "wikidata", "group"]:
                if template.has(fetched):
                    returned[fetched] = template.get(fetched).value.strip()
    return returned
