import scraperwiki
import urllib2
from BeautifulSoup import BeautifulSoup

# Blank Python

school_list = ['morehead-state-university','union-college','university-of-louisville','murray-state-university','northern-kentucky-university','centre-college','eastern-kentucky-university','western-kentucky-university','dillard-university','grambling-state-university','louisiana-tech-university','loyola-university-new-orleans','university-of-new-orleans','university-of-louisiana----monroe','southeastern-louisiana-university','tulane-university','xavier-university-of-louisiana','centenary-college-of-louisiana','louisiana-college','southern-university--and--a-and-m-college','university-of-louisiana----lafayette','louisiana-state-university','northwestern-state-university-of-louisiana','bowdoin-college','colby-college','university-of-maine','university-of-new-england','bates-college','coppin-state-university','frostburg-state-university','university-of-maryland----baltimore-county','mount-st-marys-university','stevenson-university','johns-hopkins-university','university-of-maryland----college-park','towson-university','university-of-baltimore','bowie-state-university','goucher-college','hood-college','loyola-university-maryland','university-of-maryland----college-park','university-of-maryland-eastern-shore','morgan-state-university','salisbury-university','amherst-college','bentley-university','boston-university','clark-university','hampshire-college','harvard-university','college-of-the-holy-cross','university-of-massachusetts----amherst','massachusetts-institute-of-technology','northeastern-university','suffolk-university','tufts-university','westfield-state-university','brandeis-university','emerson-college','lesley-university','massachusetts-college-of-liberal-arts','simmons-college','wellesley-college','wheaton-college----illinois','worcester-polytechnic-institute','bay-path-college','boston-college','bridgewater-state-university','emmanuel-college----boston','fitchburg-state-university','university-of-massachusetts----lowell','mount-holyoke-college','salem-state-university','smith-college','university-of-massachusetts----dartmouth','williams-college','albion-college','central-michigan-university','davenport-university','kettering-university','university-of-michigan----ann-arbor','michigan-state-university','michigan-technological-university','university-of-michigan----dearborn','western-michigan-university','calvin-college','eastern-michigan-university','ferris-state-university','saginaw-valley-state-university','spring-arbor-university','grand-valley-state-university','northern-michigan-university','oakland-university','wayne-state-university','carleton-college','gustavus-adolphus-college','macalester-college','northwestern-college----minnesota','saint-cloud-state-university','hamline-university','minnesota-state-university','university-of-minnesota----twin-cities','minnesota-state-university----moorhead','augsburg-college','concordia-college-at-moorhead','university-of-minnesota----duluth','winona-state-university','millsaps-college','university-of-mississippi','mississippi-state-university','university-of-southern-mississippi','jackson-state-university','university-of-central-missouri','missouri-western-state-university','university-of-missouri','university-of-missouri----kansas-city','rockhurst-university','missouri-state-university','maryville-university','missouri-university-of-science--and--technology','webster-university','lindenwood-university','truman-state-university','northwest-missouri-state-university','park-university','saint-louis-university','southeast-missouri-state-university','university-of-montana','montana-state-university','hastings-college','university-of-nebraska----lincoln','creighton-university','university-of-nebraska-at-omaha','university-of-nevada----las-vegas','university-of-nevada----reno','dartmouth-college','university-of-new-hampshire','keene-state-college','plymouth-state-university','fairleigh-dickinson-university----college-at-florham','rowan-university','william-paterson-university-of-new-jersey','montclair-state-university','new-jersey-institute-of-technology','rutgers-university----newark','william-paterson-university-of-new-jersey','drew-university','fairleigh-dickinson-university','montclair-state-university','new-jersey-institute-of-technology','princeton-university','rider-university','rutgers-university','stevens-institute-of-technology','kean-university','ramapo-college-of-new-jersey','seton-hall-university','the-richard-stockton-college-of-new-jersey','the-college-of-new-jersey','university-of-new-mexico','new-mexico-state-university','adelphi-university','alfred-university','canisius-college','cornell-university','cuny-baruch-college','cuny-college-of-staten-island','cuny-city-college-of-new-york','cuny-queens-college','hamilton-college','hofstra-university','long-island-university----brooklyn','manhattan-college','nazareth-college','niagara-university','pratt-institute','rensselaer-polytechnic-institute','university-of-rochester','sarah-lawrence-college','suny-university-at-albany','suny-university-at-buffalo','suny-stony-brook-university','suny-fredonia','suny-potsdam','suny-plattsburgh','united-states-military-academy-at-west-point','vassar-college','wagner-college','bard-college','barnard-college','colgate-university','columbia-university','cuny-hunter-college','cuny-lehman-college','elmira-college','fordham-university','hobart--and--william-smith-colleges','iona-college','ithaca-college','manhattanville-college','marymount-manhattan-college','college-of-mount-saint-vincent','the-new-school','new-york-university','the-college-of-saint-rose','skidmore-college','suny-college-at-brockport','suny-university-at-buffalo','suny-geneseo','suny-new-paltz','syracuse-university','cuny-brooklyn-college','cuny-john-jay-college-of-criminal-justice','marist-college','pace-university','rochester-institute-of-technology','suny-binghamton-university','suny-college-at-oneonta','suny-purchase-college','union-college','appalachian-state-university','campbell-university','davidson-college','duke-university','east-carolina-university','elizabeth-city-state-university','elon-university','guilford-college','montreat-college','university-of-north-carolina-at-asheville','university-of-north-carolina-at-chapel-hill','university-of-north-carolina----greensboro','north-carolina-central-university','university-of-north-carolina----wilmington','university-of-north-carolina-at-pembroke','salem-college','wake-forest-university','warren-wilson-college','winston--salem-state-university','western-carolina-university','bennett-college-for-women','fayetteville-state-university','north-carolina-state-university','gardner--webb-university','high-point-university','north-carolina-a-and-t-state-university','university-of-north-carolina-at-charlotte','shaw-university','university-of-north-dakota']

#print list[0]

for thisSchool in school_list:
    #print thisSchool

    try:
        page = urllib2.urlopen("http://collegeprowler.com/" + thisSchool + "/guys--and--girls/student-polls/")

        soup = BeautifulSoup(page)

        table_one = soup.findAll("table")[1]

        attractive_label = table_one.findAll("td")[22].string #label
        #print attractive_label

        attractive_value = table_one.findAll("td")[23].string #value
        print attractive_value
    
    except  (IndexError):
         print "Oops! Try again..."
    
    scraperwiki.sqlite.save([], {thisSchool: attractive_value})