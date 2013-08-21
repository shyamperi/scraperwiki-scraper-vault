import scraperwiki
import mechanize
import re
import urlparse
import lxml.html


# ASPX pages are some of the hardest challenges because they use javascript and forms to navigate
# Almost always the links go through the function function __doPostBack(eventTarget, eventArgument)
# which you have to simulate in the mechanize form handling library

# This example shows how to follow the Next page link

url3 = 'http://baytvliverpool.com/'
br3 = mechanize.Browser()

    # sometimes the server is sensitive to this information
br3.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response3 = br3.open(url3)


html3 = response3.read()
re.DOTALL
videoimgs = re.findall('<img src="vod/thumbs/(.*?)/>', html3)
videolinks = re.findall('<a href="vod/index.php(.*?)"', html3)
print videoimgs
print videolinks

videos = videoimgs, videolinks
allvideos = [[row[i] for row in videos] for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 25, 26, 27, 28, 29]]



scraperwiki.sqlite.execute("delete from swdata") 

record = {}
for allvideo in allvideos:
    if videoimgs:
        record['img'] = allvideo[0]
        record['link'] = allvideo[1]
        
        # Print out the data we've gathered
        print record, '------------'
        # Finally, save the record to the datastore - 'Artist' is our unique key
        scraperwiki.sqlite.save(["img"], record)