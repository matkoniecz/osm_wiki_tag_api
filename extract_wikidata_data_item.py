# Copyright (C) 2020  Mateusz Konieczny <matkoniecz@gmail.com>
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License 3 as published by FSF

import urllib
import urllib.request
import json

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

def json_response_from_api(entity_id):
    url = "https://www.wikidata.org/wiki/Special:EntityData/" + entity_id + ".json"
    url = url.replace(" ", "%20")
    data = urllib.request.urlopen(url).read()
    return json.loads(data)

p = json_response_from_api("Q42")
entity = extract_entity_from_parsed_json(p)
print(extract_description(entity))