def osm_wiki_page_name_from_link(url):
    url = url.removeprefix("https://wiki.openstreetmap.org/wiki/")
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
