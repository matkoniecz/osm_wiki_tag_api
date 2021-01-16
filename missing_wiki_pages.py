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

def undocumented_values_among_popular_tags():
    returned = ""
    returned += new_popular("attraction")
    returned += new_popular("water")
    returned += new_popular("healthcare")
    returned += new_popular("building", 8)
    returned += new_popular("amenity")
    returned += new_popular("man_made", 4)
    returned += new_popular("highway")
    returned += new_popular("natural", 0.5)
    returned += new_popular("landuse")
    returned += new_popular("shop", 0)
    returned += new_popular("historic", 4)
    returned += new_popular("power")
    returned += new_popular("leisure")
    returned += new_popular("waterway")
    returned += new_popular("barrier", 0.5)
    returned += new_popular("place", 0.1)
    returned += new_popular("tourism", 0.5)
    returned += new_popular("wall")
    returned += new_popular("footway")
    returned += new_popular("tunnel")
    returned += new_popular("bridge")
    returned += new_popular("service")
    returned += new_popular("railway")
    returned += new_popular("public_transport")
    returned += new_popular("access", 0.4)
    #returned += new_popular("denomination") - https://wiki.openstreetmap.org/wiki/Key:denomination is not even linking to most of them
    if returned == "":
        raise "reduce base value in new_popular"
    return returned

def missing_pages():
    return undocumented_values_among_popular_tags()
