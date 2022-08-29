import csv
import re

with open('infobox_data.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        status = row[3]
        status = re.sub('<!--.*-->', '', status)
        if status.strip().lower() not in ["", "approved", "in use", "de facto", "imported", "import", "discardable", "deprecated", "proposed", "rejected", "abandoned", "draft", "obsolete"]:
            print("*", row[0], row[0]+"?action=edit", status)
