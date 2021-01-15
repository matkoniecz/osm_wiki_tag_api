import taginfo
import extract_infobox_data
import links
import extract_data_item
import extract_wikidata_data_item
import extract_wikibase_item

import time
import random
import pywikibot

#tag
#tag description ?
#specified linked wikidata page
#linked wikidata page description

def get_wikidata_description(wikidata_id):
    if wikidata_id[0] == "P":
        return "Unexpected linking of property, not of item"
    wikidata_url = 'https://www.wikidata.org/wiki/' + wikidata
    p = extract_wikidata_data_item.json_response_from_api(wikidata)
    entity = extract_wikibase_item.extract_entity_from_parsed_json(p)
    description = extract_wikibase_item.extract_description(entity)
    label = extract_wikibase_item.extract_label(entity)
    if description == None:
        description = ""
    if label == None:
        label = ""
    return label + " - " + description

"ab".removeprefix("a") # quick check that we are running python 3.9+
site = pywikibot.Site('en', 'osm')
values = pywikibot.Page(site, "Template:ValueDescription").getReferences(namespaces=[0], content=True)
keys = pywikibot.Page(site, "Template:KeyDescription").getReferences(namespaces=[0], content=True)
values = list(values)
keys = list(keys)
remaining_wanted_examples = 400
remaining_total_count = len(keys) + len(values)

table = """
sample of randomly selected enties with linked wikidata items

{| class="wikitable"
|+ Caption text
|-
! tag !! linked wikidata item !! description of linked item
"""

for page in (values + keys):
    title = page.title().replace(" ", "_")
    if title.find("Tag:") == 0 or title.find("Key:") == 0:
        if remaining_wanted_examples > random.randrange(remaining_total_count):
            template = extract_infobox_data.page_data(page.title())

            tag_link = None
            if title.find("Tag:") == 0:
                cleaned = title.replace("Tag:", "")
                key, value = cleaned.split("=")
                tag_link = "{{Tag|" + key + "|" + value + "}}"
            elif title.find("Key:") == 0:
                key = title.replace("Key:", "")
                tag_link = "{{Tag|" + key + "}}"
            
            wikidata = None
            if "wikidata" in template:
                if template["wikidata"].strip() != "":
                    wikidata = template["wikidata"].strip()
            if wikidata == None:
                data_item = extract_data_item.page_data(page.title())
                if "wikidata" in data_item:
                    wikidata = data_item["wikidata"]
            if wikidata != None:
                wikidata_url = 'https://www.wikidata.org/wiki/' + wikidata
                description = get_wikidata_description(wikidata)
                print(tag_link)
                print(wikidata_url)
                print(description)
                print()
                table += "|-\n"
                table += "| " + tag_link + " || " + wikidata_url + " || " + description + "\n"
                remaining_wanted_examples -= 1
    remaining_total_count -= 1

table += """
|}
"""
print(table)