require_relative 'mediawikiapi.rb'

api = MediaWikiAPI::API.new('/w/index.php?')
title = "Tag:highway=motorway"
returned = api.get({ :title => title, :action => 'raw' }).body
puts(returned)