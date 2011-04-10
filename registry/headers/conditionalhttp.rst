conditionalhttp
#author Wari Wahab
#email pyblosxom at wari dot per dot sg
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Allows for caching if-not-modified-since....
#license MIT
#registrytags 1.4, 1.5, core
#generator update_registry

This plugin can help save bandwidth for low bandwidth quota sites (how
unfortunate).

This is done by outputing cache friendly HTTP header tags like Last-Modified
and ETag. These values are calculated from the first entry returned by
entry_list.
