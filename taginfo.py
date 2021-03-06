import urllib
import urllib.request
import urllib.parse
import json

def count_appearances_of_tag(key, value):
    url = "https://taginfo.openstreetmap.org/api/4/tag/stats?key=" + urllib.parse.quote(key) + "&value=" + urllib.parse.quote(value)
    data = json_response_from_url(url)
    return data['data'][0]['count']

def count_appearances_of_key(key):
    url = "https://taginfo.openstreetmap.org/api/4/key/stats?key=" + urllib.parse.quote(key)
    data = json_response_from_url(url)
    return data['data'][0]['count']

def count_appearances_from_wiki_page_title(osm_wiki_page_title):
    title = osm_wiki_page_title.replace(" ", "_")
    if title.find("Tag:") == 0:
        cleaned = title.replace("Tag:", "")
        key, value = cleaned.split("=")
        return count_appearances_of_tag(key, value)
    elif title.find("Key:") == 0:
        key = title.replace("Key:", "")
        return count_appearances_of_key(key)
    else:
        raise "unhandled"

def get_all_data_about_key_use(key):
    url = "https://taginfo.openstreetmap.org/api/4/key/chronology?key=" + urllib.parse.quote(key)
    data = json_response_from_url(url)
    return data['data']

def get_all_data_about_tag_use(key, value):
    url = "https://taginfo.openstreetmap.org/api/4/tag/chronology?key=" + urllib.parse.quote(key) + "&value=" + urllib.parse.quote(value)
    data = json_response_from_url(url)
    return data['data']

def count_new_appearances_of_tag_historic_data_from_deltas(data, days_ago):
    if data == []:
        return None
    diff = 0
    for offset in range(1, days_ago):
        if len(data) >= offset:
            diff += data[-offset]["nodes"]
            diff += data[-offset]["ways"]
            diff += data[-offset]["relations"]
    return diff

def count_new_appearances_of_tag_historic_data(key, value, days_ago):
    data = get_all_data_about_tag_use(key, value)
    return count_new_appearances_of_tag_historic_data_from_deltas(data, days_ago)

def count_new_appearances_of_key_historic_data(key, days_ago):
    data = get_all_data_about_key_use(key)
    return count_new_appearances_of_tag_historic_data_from_deltas(data, days_ago)

def get_all_values_of_key(key):
    page = 1
    while True:
        data = get_page_of_key_values(key, page)
        for entry in data:
            yield entry
        page += 1
        if len(data) < entries_per_page():
            break

def entries_per_page():
    return 999

def get_page_of_key_values(key, page):
    url = "https://taginfo.openstreetmap.org/api/4/key/values?key=" + urllib.parse.quote(key) + "&page=" + str(page) + "&rp=" + str(entries_per_page()) + "&sortname=count_all&sortorder=desc"
    return json_response_from_url(url)["data"]

def json_response_from_url(url):
    url = url.replace(" ", "%20")
    try:
        data = urllib.request.urlopen(url).read()
        return json.loads(data)
    except UnicodeEncodeError:
        print("failed to process", url)
        raise
