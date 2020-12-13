# Copyright (C) 2020  Mateusz Konieczny <matkoniecz@gmail.com>
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License 3 as published by FSF

import urllib
import json

def page_data(page_title):
    parsed = json_response_from_api(page_title)
    return turn_api_response_to_parsed(parsed)

def pretty_response_text(page_title):
    parsed = json_response_from_api(page_title)
    return json.dumps(parsed, indent = 4)

def tag_data(key, value=None):
    if value == None:
        return page_data("Key:" + key)
    else:
        return page_data("Tag:" + key + "=" + value)

# this is a hacky workaround

# pywikibot failed: https://phabricator.wikimedia.org/T269635
# maybe https://github.com/SuLab/WikidataIntegrator would work (see https://github.com/SuLab/WikidataIntegrator/issues/164 )

def extract_unqualified_statement(entity, claim_id):
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

def status_for_geometry(entity, claim_id):
    statement = extract_unqualified_statement(entity, claim_id)
    if statement == None:
        return None
    magic_status_code_object = statement["datavalue"]["value"]
    if "numeric-id" in magic_status_code_object:
        magic_status_code = magic_status_code_object["numeric-id"]
        if magic_status_code == 8001:
            return "no"
        if magic_status_code == 8000:
            return "yes"
        print(magic_status_code)
        print("invalid status code for geometry")
    else:
        print(json.dumps(entity, indent = 4))
        print(magic_status_code_object)
        raise "invalid magic object"

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

def extract_magic_code(entity, claim_id):
    if "claims" not in entity:
        return None
    if claim_id not in entity["claims"]:
        return None
    statement = extract_unqualified_statement(entity, claim_id)
    if statement == None:
        return None
    if "datavalue" not in statement:
        print(json.dumps(parsed_json, indent = 4))
        raise "missing data value"
    datavalue = statement["datavalue"]
    magic_status_code_object = datavalue["value"]
    if "numeric-id" in magic_status_code_object:
        return magic_status_code_object["numeric-id"]
    else:
        print(json.dumps(parsed_json, indent = 4))
        print(json.dumps(magic_status_code_object, indent = 4))
        raise "missing status code"

def extract_usage_status_string(entity):
    claim_id = "P6"
    magic_status_code = extract_magic_code(entity, claim_id)
    if magic_status_code == None:
        return None

    # active
    if magic_status_code == 13:
        return "de facto"
    elif magic_status_code == 14:
        return "in use"
    elif magic_status_code == 15:
        return "approved"

    # active, but not fully
    elif magic_status_code == 5061:
        return "deprecated"
    elif magic_status_code == 5060:
        return "obsolete"
    elif magic_status_code == 21146:
        return "imported"
    elif magic_status_code == 18:
        return "draft"
    elif magic_status_code == 20:
        return "proposed"
    elif magic_status_code == 19:
        return "abandoned"
    elif magic_status_code == 7550:
        return "discardable"
    else:
        print(json.dumps(entity, indent = 4))
        print(magic_status_code)
        raise "unexpected status code"

def turn_api_response_to_parsed(parsed_json):
    returned_ids = list(parsed_json['entities'].keys())
    if len(returned_ids) != 1:
        print(json.dumps(parsed_json, indent = 4))
        raise "unexpected"
    item_id = returned_ids[0]
    entity = parsed_json['entities'][item_id]

    returned = {}
    value = extract_string(entity, "P28")
    if value != None:
        returned["image"] = value
    language_code = "en"
    if "descriptions" in entity:
        if language_code in entity["descriptions"]:
            returned["description"] = entity["descriptions"][language_code]["value"]
    status_string = extract_usage_status_string(entity)
    if status_string != None:
        returned["status"] = status_string

    status = status_for_geometry(entity, "P33")
    if status != None:
        returned["onNode"] = status 

    status = status_for_geometry(entity, "P34")
    if status != None:
        returned["onWay"] = status 

    status = status_for_geometry(entity, "P35")
    if status != None:
        returned["onArea"] = status 

    status = status_for_geometry(entity, "P36")
    if status != None:
        returned["onRelation"] = status 

    if "P46" in entity["claims"]:
        returned["combination"] = "??????" # TODO, process this horrific mess

    if "P45" in entity["claims"]:
        returned["implies"] = "??????" # TODO, process this horrific mess

    if "P18" in entity["claims"]: # Note that P18 is "different from", not "see also" - but it is used in this way
        returned["seeAlso"] = "??????" # TODO, process this horrific mess

    if "P22" in entity["claims"]:
        returned["requires"] = "??????" # TODO, process this horrific mess

    if "P25" in entity["claims"]:
        returned["group"] = "??????" # TODO, process this horrific mess

    if "P11" in entity["claims"]:
        returned["statuslink"] = extract_url(entity, 'P11')
    

    value = extract_string(entity, "P12")
    if value != None:
        returned["wikidata"] = value
    return returned

def json_response_from_api(page_title):
    url = "https://wiki.openstreetmap.org/w/api.php?action=wbgetentities&sites=wiki&titles=" + page_title + "&languages=en|fr&format=json"
    url = url.replace(" ", "%20")
    data = urllib.request.urlopen(url).read()
    return json.loads(data)


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
    """
    NOT WORKING
    probably due to https://phabricator.wikimedia.org/T269635

    def get_data_item_from_page(site, page):
        data_item_id = get_data_item_id_from_page(page)
        repo = site.data_repository()
        return pywikibot.ItemPage(repo, data_item_id)

    page = pywikibot.Page(pywikibot.Site(), "Tag:building=yes")
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
