#This is the second pass at a scraper of Excel files. 
#Currently it scrapes all sheets of one spreadsheet, identified by one direct xls URL
#NEED TO ADD: 
#More than one spreadsheet, linked from one webpage URL = 'http://transparency.dh.gov.uk/2012/10/26/winter-pressures-daily-situation-reports-2012-13/'

#useful guides at:
#https://scraperwiki.com/docs/python/python_excel_guide/
#http://blog.scraperwiki.com/2011/09/14/scraping-guides-excel-spreadsheets/
#https://scraperwiki.com/docs/python/tutorials/

import scraperwiki
#import xlrd library - documentation at https://secure.simplistix.co.uk/svn/xlrd/trunk/xlrd/doc/xlrd.html
import xlrd
import lxml.html

import datetime

def cellval(cell, datemode):
    if cell.ctype == xlrd.XL_CELL_DATE:
        datetuple = xlrd.xldate_as_tuple(cell.value, datemode)
        if datetuple[3:] == (0, 0, 0):
            return datetime.date(datetuple[0], datetuple[1], datetuple[2])
        return datetime.date(datetuple[0], datetuple[1], datetuple[2], datetuple[3], datetuple[4], datetuple[5])
    if cell.ctype == xlrd.XL_CELL_EMPTY:    return None
    if cell.ctype == xlrd.XL_CELL_BOOLEAN:  return cell.value == 1
    return cell.value

URL = 'http://transparency.dh.gov.uk/2012/10/26/winter-pressures-daily-situation-reports-2012-13/'
#set a variable for the spreadsheet location
XLS = 'https://www.wp.dh.gov.uk/transparency/files/2012/10/DailySR-Pub-file-WE-11-11-123.xls'
#use the scrape function on that spreadsheet to create a new variable

def scrapespreadsheet(XLS):
    xlbin = scraperwiki.scrape(XLS)
#use the open_workbook function on that new variable to create another
    book = xlrd.open_workbook(file_contents=xlbin)

#the .nsheets method tells us how many sheets 'book' has
    print "nsheets result: ", book.nsheets
#we can use that number to initialise a new variable
    sheetstotal = book.nsheets
#and then use that variable to create the end value in a range of numbers, called 'sheetsrange'
    sheetsrange = range(3,sheetstotal)
#both lines could of course have been combined into one like this:
#sheetsrange = range(0,book.nsheets)

#print "sheetsrange:" followed by that range of numbers:
    print "sheetsrange:", sheetsrange

#create a new variable, 'id', set at 0. We'll add one to this every time a loop runs, so we have a unique id for every row of data
    id = 0
#now to loop through the 'sheetsrange' variable (a list) and put each item in 'sheetnum'
    for sheetnum in sheetsrange:
        print "scraping sheet ", sheetnum
    #use the sheet_by_index method to open the first (0) sheet in variable 'book' - and put it into new variable 'sheet'
        sheet = book.sheet_by_index(sheetnum)
    #use the row_values method and index (1) to grab the second row of 'sheet'
    #and put all cells into the list variable 'title'
        title = sheet.row_values(1)
    #print the string "Title:", followed by the third [2] item (column) in the variable 'title' 
        print "Title:", title[2]
    #put cells from the 15th row into 'keys' variable 
        keys = []
        for cell in sheet.row(14):
            keys.append(str(cellval(cell,book.datemode)).replace("'",""))
        print "KEYS",keys
        keys[5].replace("'","")
        keys[6].replace("'","")
#    for key in keys:
 #       key.replace("'","")
  #      print "JOINED KEY", key
        print "keys:", keys
        print "keys[2]", keys[2]
    #create an empty dictionary variable, 'record'
        record = {}
    #loop through a range - from the 16th item (15) to a number generated by using the .nrows method on 'sheet' (to find number of rows in that sheet)
    #put each row number in 'rownumber' as you loop
        for rownumber in range(15, sheet.nrows):
            for column in range(1,sheet.ncols):
                print "Scraping row", rownumber
                record[keys[column]] = sheet.row_values(rownumber)[column]
                record['title'] = title[2]
                print "RECORD SO FAR:", record
            scraperwiki.sqlite.save([keys[2]], record, table_name=sheetnum)

def grabexcellinks(URL):
    #Use Scraperwiki's scrape function on 'URL', put results in new variable 'html'
    html = scraperwiki.scrape(URL)
    #and show it us
    print html
    #Use lxml.html's fromstring function on 'html', put results in new variable 'root'
    root = lxml.html.fromstring(html)
    #use cssselect method on 'root' to grab all <a> tags within a <p> tag - and put in a new list variable 'links'
    links = root.cssselect('p a')
    #for each item in that list variable, from the first to the second last [0:-1], put it in the variable 'link'
    for link in links[1:-1]:
        #and print the text_content of that (after the string "link text:")
        print "link text:", link.text_content()
        #use the attrib.get method on 'link' to grab the href= attribute of the HTML, and put in new 'linkurl' variable
        linkurl = link.attrib.get('href')
        #print it
        print linkurl
        #run the function scrapesheets, using that variable as the parameter
        scrapespreadsheet(linkurl)

grabexcellinks(URL)

#scrapespreadsheet(XLS)