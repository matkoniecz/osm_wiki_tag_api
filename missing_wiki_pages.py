import taginfo
import links
import time

def list_of_new_popular_values_for_key(key, multiplier, offset):
    new_popular_values = []
    values = taginfo.get_all_values_of_key(key)
    for entry in values:
        value = entry["value"]
        description = entry["description"]
        if description == "" or description == None:
            delta = taginfo.count_new_appearances_of_tag_historic_data(key, value, offset)
            if delta == None:
                return new_popular_values # dropped into lower use
            if delta > 1000 * multiplier: # growing
                new_popular_values.append({"key": key, "value": value, "delta": delta, "delta_offset_in_days": offset})
    return new_popular_values


def new_popular_report_text(new_popular_values):
    returned = ""
    for entry in new_popular_values:
        identifier = entry["key"] + "=" + entry["value"]
        if identifier not in blacklisted_tags_that_do_not_need_pages():
            returned += identifier + " (increase by " + str(entry["delta"]) + " in last " + str(entry["delta_offset_in_days"]) + " days):"
            returned += "\n"
            returned += links.osm_wiki_page_link_from_tag(entry["key"], entry["value"])
            returned += "\n"
            returned += "\n"
    return returned

def new_popular_report_wikicode_text(new_popular_values):
    returned = ""
    for entry in new_popular_values:
        identifier = entry["key"] + "=" + entry["value"]
        if identifier not in blacklisted_tags_that_do_not_need_pages():
            returned += "|-\n"
            returned += "| {{tag|" + entry["key"] + "|" + entry["value"] + "}} || " + str(entry["delta"]) + "\n"
            returned += "\n"
    return returned

def blacklisted_tags_that_do_not_need_pages():
    return ["bridge=yes", "tunnel=yes", "man_made=tar_kiln",
        "highway=removed:street_lamp", # https://www.openstreetmap.org/note/2535136
        ]

def keys_where_values_should_be_documented():
    returned = []
    for entry in keys_where_values_should_be_documented_with_weights():
        returned.append(entry['key'])
    return returned

def keys_where_values_should_be_documented_with_weights():
    return [
    # scaling - higher means that higher usage is required to appear on the list
    {'key': "attraction", 'scaling': 1},
    {'key': "water", 'scaling': 1},
    {'key': "healthcare", 'scaling': 1},
    {'key': "building", 'scaling': 8},
    {'key': "amenity", 'scaling': 1},
    {'key': "man_made", 'scaling': 4},
    {'key': "highway", 'scaling': 1},
    {'key': "natural", 'scaling': 0.5},
    {'key': "landuse", 'scaling': 1},
    {'key': "shop", 'scaling': 0},
    {'key': "historic", 'scaling': 4},
    {'key': "power", 'scaling': 1},
    {'key': "leisure", 'scaling': 1},
    {'key': "waterway", 'scaling': 1},
    {'key': "barrier", 'scaling': 0.5},
    {'key': "place", 'scaling': 0.1},
    {'key': "tourism", 'scaling': 0.5},
    {'key': "surface", 'scaling': 1},
    {'key': "wall", 'scaling': 1},
    {'key': "footway", 'scaling': 1},
    {'key': "tunnel", 'scaling': 1},
    {'key': "bridge", 'scaling': 1},
    {'key': "service", 'scaling': 1},
    {'key': "railway", 'scaling': 1},
    {'key': "public_transport", 'scaling': 1},
    {'key': "access", 'scaling': 0.4},
    {'key': "bicycle", 'scaling': 1},
    {'key': "foot", 'scaling': 1},
    {'key': "vehicle", 'scaling': 3},
    {'key': "motor_vehicle", 'scaling': 10},
    {'key': "mofa", 'scaling': 10},
    #'key': "denomination", 'scaling': 2},
    {'key': "location", 'scaling': 2},
    {'key': "entrance", 'scaling': 0.2},
    {'key': "usage", 'scaling': 2},
    {'key': "segregated", 'scaling': 1},
    ]

def undocumented_values_among_popular_tags_reports():
    data = []
    offset_in_days = 100
    for entry in keys_where_values_should_be_documented_with_weights():
        data += list_of_new_popular_values_for_key(entry['key'], entry['scaling'], offset=offset_in_days)
    
    if len(data) == 0:
        raise "reduce base value in new_popular"
    returned = ""
    returned += new_popular_report_text(data)
    returned += "\n\n\n"
    returned += "{| class=\"wikitable sortable\"\n"
    returned += "|-\n"
    returned += "! Tag !! Increase in past " + str(offset_in_days) + " days\n"
    returned += new_popular_report_wikicode_text(data)
    returned += "|}"
    return returned
