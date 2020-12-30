# Copyright (C) 2020  Mateusz Konieczny <matkoniecz@gmail.com>
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License 3 as published by FSF

import urllib
import urllib.request
import json

# this is a hacky workaround

# pywikibot failed: https://phabricator.wikimedia.org/T269635
# maybe https://github.com/SuLab/WikidataIntegrator would work (see https://github.com/SuLab/WikidataIntegrator/issues/164 )
# see https://github.com/osmlab/atlas-checks/blob/0296d4d0544e801a198a186462487f2014c8fac5/scripts/wikidata/get_wikidata.py
# for a very similar parsing to this one, but different
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
page = pywikibot.Page(pywikibot.Site('en', 'osm'), "Key:amenity")
item = pywikibot.ItemPage.fromPage(page)
"""

"""
works but requires known id
repo = site.data_repository()
item = pywikibot.ItemPage(repo, "Q4980")
print(item)
"""
"""
NOT WORKING
probably due to https://phabricator.wikimedia.org/T269635

def get_data_item_from_page(site, page):
    data_item_id = get_data_item_id_from_page(page)
    repo = site.data_repository()
    return pywikibot.ItemPage(repo, data_item_id)

page = pywikibot.Page(pywikibot.Site('en', 'osm'), "Tag:building=yes")
data_item = get_data_item_from_page(site, page)
print(data_item)
data_item.get()  # you need to call it to access any data.
sitelinks = data_item.sitelinks
aliases = data_item.aliases
if 'en' in data_item.labels:
    print('The label in English is: ' + data_item.labels['en'])
if item.claims:
    for claim in data_item.claims: # instance of
        print(claim)
        print(data_item.claims[claim][0].getTarget())
"""

def extract_description(entity, language_code = "en"):
    if "descriptions" in entity:
        if language_code in entity["descriptions"]:
            return entity["descriptions"][language_code]["value"]
    return None

def extract_entity_from_parsed_json(parsed_json):
    returned_ids = list(parsed_json['entities'].keys())
    if len(returned_ids) != 1:
        print(json.dumps(parsed_json, indent = 4))
        raise "unexpected"
    item_id = returned_ids[0]
    entity = parsed_json['entities'][item_id]
    return entity

def turn_api_response_to_parsed(parsed_json):
    entity = extract_entity_from_parsed_json(parsed_json)

    returned = {}
    value = extract_string(entity, "P28")
    if value != None:
        returned["image"] = value
    
    description = extract_description(entity)

def extract_string(entity, claim_id):
    if "claims" not in entity:
        return None
    if claim_id not in entity["claims"]:
        return None
    statement = extract_unqualified_statement(entity, claim_id)
    if statement == None:
        return None
    return statement["datavalue"]["value"]

def extract_url(entity, claim_id):
    # maybe implementing whatever type matches should be done...
    return extract_string(entity, claim_id)

def extract_unqualified_statement(entity, claim_id):
    if "claims" not in entity:
        return None
    if claim_id not in entity["claims"]:
        return None
    statements = entity["claims"][claim_id]
    for statement in statements:
        if "qualifiers" in statement:
            continue
        # returns first value if there are multiple ones
        # see case of image for
        # https://wiki.openstreetmap.org/wiki/Item:Q4990
        return statement["mainsnak"]
    return None
