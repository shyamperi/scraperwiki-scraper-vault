###################################################################################
# Twitter API scraper - designed to be forked and used for more interesting things
###################################################################################

import scraperwiki
import simplejson
import urllib2

# Get results from the Twitter API! Change QUERY to your search term of choice. 
# Examples: 'newsnight', 'from:bbcnewsnight', 'to:bbcnewsnight' 166866601
QUERY = 'from:sbahnberlin'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 5 

for page in range(1, NUM_PAGES+1):
    base_url = 'http://api.twitter.com/1/statuses/user_timeline.json?screen_name=sbahnberlin'
##'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
##         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        print results_json
        for result in results_json:
           data = {}
           data['id'] = result['id']
           data['text'] = result['text']
           data['created_at'] = result['created_at']
           scraperwiki.sqlite.save(["id"], data) 
    except:
        print 'Oh dear, failed to scrape %s' % base_url
        
    ###################################################################################
# Twitter API scraper - designed to be forked and used for more interesting things
###################################################################################

import scraperwiki
import simplejson
import urllib2

# Get results from the Twitter API! Change QUERY to your search term of choice. 
# Examples: 'newsnight', 'from:bbcnewsnight', 'to:bbcnewsnight' 166866601
QUERY = 'from:sbahnberlin'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 5 

for page in range(1, NUM_PAGES+1):
    base_url = 'http://api.twitter.com/1/statuses/user_timeline.json?screen_name=sbahnberlin'
##'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
##         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        print results_json
        for result in results_json:
           data = {}
           data['id'] = result['id']
           data['text'] = result['text']
           data['created_at'] = result['created_at']
           scraperwiki.sqlite.save(["id"], data) 
    except:
        print 'Oh dear, failed to scrape %s' % base_url
        
    ###################################################################################
# Twitter API scraper - designed to be forked and used for more interesting things
###################################################################################

import scraperwiki
import simplejson
import urllib2

# Get results from the Twitter API! Change QUERY to your search term of choice. 
# Examples: 'newsnight', 'from:bbcnewsnight', 'to:bbcnewsnight' 166866601
QUERY = 'from:sbahnberlin'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 5 

for page in range(1, NUM_PAGES+1):
    base_url = 'http://api.twitter.com/1/statuses/user_timeline.json?screen_name=sbahnberlin'
##'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
##         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        print results_json
        for result in results_json:
           data = {}
           data['id'] = result['id']
           data['text'] = result['text']
           data['created_at'] = result['created_at']
           scraperwiki.sqlite.save(["id"], data) 
    except:
        print 'Oh dear, failed to scrape %s' % base_url
        
    