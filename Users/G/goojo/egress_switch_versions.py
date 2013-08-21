import scraperwiki

import lxml.html           
import re
import datetime

html = scraperwiki.scrape("http://switch.egress.com")
root = lxml.html.fromstring(html)
print "Hello"
#<meta name="generator" content="Switch 3.0.96.0 (c) Egress Software technologies" />

for meta in root.cssselect('meta'):
    name = meta.get('name')
    content = meta.get('content')
    if name=="generator":
        print 
        data = {"version": content.split("(c)")[0],
                "date": datetime.datetime.now()
        }
        scraperwiki.sqlite.save(unique_keys=['version'], data=data)


