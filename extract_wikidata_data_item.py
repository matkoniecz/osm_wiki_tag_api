# Copyright (C) 2020  Mateusz Konieczny <matkoniecz@gmail.com>
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License 3 as published by FSF

import urllib
import urllib.request
import json

def json_response_from_api(entity_id):
    url = "https://www.wikidata.org/wiki/Special:EntityData/" + entity_id + ".json"
    url = url.replace(" ", "%20")
    data = urllib.request.urlopen(url).read()
    return json.loads(data)

print(json_response_from_api("Q42"))