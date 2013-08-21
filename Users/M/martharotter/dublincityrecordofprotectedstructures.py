import scraperwiki
import urllib
import lxml.etree, lxml.html
import re

pdfurl = "http://www.dublincity.ie/Planning/HeritageConservation/Conservation/Documents/VOLUME%203.pdf"


# (harder example to work on: http://www.nihe.gov.uk/schemes_accepted_010109_to_310309.pdf )
pdfdata = urllib.urlopen(pdfurl).read()
pdfxml = scraperwiki.pdftoxml(pdfdata)
root = lxml.etree.fromstring(pdfxml)
print pdfxml

fontspecs = { }
pagetexts = [ ]
for page in root:
    assert page.tag == 'page'
    print "page details", page.attrib
    pagelines = { }
    for v in page:
        if v.tag == 'fontspec':
            fontspecs[v.attrib.get('id')] = v
        else:
            assert v.tag == 'text'
            text = re.match('(?s)<text.*?>(.*?)</text>', lxml.etree.tostring(v)).group(1)   # there has to be a better way here to get the contents
            top = int(v.attrib.get('top'))
            if top not in pagelines:
                pagelines[top] = [ ]
            pagelines[top].append((int(v.attrib.get('left')), text))
    lpagelines = pagelines.items()
    lpagelines.sort()
    for top, line in lpagelines[:20]:
        record = {}
        line.sort()
#        print top, line
        record['ProtectedStructure'] = line
    pagetexts.append(pagelines)
    scraperwiki.datastore.save(["ProtectedStructure"], record)
    
    
