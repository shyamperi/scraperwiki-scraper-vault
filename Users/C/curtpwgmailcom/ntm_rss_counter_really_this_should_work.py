import scraperwiki
import lxml.etree
import lxml.html
import urllib

def getRoot(url):
    root = lxml.html.parse(url).getroot()
    return root

def getRSSitems(url):

    tree = lxml.etree.parse(urllib.urlopen(url[0]))
    items = tree.xpath("//item")

    newspaper = url[1]
    print newspaper

    rssArticles = []

    for item in items:
        article = {}

        article["title"] = item.xpath("./title")[0].text.strip()
        article["link"] = item.xpath("./link")[0].text.strip()
   #     article["author"] = item.xpath("./author")[0].text.strip()
        article["pubDate"] = item.xpath("./pubDate")[0].text.strip()

        # Hämta artikel ID från länken
  #      article["articleId"] = int(article["link"].split("=")[1])

        # Alla har inte beskrivningar så vi kollar här
        description = item.xpath("./description")
        if(len(description) > 0):
            article["description"] = description[0].text.strip()

        # Spara datan
        scraperwiki.sqlite.save(["articleId"], article, table_name=newspaper, verbose=2)           

        rssArticles.append(article)

    return rssArticles

rssURLs = [("http://www.jobgymn.com/makefulltextfeed.php?url=rss.indeed.com%2Frss%3Fq%3Daa&max=10&links=preserve&exc=&submit=Create+Feed","PT"),
("http://2007.kuriren.nu/allt.rss","NK"),
("http://www.nsd.se/allt.rss","NSD")]

for rssURL in rssURLs:
    print "Getting data from",rssURL
    getRSSitems(rssURL)
