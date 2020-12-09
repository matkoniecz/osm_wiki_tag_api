# Taginfo code (Ruby)

https://github.com/taginfo/taginfo/blob/master/sources/wiki/lib/mediawikiapi.rb

https://github.com/taginfo/taginfo/blob/master/sources/wiki/get_wiki_data.rb

```
require_relative 'mediawikiapi.rb'

api = MediaWikiAPI::API.new('/w/index.php?')
title = "Tag:highway=motorway"
returned = api.get({ :title => title, :action => 'raw' }).body
puts(returned)
```