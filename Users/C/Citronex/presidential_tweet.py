import scraperwiki

## GramercyOne

import scraperwiki
import simplejson
import urllib2

# Change QUERY to your search term of choice.


QUERY = 'GramercyOne'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10

QUERY = 'gramercyone'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10

QUERY = 'GoBook'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10

QUERY = 'SpaBooker'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10

QUERY = 'Spa-Booker'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10

for page in range(1, NUM_PAGES+1):
    base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        for result in results_json['results']:
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            data['created_at'] = result['created_at']
            print data['from_user'], data['text'],data['from_user'],data['created_at']
            scraperwiki.sqlite.save(["id"], data)
    except:
        print 'Oh dear, failed to scrape %s' % base_url

# Blank Python
import scraperwiki

## GramercyOne

import scraperwiki
import simplejson
import urllib2

# Change QUERY to your search term of choice.


QUERY = 'GramercyOne'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10

QUERY = 'gramercyone'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10

QUERY = 'GoBook'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10

QUERY = 'SpaBooker'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10

QUERY = 'Spa-Booker'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10

for page in range(1, NUM_PAGES+1):
    base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        for result in results_json['results']:
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            data['created_at'] = result['created_at']
            print data['from_user'], data['text'],data['from_user'],data['created_at']
            scraperwiki.sqlite.save(["id"], data)
    except:
        print 'Oh dear, failed to scrape %s' % base_url

# Blank Python
