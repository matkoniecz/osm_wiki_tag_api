# Copyright (C) 2020  Mateusz Konieczny <matkoniecz@gmail.com>
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License 3 as published by FSF

import template_extractor
text = """
{{ValueDescription
|key=building
|value=yes
|image=File:Parque Avenida Building in Paulista Avenue.jpg
|description=General tag for building.
|onNode=yes
|onWay=no
|onArea=yes
|onRelation=no
|status=de facto
}}
Building of an unspecific type, used when someone is unable to tag it more specifically. It can be also used when someone wants to record presence of a building, without tagging further detail.

Replacing by more specific building type is always welcomed (if more specific value is correct). [[StreetComplete]] is one of tools that can be used for that.
"""

print(template_extractor.turn_page_text_to_parsed(text))