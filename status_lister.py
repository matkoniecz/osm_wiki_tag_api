import csv
import re
# see also https://wiki.openstreetmap.org/wiki/Category:Feature_descriptions_with_incorrect_status_value
with open('infobox_data.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        status = row[3]
        status = re.sub('<!--.*-->', '', status)
        if status.strip().lower() not in ["", "approved", "in use", "de facto", "imported", "discardable", "deprecated", "proposed", "rejected", "abandoned", "draft", "obsolete"]:
            print("*", row[0], row[0]+"?action=edit", status)
