import scraperwiki
import requests
import lxml.html
html = requests.get('www.last.fm/charts/tracks/top/place/Korea%2C+Republic+of?ending=1364731200').text
root = lxml.html.fromstring(html)
for optgroup in root.cssselect("#weekpicker-weeks optgroup"):
    year = optgroup.get("label")
    if year == "2013":
        for option in optgroup.cssselect("option"):
            unixtime = option.get("value")
            html2 = requests.get('http://www.last.fm/charts/tracks/top/place/Korea%2C+Republic+of?ending=' + unixtime).text
            root2 = lxml.html.fromstring(html2)
            for box in root2.cssselect("li.rankItem"):
                print unixtime, box.cssselect("span.rankItem-title")[0].text_content(),box.cssselect("span.rankItem-position")[0].text_content(), box.cssselect("span.rankItem-bar-percentage")[0].text_content()
                data = {
                    'DATE' : unixtime,
                    'POSITION' : box.cssselect("span.rankItem-position")[0].text_content(),
                    'TRACK' : box.cssselect("span.rankItem-title")[0].text_content(),
                    'LISTEN' : box.cssselect("span.rankItem-bar-percentage")[0].text_content(),
                        }
                scraperwiki.sqlite.save(unique_keys=['DATE','TRACK', 'LISTEN'], data=data)
                    

                