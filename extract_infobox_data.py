import mwparserfromhell
import pywikibot
import links

def page_data(page_title):
    page = pywikibot.Page(pywikibot.Site('en', 'osm'), page_title)
    try:
        return turn_page_text_to_parsed(page.text, page_title)
    except ValueError:
        return None

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

def turn_page_text_to_parsed(text, page_title):
    wikicode = mwparserfromhell.parse(text)
    templates = wikicode.filter_templates()
    returned = {}
    template_found_already = False
    expected_keys = ["image", "description", "status", "statuslink", "onNode", "onWay", "onArea", "onRelation",
                     "requires", "implies", "combination", "seeAlso", "wikidata", "group"]
    also_expected_but_ignored_keys = [
                                      # TODO: check whatever following are appearing in data items, start tracking
                                      # without requirement of having them present
                                      'osmcarto-rendering', 'osmcarto-rendering-size',
                                      'osmcarto-rendering-node', 'osmcarto-rendering-node-size',
                                      'osmcarto-rendering-way', 'osmcarto-rendering-way-size',
                                      'osmcarto-rendering-area', 'osmcarto-rendering-area-size',
                                      'website',
                                      'nativekey', # not copied into data items
                                      'onChangeset', # not used but makes sense
                                      'image_caption', # popular, eliminate with bot, not worth manual removal (some may be valid! make list?)
                                      'onClosedWay', # popular on network pages - leave removal for bot edit
                                      'url_pattern', # pointless, maybe I will also eleiminate it some day
                                      ]
    for template in templates:
        #print(template.name)
        #print(template.params)
        if template.name.strip() in ["ValueDescription", "KeyDescription"]:
            if template_found_already:
                print("MULTIPLE MATCHING TEMPLATES")
                raise ValueError("Multiple matching templates")
            template_found_already = True
            for fetched in expected_keys:
                if template.has(fetched):
                    returned[fetched] = template.get(fetched).value.strip()
            for param in template.params:
                if param != '' and "=" in param:
                    key = param.split("=")[0].strip()
                    if key == "key":
                        continue # TODO check match
                    if key == "value" and template.name.strip() == "ValueDescription":
                        continue # TODO check match
                    if key not in expected_keys and key not in also_expected_but_ignored_keys:
                        print(": Unexplained weird parameter (" + key + ") in", template.name.strip(), "on", links.osm_wiki_page_link(page_title))
                        raise ValueError("Unexplained weird unhandled <" + key + "> parameter")
                elif param == "":
                    print(": Unexplained empty parameter in", template.name.strip(), "on", links.osm_wiki_page_link(page_title))
                    raise ValueError("Empty parameter")
                else:
                    print(": Unexplained weird parameters in", template.name.strip(), "on", links.osm_wiki_page_link(page_title))
                    print(":", param)
                    print(":", template.params)
                    raise ValueError("Unexplained weird parameter")


    return returned
