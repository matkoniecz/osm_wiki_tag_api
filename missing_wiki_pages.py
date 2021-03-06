import taginfo
import links
import time

def new_popular(key, multiplier=1):
    returned = ""
    values = taginfo.get_all_values_of_key(key)
    for entry in values:
        value = entry["value"]
        description = entry["description"]
        if description == "" or description == None:
            offset = 100
            delta = taginfo.count_new_appearances_of_tag_historic_data(key, value, offset)
            if delta == None:
                return returned # dropped into lower use
            if delta > 1000 * multiplier: # growing
                identifier = key + "=" + value
                if identifier not in ["bridge=yes", "tunnel=yes"]:
                    returned += key + "=" + value + " (increase by " + str(delta) + " in last " + str(offset) + " days):"
                    returned += "\n"
                    returned += links.osm_wiki_page_link_from_tag(key, value)
                    returned += "\n"
                    returned += "\n"
    return returned

def keys_where_values_should_be_documented():
    returned = []
    for entry in keys_where_values_should_be_documented_with_weights():
        returned.append(entry['key'])
    return returned

def keys_where_values_should_be_documented_with_weights():
    return [
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
    {'key': "wall", 'scaling': 1},
    {'key': "footway", 'scaling': 1},
    {'key': "tunnel", 'scaling': 1},
    {'key': "bridge", 'scaling': 1},
    {'key': "service", 'scaling': 1},
    {'key': "railway", 'scaling': 1},
    {'key': "public_transport", 'scaling': 1},
    {'key': "access", 'scaling': 0.4},
    {'key': "denomination", 'scaling': 2},
    ]

def undocumented_values_among_popular_tags():
    returned = ""
    for entry in keys_where_values_should_be_documented_with_weights():
        returned += new_popular(entry['key'], entry['scaling'])
    if returned == "":
        raise "reduce base value in new_popular"
    return returned

def missing_pages():
    return undocumented_values_among_popular_tags()
