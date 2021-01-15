# Copyright (C) 2020  Mateusz Konieczny <matkoniecz@gmail.com>
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License 3 as published by FSF

import extract_wikibase_item
import urllib
import urllib.request
import json

def json_response_from_api(entity_id):
    if entity_id.strip() == "":
        raise
    if entity_id.strip() == None:
        raise
    if entity_id[0] != "Q":
        raise
    url = "https://www.wikidata.org/wiki/Special:EntityData/" + entity_id + ".json"
    url = url.replace(" ", "%20")
    data = urllib.request.urlopen(url).read()
    return json.loads(data)
