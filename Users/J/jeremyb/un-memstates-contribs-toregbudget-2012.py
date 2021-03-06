#Scraper for Burundi microfinance data from pdf file. Based on Scraperwiki's PDF example.
# Position visualizer is here: http://scraperwikiviews.com/run/pdf-to-html-preview-1/

import scraperwiki
import os
import tempfile
import sys
import re
import pprint

lineparser = re.compile(r'^(?:\s{0,2}(?P<rownum>\d{0,5}))(?:$|\s(?P<name>.{77}.*?)(?:$|\s{5,}(?P<type>.{17}.*?)\s(?P<address>.*)))\s*$')
multispacere = re.compile(r'\s{3,}')

def pdftotext(pdfdata):
    """converts pdf file to text"""
    pdffout = tempfile.NamedTemporaryFile(suffix='.pdf')
    pdffout.write(pdfdata)
    pdffout.flush()

    textin = tempfile.NamedTemporaryFile(mode='r', suffix='.html')
    tmptext = textin.name
    cmd = '/usr/bin/pdftotext -layout -enc UTF-8 "%s" "%s"' % (pdffout.name, tmptext)
    cmd = cmd + " >/dev/null 2>&1" # can't turn off output, so throw away even stderr yeuch
    os.system(cmd)

    pdffout.close()
    text = textin.read()
    textin.close()
    return text

#Code nicked from ScraperWiki's pdttotext example
#Creates text version of the table with its columns separated  by tabs.

pdfurl = "http://www.tuxmachine.com/.N1165367.pdf"
a = scraperwiki.scrape(pdfurl)
rawtext = pdftotext(a)
print rawtext
print repr(rawtext)

#Convert table to array.  Aargh! This is wrong and messy at the moment! 
lastLine = None
out = []
headers = {}
namebuffer = None

print pprint.pprint([multispacere.split(line.strip()) for line in rawtext.splitlines()])

sys.exit()

for line in rawtext.splitlines():
    
    if not line.strip():
        continue
    lv = dict((k,v.strip()) for k,v in lineparser.search('%-200s' % line.rstrip()).groupdict().items())
    #print(repr(dict((k,v.strip()) for k,v in lineparser.search('%-200s' % line.rstrip()).groupdict().items())))
    print repr(lv)

    if not headers:
        if "adresse" in lv['address'].lower():
             headers = lv
        continue

    if lv['rownum']:
        if lastLine:
            out.append(lastLine)
            print repr(lastLine)
        lastLine = lv
    else:
        for k in lastLine.keys():
            lastLine[k] = ' '.join((lastLine[k],lv[k]))
        
    #data = args2dict(lv)
    #print repr(data)

out.append(lastLine)
print repr(lastLine)

print repr(out)
#Dump data out to scrtaperwiki store
scraperwiki.sqlite.save(unique_keys=['rownum'], data=out)
#Scraper for Burundi microfinance data from pdf file. Based on Scraperwiki's PDF example.
# Position visualizer is here: http://scraperwikiviews.com/run/pdf-to-html-preview-1/

import scraperwiki
import os
import tempfile
import sys
import re
import pprint

lineparser = re.compile(r'^(?:\s{0,2}(?P<rownum>\d{0,5}))(?:$|\s(?P<name>.{77}.*?)(?:$|\s{5,}(?P<type>.{17}.*?)\s(?P<address>.*)))\s*$')
multispacere = re.compile(r'\s{3,}')

def pdftotext(pdfdata):
    """converts pdf file to text"""
    pdffout = tempfile.NamedTemporaryFile(suffix='.pdf')
    pdffout.write(pdfdata)
    pdffout.flush()

    textin = tempfile.NamedTemporaryFile(mode='r', suffix='.html')
    tmptext = textin.name
    cmd = '/usr/bin/pdftotext -layout -enc UTF-8 "%s" "%s"' % (pdffout.name, tmptext)
    cmd = cmd + " >/dev/null 2>&1" # can't turn off output, so throw away even stderr yeuch
    os.system(cmd)

    pdffout.close()
    text = textin.read()
    textin.close()
    return text

#Code nicked from ScraperWiki's pdttotext example
#Creates text version of the table with its columns separated  by tabs.

pdfurl = "http://www.tuxmachine.com/.N1165367.pdf"
a = scraperwiki.scrape(pdfurl)
rawtext = pdftotext(a)
print rawtext
print repr(rawtext)

#Convert table to array.  Aargh! This is wrong and messy at the moment! 
lastLine = None
out = []
headers = {}
namebuffer = None

print pprint.pprint([multispacere.split(line.strip()) for line in rawtext.splitlines()])

sys.exit()

for line in rawtext.splitlines():
    
    if not line.strip():
        continue
    lv = dict((k,v.strip()) for k,v in lineparser.search('%-200s' % line.rstrip()).groupdict().items())
    #print(repr(dict((k,v.strip()) for k,v in lineparser.search('%-200s' % line.rstrip()).groupdict().items())))
    print repr(lv)

    if not headers:
        if "adresse" in lv['address'].lower():
             headers = lv
        continue

    if lv['rownum']:
        if lastLine:
            out.append(lastLine)
            print repr(lastLine)
        lastLine = lv
    else:
        for k in lastLine.keys():
            lastLine[k] = ' '.join((lastLine[k],lv[k]))
        
    #data = args2dict(lv)
    #print repr(data)

out.append(lastLine)
print repr(lastLine)

print repr(out)
#Dump data out to scrtaperwiki store
scraperwiki.sqlite.save(unique_keys=['rownum'], data=out)
