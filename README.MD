This repository contains

- [code](extract_infobox_data.py) to obtain relevant parameters from infobox of OSM Wiki tag page (OSM Wiki is a Mediawiki wiki, so standard tools such as `pywikibot` and `mwparserfromhell` were used)
    - this code is fairly trivial, but may be useful for others as finding correct tool for job was not trivial
- [code](data_item.py) to obtain statements from data item (from Wikibase setup)
    - this code is fairly trivial and is parsing in a weird way (as workaround for [bug](https://phabricator.wikimedia.org/T269635) that hopefully is now fixed as you read this), but finding even this way was not so easy so maybe it will be useful for someone
- [code](compare.py) comparing info in data items and in infoboxes, listing mismatches and cases where infobox is not using its parameters but is silently displaying info from data item
    - mismatches often indicate that something is wrong, and use of data item instead of infobox parameters is unwanted. Especially in cases where someone deleted parameter from infobox ecause it was wrong but incorrect data from data item still haunts us.

# Limitations

If you need anything of things listed below - feel free to make a pull request!

Ideally, open an issue first if you want to add something not listed below.

* Full parsing of data items is missing.

* Missing support for non-English descriptions

* Missing documentation and proper tests

# Dependencies

Python 3.9+

`pip3 install -r requirements.txt`

#Alternatives
## Taginfo code (Ruby)

This can be used as an alternative way of getting parsed infoboxes if you need a Ruby code.

https://github.com/taginfo/taginfo/blob/master/sources/wiki/lib/mediawikiapi.rb

https://github.com/taginfo/taginfo/blob/master/sources/wiki/get_wiki_data.rb

```
require_relative 'mediawikiapi.rb'

api = MediaWikiAPI::API.new('/w/index.php?')
title = "Tag:highway=motorway"
returned = api.get({ :title => title, :action => 'raw' }).body
puts(returned)
```