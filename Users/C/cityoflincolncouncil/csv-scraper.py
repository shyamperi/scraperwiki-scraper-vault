# We're going to scrape a CSV and see what we can do with it!
# http://www.lincoln.gov.uk/doclib/AREA_A_ERMINE_EAST_PLAN_6_03_09_version3.csv

import urllib
import csv
import scraperwiki

# We'll open our CSV file
url = []

url.append("http://www.lincoln.gov.uk/doclib/DHomesCityCentre.csv")



clist = []

for source in url:
    f = urllib.urlopen(source)
    lines = f.readlines()

    lines.pop(0)

    tempclist = list(csv.reader(lines))
    #print lines

    for line in tempclist:
        clist.append(line)

print clist

# Now we're going to build up an array of tables so that we can map multiple properties to one postcode

formatted = []

for row in clist:

    #Make sure we're not trying to process an empty row
    if len(row) > 0:
        #print len(row)
        #print row

        issame = 0
        prow = 0
    
        bathroom = ''
        bathroomstyle = ''
        chimneys = ''
        chimneystyle = ''
        electrics = ''
        electricstyle = ''
        heating = ''
        heatingstyle = ''
        kitchen = ''
        kitchenstyle = ''
        roof = ''
        roofstyle = ''
        structure = ''
        structurestyle = ''
        thermal = ''
        thermalstyle = ''
        doors = ''
        doorstyle = ''

        #Here we're going to check the data and generate some classes for displaying
        #First off, let's get the status so that we can style the whole row
    
        if row[3] == 'D':
            rowstyle = ' class="decent"'
        elif row[3] == 'U/S':
            rowstyle = ' class="unsurveyed"'
        else:
            rowstyle = ''
    
        #Now let's look at each individual element so that we can style that based on whether the work has been done or not#
        #We've got some error checking in here to make sure that we're allowing for discrepancies in the data
        #Bathroom
        try:
            bathroom = row[4]
            if row[4] <> '':
                bathroomstyle = ' bathroom'
            else:
                bathroomstyle = ''
        except:
            bathroom = ''
            bathroomstyle = ''

        #Chimneys
        try:
            chimneys = row[5]
            if row[5] <> '':
                chimneystyle= ' chimneys'
            else:
                chimneystyle= ''
        except:
            chimneys = ''
            chimneystyle = ''
    
        #Electrics
        try:
            electrics = row[6]
            if row[6] <> '':
                electricstyle = ' electrics'
            else:
                electricstyle = ''
        except:
            electrics = ''
            electricstyle = ''
    
        #Heating
        try:
            heating = row[7]
            if row[7] <> '':
                heatingstyle = ' heating'
            else:
                heatingstyle = ''
        except:
            heating = ''
            heatingstyle = ''
    
        #Kitchen
        try:
            kitchen = row[8]
            if row[8] <> '':
                kitchenstyle = ' kitchen'
            else:
                kitchenstyle = ''
        except:
            kitchen = ''
            kitchenstyle = ''
    
        #Roof
        try:
            roof = row[9]
            if row[9] <> '':
                roofstyle = ' roof'
            else:
                roofstyle = ''
        except:
            roof = ''
            roofstyle = ''
    
        #Structure
        try:
            structure = row[10]
            if row[10] <> '':
                structurestyle = ' structure'
            else:
                doorstyle = ''
        except:
            structure = ''
            structurestyle = ''
    
        #Thermal
        try:
            thermal = row[11]
            if row[11] <> '':
                thermalstyle = ' thermal'
            else:
                thermalstyle = ''
        except:
            thermal = ''
            thermalstyle = ''
    
        #Doors
        try:
            doors = row[12]
            if row[12] <> '':
                doorstyle = ' doors'
            else:
                doorstyle = ''
        except:
            doors = ''
            doorstyle = ''
    
    
        house_row = '<tr'+rowstyle+'><td class="cell_left">'+row[0]+'</td><td>'+row[2]+'</td><td class="center">'+row[3]+'</td><td class="center'+bathroomstyle+'">'+bathroom+'</td><td class="center'+chimneystyle+'">'+chimneys+'</td><td class="center'+electricstyle+'">'+electrics+'</td><td class="center'+heatingstyle+'">'+heating+'</td><td class="center'+kitchenstyle+'">'+kitchen+'</td><td class="center'+roofstyle+'">'+roof+'</td><td class="center'+structurestyle+'">'+structure+'</td><td class="center'+thermalstyle+'">'+thermal+'</td><td class="cell_right'+doorstyle+'">'+doors+'</td></tr>'
    
        count = 0
        for frow in formatted:
            if frow[0] == row[1]:
                issame = 1
                prow = count 
            count += 1
                
        # print prow    
    
        if issame == 1:
            formatted[prow][1] += house_row
    
        else:
            new_row = [row[1],house_row]
            # print new_row
            formatted.append(new_row)
        
        # print formatted[prow][0]

#print formatted    



#And now let's write our formatted data into ScraperWiki
scraperwiki.metadata.save('data_columns', ['Postcode', 'Data'])

#print clist

for row in formatted:
    #print row

    record = {}
    
    record['Postcode'] = row[0]
    record['Data'] = row[1]

    print record

    scraperwiki.datastore.save(["Postcode"], record)
