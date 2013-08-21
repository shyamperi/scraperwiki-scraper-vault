import scraperwiki
import simplejson
import urllib2

QUERY = 'meetup'
RESULTS_PER_PAGE = '100'
NUM_PAGES = 10

for page in range(1, NUM_PAGES+1):
    base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&page=%s' \
         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, page)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        for result in results_json['results']:
            #print result
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            data['location'] = scraperwiki.geo.extract_gb_postcode(result['text'])
            data['from_user'] = result['from_user']
            data['created_at'] = result['created_at']
            if data['location']:
                print data['location'], data['from_user']
                scraperwiki.sqlite.save(["id"], data)
    except:
        print 'Oh dear, failed to scrape %s' % base_url
        break
