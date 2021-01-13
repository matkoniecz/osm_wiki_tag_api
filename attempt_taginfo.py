import taginfo
import links
import time

def show_new_popular(key, multiplier=1):
    values = taginfo.get_all_values_of_key(key)
    for entry in values:
        value = entry["value"]
        description = entry["description"]
        if description == "" or description == None:
            offset=100
            delta = taginfo.count_new_appearances_of_tag_historic_data(key, value, offset)
            if delta == None:
                return # dropped into low use
            if delta > 1000 * multiplier: # growing
                print(key + "=" + value, "(increase by " + str(delta) + " in last " + str(offset) + " days):")
                print(links.osm_wiki_page_link_from_tag(key, value))
                print()

show_new_popular("attraction")
show_new_popular("water")
show_new_popular("tunnel")
show_new_popular("public_transport")
show_new_popular("healthcare")
show_new_popular("building", 8)
show_new_popular("amenity")
show_new_popular("man_made", 4)
show_new_popular("highway")
show_new_popular("natural", 0.5)
show_new_popular("landuse")
show_new_popular("shop", 0)
show_new_popular("historic", 4)
show_new_popular("power")
show_new_popular("leisure")
show_new_popular("waterway")
show_new_popular("barrier", 0.5)
show_new_popular("place", 0.1)
show_new_popular("tourism", 0.5)
show_new_popular("wall")
show_new_popular("footway")
show_new_popular("bridge")
show_new_popular("service")
show_new_popular("railway")
show_new_popular("access", 0.1)
show_new_popular("bridge")
time.sleep(10101010101010101010110100101)
print(taginfo.count_appearances_of_key("building"))
print(taginfo.count_appearances_of_tag("landuse", "yes"))
print(taginfo.get_all_data_about_key_use("shop"))
