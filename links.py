def osm_wiki_page_name_from_link(url):
    prefix = "https://wiki.openstreetmap.org/wiki/"
    if url.find(prefix) != 0:
        return None
    url = url.removeprefix(prefix)
    return url

def osm_data_item_code_from_link(url):
    prefix = "https://wiki.openstreetmap.org/wiki/Item:"
    if url.find(prefix) != 0:
        return None
    url = url.removeprefix(prefix)
    return url

def osm_data_entity_code_from_link(url):
    # may be item, property, etc
    prefix = "https://wiki.openstreetmap.org/wiki/"
    if url.find(prefix) != 0:
        return None
    url = url.removeprefix(prefix)
    return url

def osm_wiki_page_link(page_name):
    url = "https://wiki.openstreetmap.org/wiki/" + page_name
    url = url.replace(" ", "_")
    return url

def osm_wiki_page_link_from_tag(key, value):
    url = "https://wiki.openstreetmap.org/wiki/Tag:" + key + "=" + value
    url = url.replace(" ", "_")
    return url

def osm_wiki_page_link_from_key(key):
    url = "https://wiki.openstreetmap.org/wiki/Key:" + key
    url = url.replace(" ", "_")
    return url
