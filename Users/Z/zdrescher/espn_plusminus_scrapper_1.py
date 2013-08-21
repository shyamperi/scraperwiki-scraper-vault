from urllib2 import urlopen
from lxml.html import fromstring, tostring
from scraperwiki.sqlite import save
import datetime
from unidecode import unidecode

i=1
while i<762:
    print i
    iStr = str(i)
    url = "http://espn.go.com/nhl/statistics/player/_/stat/points/sort/plusMinus/seasontype/2/count/"+iStr
    page = urlopen(url) #This line defines your webpage of interest

    rawText=page.read() #This function reads through the page you've defined
    rawHTML=fromstring(rawText) #This variable contains a string (letters) of the raw HTML text of your website

    print tostring(rawHTML)



    tables = rawHTML.cssselect('table') #Now we get into sorting through that HTML code, and isolating the table you want to work with

    table=tables[0] #This saves your table, isolating it from any other tables on the webpage
    print tostring(table)

    header_row = table.cssselect('tr')[1] #this selects the second row, which contains the column names
    column_names = [td.text_content().replace('.','') for td in header_row.cssselect('th,td')]
    columnnames = column_names[0:17]
    columnnames[4]="goals"
    columnnames[5]="assists"
    columnnames[7]="plusminus"
    columnnames[9]="pointspergame"
    columnnames[13]="PPG"
    columnnames[14]="PPA"
    columnnames[15]="SHG"
    columnnames[16]="SHA"

    print column_names[0:17] #this saves those column names as a variable we can reference later

    for tr in table.cssselect('tr')[2:]: #This selects a specific row from the third row onwards
        cellvalues = [td.text_content() for td in tr.cssselect('td')] #this saves the contents of that row as an object in our table
        data = dict(zip(columnnames, cellvalues)) #this saves the data in our set
        for key in ['GP','goals','assists','PTS',"plusminus", "PIM","PPG", "PPA", "SHG", "SHA"]:
            try: 
                data['key']=int(data['key'])  
            except:
                pass
        for key in ['PLAYER', 'TEAM']:
            try: 
                data['key']=str(data['key'])  
            except:
                pass
        save([], data)
    i=i+40

data['rawHTML'] = unidecode(rawText)  
print data['rawHTML']