import scraperwiki
import lxml.html 

html = scraperwiki.scrape("http://unstats.un.org/unsd/demographic/products/socind/education.htm")

print html


root = lxml.html.fromstring(html) 

for tr in root.cssselect("div[align='left'] tr.tcont"): 
    tds = tr.cssselect("td") 
    record = { 
        'country' : tds[0].text_content(),
        'years_in_school' : int(tds[4].text_content()) 
    }
    print tds[0].text_content()
    print record
    scraperwiki.sqlite.save(unique_keys=['country'], data=record)
