def osm_wiki_page_link(page_name):
    url = "https://wiki.openstreetmap.org/wiki/" + page_name
    url = url.replace(" ", "_")
    return url
