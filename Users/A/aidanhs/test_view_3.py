import scraperwiki

scraperwiki.utils.httpresponseheader("Content-Type", "application/rss+xml")

print """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
<title>RSS Example</title>
<description>This is an example of an RSS feed</description>
<link>http://www.example.com/link.htm</link>
<lastBuildDate>Mon, 28 Aug 2006 11:12:55 -0400 </lastBuildDate>
<pubDate>Tue, 29 Aug 2006 09:00:00 -0400</pubDate>

<item>
<title>Item Example</title>
<description>This is an example of an Item</description>
<link>http://www.example.com/link.htm</link>
<guid isPermaLink="false"> 1102345</guid>
<pubDate>Tue, 29 Aug 2006 09:00:00 -0400</pubDate>
</item>

</channel>
</rss>"""

