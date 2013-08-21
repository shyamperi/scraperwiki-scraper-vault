# typical URL is http://www.london-gazette.co.uk/id/issues/60112/notices/1568529
# list of URLs collected by scraper at https://scraperwiki.com/scrapers/bankruptcies/
# Downloaded as CSV and codes extracted in Google Docs by using =RIGHT(A2, 7)
# Cycle through a list of those codes, created by using the =JOIN formula in Google Docs

#If you want to understand this scraper - start at the bottom where it says 'base_url' 

import scraperwiki
#import urlparse
import lxml.html

#Create a function called 'scrape_table' which is called in the function 'scrape_page' below
#The 'scrape_page' function also passed the contents of the page to this function as 'root'
def scrape_table(root):
    #Use cssselect to find the contents of a particular HTML tag, and put it in a new object 'divdata'
    #there's more than one div, so we need to specify the class="Data", represented by the full stop
    divdata = root.cssselect("div.Data")
    for pars in divdata:
        #Create a new empty record
        record = {}
        #Assign the contents of <td> to a new object called 'table_cells'
        lines = pars.cssselect("p")
        spans = pars.cssselect("p span")
        #If there's anything
#TO ADD: AN ELSE TO ADDRESS DATE/URLCODE WHICH ARE 'OUT OF RANGE' ON SOME PAGES        
        if lines: 
            #Put the contents of the first <p> into a record in the column 'pubdate'
            record['pubdate'] = spans[0].text
            record['noticecode'] = spans[1].text
            record['name'] = spans[2].text
            record['address'] = lines[4].text
            record['DOB'] = lines[5].text
            record['description'] = lines[6].text
            record['court'] = lines[7].text
            record['dateofpetition'] = lines[8].text
            record['dateoforder'] = lines[9].text
            record['timeoforder'] = lines[10].text
            record['petitionby'] = lines[11].text
            record['receiver'] = spans[2].text
#            record['date'] = lines[13].text
#            record['urlcode'] = lines[14].text
            record['ID'] = item
            print record, '------------'
            #Save in the SQLite database, with the ID code to be used as the unique reference
            scraperwiki.sqlite.save(["ID"], record)
        


#this creates a new function and (re)names whatever parameter is passed to it - i.e. 'next_link' below - as 'url'
def scrape_page(url):
    #now 'url' is scraped with the scraperwiki library imported above, and the contents put into a new object, 'html'
    html = scraperwiki.scrape(url)
    print html
    #now we use the lxml.html function imported above to convert 'html' into a new object, 'root'
    root = lxml.html.fromstring(html)
    #now we call another function on root, which we write - above
    scrape_table(root)

#START HERE: This is the part of the URL which all our pages share
base_url = 'http://www.london-gazette.co.uk/issues/'
#And these are the numbers which we need to complete that URL to make each individual URL
#This array has been compiled using the =JOIN formula in Google Docs on a column of URL codes
codes = ['59750/notices/1336695','59753/notices/1339819','59753/notices/1339820','59753/notices/1339818','59753/notices/1339817','59754/notices/1340684','59756/notices/1341863','59763/notices/1347313','59766/notices/1348276','59769/notices/1350316','59746/notices/1333669','59746/notices/1333469','59746/notices/1333684','59746/notices/1333502','59746/notices/1333580','59746/notices/1333559','59746/notices/1333613','59746/notices/1333478','59746/notices/1333594','59746/notices/1333549','59746/notices/1333655','59746/notices/1333606','59746/notices/1333695','59746/notices/1333648','59746/notices/1333686','59746/notices/1333603','59746/notices/1333623','59746/notices/1333572','59746/notices/1333545','59746/notices/1333616','59746/notices/1333485','59746/notices/1333463','59746/notices/1333637','59746/notices/1333661','59746/notices/1333524','59746/notices/1333666','59746/notices/1333453','59746/notices/1333448','59746/notices/1333514','59746/notices/1333518','59746/notices/1333619','59746/notices/1333522','59746/notices/1333586','59746/notices/1333692','59746/notices/1333608','59746/notices/1333470','59746/notices/1333447','59746/notices/1333568','59746/notices/1333472','59746/notices/1333458','59746/notices/1333504','59746/notices/1333509','59746/notices/1333621','59746/notices/1333595','59746/notices/1333476','59746/notices/1333573','59746/notices/1333651','59746/notices/1333517','59746/notices/1333640','59746/notices/1333552','59746/notices/1333553','59746/notices/1333660','59746/notices/1333707','59746/notices/1333627','59746/notices/1333529','59746/notices/1333585','59746/notices/1333700','59746/notices/1333521','59746/notices/1333582','59746/notices/1333592','59746/notices/1333578','59746/notices/1333677','59746/notices/1333571','59746/notices/1333703','59746/notices/1333451','59746/notices/1333512','59746/notices/1333537','59746/notices/1333701','59746/notices/1333527','59746/notices/1333596','59746/notices/1333670','59746/notices/1333698','59746/notices/1333699','59746/notices/1333576','59746/notices/1333457','59746/notices/1333520','59746/notices/1333678','59746/notices/1333528','59746/notices/1333705','59746/notices/1333466','59746/notices/1333615','59746/notices/1333473','59746/notices/1333706','59746/notices/1333583','59746/notices/1333584','59746/notices/1333507','59746/notices/1333506','59746/notices/1333685','59746/notices/1333663','59746/notices/1333674','59746/notices/1333534','59746/notices/1333702','59746/notices/1333691','59746/notices/1333672','59746/notices/1333675','59746/notices/1333614','59746/notices/1333567','59746/notices/1333668','59746/notices/1333639','59746/notices/1333483','59746/notices/1333486','59746/notices/1333605','59746/notices/1333538','59746/notices/1333664','59746/notices/1333536','59746/notices/1333535','59746/notices/1333636','59746/notices/1333566','59746/notices/1333562','59746/notices/1333555','59746/notices/1333644','59746/notices/1333505','59746/notices/1333598','59746/notices/1333671','59746/notices/1333593','59746/notices/1333455','59746/notices/1333495','59746/notices/1333556','59746/notices/1333523','59746/notices/1333683','59746/notices/1333589','59746/notices/1333481','59746/notices/1333482','59746/notices/1333464','59746/notices/1333665','59746/notices/1333561','59746/notices/1333560','59746/notices/1333484','59746/notices/1333587','59746/notices/1333620','59746/notices/1333551','59746/notices/1333565','59746/notices/1333645','59746/notices/1333496','59746/notices/1333487','59746/notices/1333452','59746/notices/1333563','59746/notices/1333542','59746/notices/1333488','59746/notices/1333508','59746/notices/1333539','59746/notices/1333626','59746/notices/1333554','59746/notices/1333475','59746/notices/1333588','59746/notices/1333634','59746/notices/1333530','59746/notices/1333532','59746/notices/1333591','59746/notices/1333693','59746/notices/1333474','59746/notices/1333533','59746/notices/1333600','59746/notices/1333497','59746/notices/1333599','59746/notices/1333547','59746/notices/1333546','59746/notices/1333477','59746/notices/1333602','59746/notices/1333462','59746/notices/1333471','59746/notices/1333681','59746/notices/1333515','59746/notices/1333688','59746/notices/1333680','59746/notices/1333631','59746/notices/1333519','59746/notices/1333604','59746/notices/1333643','59746/notices/1333646','59746/notices/1333625','59746/notices/1333503','59746/notices/1333540','59746/notices/1333629','59746/notices/1333499','59746/notices/1333633','59746/notices/1333659','59746/notices/1333480','59746/notices/1333642','59746/notices/1333649','59746/notices/1333489','59746/notices/1333465','59746/notices/1333617','59746/notices/1333564','59746/notices/1333612','59746/notices/1333544','59746/notices/1333632','59746/notices/1333500','59746/notices/1333569','59746/notices/1333630','59746/notices/1333581','59746/notices/1333709','59746/notices/1333708','59750/notices/1336621','59750/notices/1336823','59750/notices/1336904','59750/notices/1336472','59750/notices/1336514','59750/notices/1336459','59750/notices/1336861','59750/notices/1336912','59750/notices/1336565','59750/notices/1336564','59750/notices/1336618','59750/notices/1336573','59750/notices/1336833','59750/notices/1336910','59750/notices/1336828','59750/notices/1336653','59750/notices/1336650','59750/notices/1336844','59750/notices/1336853','59750/notices/1336602','59750/notices/1336442','59750/notices/1336945','59750/notices/1336776','59750/notices/1336590','59750/notices/1336987','59750/notices/1336616','59750/notices/1336744','59750/notices/1336947','59750/notices/1336906','59750/notices/1336863','59750/notices/1336589','59750/notices/1336964','59750/notices/1336818','59750/notices/1336899','59750/notices/1336898','59750/notices/1336655','59750/notices/1336540','59750/notices/1336539','59750/notices/1336850','59750/notices/1336482','59750/notices/1336883','59750/notices/1336914','59750/notices/1336874','59750/notices/1336607','59750/notices/1336905','59750/notices/1336777','59750/notices/1336500','59750/notices/1336648','59750/notices/1336566','59750/notices/1336979','59750/notices/1336893','59750/notices/1336517','59750/notices/1336935','59750/notices/1336490','59750/notices/1336671','59750/notices/1336510','59750/notices/1336991','59750/notices/1336548','59750/notices/1336793','59750/notices/1336841','59750/notices/1336815','59750/notices/1336867','59750/notices/1336865','59750/notices/1336873','59750/notices/1336838','59750/notices/1336922','59750/notices/1336552','59750/notices/1336763','59750/notices/1336975','59750/notices/1336608','59750/notices/1336609','59750/notices/1336745','59750/notices/1336758','59750/notices/1336923','59750/notices/1336476','59750/notices/1336496','59750/notices/1336624','59750/notices/1336877','59750/notices/1336780','59750/notices/1336924','59750/notices/1336691','59750/notices/1336584','59750/notices/1336908','59750/notices/1336836','59750/notices/1336632','59750/notices/1336615','59750/notices/1336641','59750/notices/1336509','59750/notices/1336993','59750/notices/1336690','59750/notices/1336997','59750/notices/1336636','59750/notices/1336542','59750/notices/1336769','59750/notices/1336946','59750/notices/1336736','59750/notices/1336757','59750/notices/1336943','59750/notices/1336791','59750/notices/1336635','59750/notices/1336760','59750/notices/1336967','59750/notices/1336986','59750/notices/1336761','59750/notices/1336921','59750/notices/1336468','59750/notices/1336955','59750/notices/1336990','59750/notices/1336561','59750/notices/1336521','59750/notices/1336622','59750/notices/1336623','59750/notices/1336673','59750/notices/1336684','59750/notices/1336478','59750/notices/1336954','59750/notices/1336974','59750/notices/1336820','59750/notices/1336511','59750/notices/1336592','59750/notices/1336452','59750/notices/1336951','59750/notices/1336934','59750/notices/1336750','59750/notices/1336881','59750/notices/1336900','59750/notices/1336880','59750/notices/1336578','59750/notices/1336999','59750/notices/1336968','59750/notices/1336541','59750/notices/1336824','59750/notices/1336450','59750/notices/1337002','59750/notices/1337001','59750/notices/1336829','59750/notices/1336577','59750/notices/1336576','59750/notices/1336557','59750/notices/1336481','59750/notices/1336461','59750/notices/1336995','59750/notices/1336966','59750/notices/1336507','59750/notices/1336972','59750/notices/1336970','59750/notices/1336661','59750/notices/1336674','59750/notices/1336879','59750/notices/1336662','59750/notices/1336965','59750/notices/1336489','59750/notices/1336572','59750/notices/1336813','59750/notices/1336456','59750/notices/1336652','59750/notices/1336739','59750/notices/1336909','59750/notices/1336740','59750/notices/1336629','59750/notices/1336971','59750/notices/1336683','59750/notices/1336855','59750/notices/1336862','59750/notices/1336530','59750/notices/1336840','59750/notices/1336457','59750/notices/1336915','59750/notices/1336494','59750/notices/1336944','59750/notices/1336493','59750/notices/1336856','59750/notices/1336804','59750/notices/1336603','59750/notices/1336903','59750/notices/1336574','59750/notices/1336746','59750/notices/1336843','59750/notices/1336682','59750/notices/1336440','59750/notices/1336802','59750/notices/1336984','59750/notices/1336989','59750/notices/1336767','59750/notices/1336687','59750/notices/1336837','59750/notices/1336754','59750/notices/1336985','59750/notices/1336992','59750/notices/1336803','59750/notices/1336538','59750/notices/1336537','59750/notices/1336890','59750/notices/1336513','59750/notices/1336471','59750/notices/1336888','59750/notices/1336627','59750/notices/1336487','59750/notices/1336467','59750/notices/1336466','59750/notices/1336936','59750/notices/1336741','59750/notices/1336892','59750/notices/1336568','59750/notices/1336875','59750/notices/1336942','59750/notices/1336491','59750/notices/1336956','59750/notices/1336812','59750/notices/1336811','59750/notices/1336598','59750/notices/1336580','59750/notices/1336463','59750/notices/1336749','59750/notices/1336738','59750/notices/1336957','59750/notices/1336958','59750/notices/1336788','59750/notices/1336614','59750/notices/1336988','59750/notices/1336998','59750/notices/1336579','59750/notices/1336585','59750/notices/1336919','59750/notices/1336831','59750/notices/1336640','59750/notices/1336747','59750/notices/1336933','59750/notices/1336495','59750/notices/1336502','59750/notices/1336474','59750/notices/1336980','59750/notices/1336571','59750/notices/1336613','59750/notices/1336575','59750/notices/1336996','59750/notices/1336559','59750/notices/1336560','59750/notices/1336597','59750/notices/1336759','59750/notices/1336978','59750/notices/1336656','59750/notices/1336498','59750/notices/1336692','59750/notices/1336554','59750/notices/1336553','59750/notices/1337000','59750/notices/1336654','59750/notices/1336960','59750/notices/1336453','59750/notices/1336742','59750/notices/1336822','59750/notices/1336931','59750/notices/1336658','59750/notices/1336680','59750/notices/1336819','59750/notices/1336570','59750/notices/1336930','59750/notices/1336771','59750/notices/1336983','59750/notices/1336497','59750/notices/1336555','59750/notices/1336556','59750/notices/1336688','59750/notices/1336857','59750/notices/1336619','59750/notices/1336858','59750/notices/1336869','59750/notices/1336551','59750/notices/1336950','59750/notices/1336686','59750/notices/1336895','59750/notices/1336515','59750/notices/1336783','59750/notices/1336645','59750/notices/1336670','59750/notices/1336550','59750/notices/1336821','59750/notices/1336676','59750/notices/1336499','59750/notices/1336626','59750/notices/1336620','59750/notices/1336932','59750/notices/1336939','59750/notices/1336925']

#go through the schoolIDs array above, and for each ID...
for item in codes:
    #show it in the console
    print item
    #create a URL called 'next_link' which adds that ID to the end of the base_url variable
    next_link = base_url+item
    #pass that new concatenated URL to a function, 'scrape_page', which is scripted above
    scrape_page(next_link)

