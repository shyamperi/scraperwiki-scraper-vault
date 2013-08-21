# -*- coding: UTF-8 -*-

import scraperwiki
import json
from BeautifulSoup import BeautifulSoup
import datetime
import dateutil.parser
import lxml.html
import resource
import sys
import urllib2
import urlparse
import re
lazycache=scraperwiki.swimport('lazycache')
postlistelib=scraperwiki.swimport('postliste-python-lib')

agency = 'Saltdal kommune'

def report_errors(errors):
    if 0 < len(errors):
        print "Errors:"
        laste  = None
        for e in errors:
            print e
            laste = e
        raise e

def out_of_cpu(arg, spent, hard, soft):
    report_errors(arg)

def process_pdf(parser, pdfurl, errors):
    errors = []
    postlistelib.exit_if_no_cpu_left(0, out_of_cpu, errors)
    try:
        pdfcontent = scraperwiki.scrape(pdfurl)
        parser.preprocess(pdfurl, pdfcontent)
        pdfcontent = None
#    except ValueError, e:
#        errors.append(e)
    except IndexError, e:
        errors.append(e)
    except ValueError, e:
        errors.append(e)
    except urllib2.HTTPError, e:
        errors.append(e)

def process_page_queue(parser, errors):
    try:
        parser.process_pages()
        postlistelib.exit_if_no_cpu_left(0, out_of_cpu, errors)
    except scraperwiki.CPUTimeExceededError, e:
        errors.append(e)

def process_journal_pdfs(parser, listurl, errors):
#    print "Finding PDFs on " + listurl
#    u = urllib.parse.urlparse(listurl)
    html = scraperwiki.scrape(listurl)
    root = lxml.html.fromstring(html)
    html = None
    for ahref in root.cssselect("table a"):
        href = ahref.attrib['href']
        url = urlparse.urljoin(listurl, href)
        if -1 != href.find("file://") or -1 == url.find(".pdf"):
#            print "Skipping non-http URL " + url
            continue
        if parser.is_already_scraped(url):
            True
#            print "Skipping already scraped " + url
        else:
#            print "Will process " + url
            process_pdf(parser, url, errors)

def test_small_pdfs(parser):
    # Test with some smaller PDFs
    errors = []
    #parser.debug = True
    newurl = "http://www.saltdal.kommune.no/images/module.files/010612.pdf"
    if not parser.is_already_scraped(newurl):
        process_pdf(parser, newurl, errors) # New format
    if parser.is_already_scraped(newurl):
        print "Already parsed"
    else:
        raise ValueError("Failed to parse")
#    process_pdf(parser, "http://www.saltdal.kommune.no/images/module.files/2007-01-31.pdf", errors) # Old format
    process_page_queue(parser, errors)
    report_errors(errors)
    exit(0)

errors = []
parser = postlistelib.PDFJournalParser(agency=agency)
#parser.debug = True

#test_small_pdfs(parser)

process_journal_pdfs(parser, "http://www.saltdal.kommune.no/postlister.html", errors)
process_page_queue(parser, errors)
report_errors(errors)

