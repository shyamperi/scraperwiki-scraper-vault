import scraperwiki
import urllib2
from BeautifulSoup import BeautifulSoup

# Blank Python

school_list = ['alabama-a--and--m-university','university-of-alabama----birmingham','university-of-alabama----huntsville','auburn-university','university-of-north-alabama','samford-university','University-of-South-Alabama','columbia-southern-university','alabama-state-university','auburn-university----montgomery','jacksonville-state-university','university-of-montevallo','oakwood-university','university-of-alabama','birmingham--southern-college','troy-university','tuskegee-university','university-of-alaska-anchorage','university-of-alaska-fairbanks','grand-canyon-university','university-of-advancing-technology','arizona-state-university','university-of-arizona','embry--riddle-aeronautical-university----prescott','northern-arizona-university','university-of-phoenix----phoenix--hohokam','university-of-phoenix----southern-arizona','university-of-arkansas-at-little-rock','university-of-arkansas','harding-university','arkansas-state-university','philander-smith-college','arkansas-tech-university','hendrix-college','university-of-the-ozarks','california-baptist-university','california-institute-of-technology','california-lutheran-university','california-state-university----stanislaus','california-state-university----san-bernardino','california-state-university----chico','california-state-university----dominguez-hills','california-state-university----fresno','california-state-university----fullerton','california-state-university----northridge','university-of-california----davis','university-of-california----irvine','university-of-california----los-angeles','university-of-california----santa-barbara','university-of-la-verne','loyola-marymount-university','mills-college','occidental-college','university-of-the-pacific','pepperdine-university','pomona-college','university-of-redlands','san-diego-state-university','university-of-san-francisco','san-jose-state-university','scripps-college','sonoma-state-university','vanguard-university-of-southern-california','university-of-southern-california','california-state-university----san-marcos','california-polytechnic-state-university----san-luis-obispo','california-state-university----east-bay','california-state-university----sacramento','university-of-california----riverside','university-of-california----san-diego','university-of-california----santa-cruz','chapman-university','claremont-mckenna-college','harvey-mudd-college','humboldt-state-university','pitzer-college','university-of-san-diego','santa-clara-university','stanford-university','azusa-pacific-university','biola-university','california-state-university----bakersfield','california-state-polytechnic-university----pomona','california-state-university----long-beach','california-state-university----los-angeles','university-of-california----berkeley','pacific-union-college','point-loma-nazarene-university','san-francisco-state-university','whittier-college','california-state-university----monterey-bay','university-of-colorado-denver','university-of-colorado-at-colorado-springs','university-of-colorado----boulder','colorado-school-of-mines','colorado-state-university','university-of-denver','colorado-mesa-university','metropolitan-state-college-of-denver','colorado-state-university----pueblo','colorado-college','university-of-northern-colorado','regis-university','university-of-bridgeport','fairfield-university','university-of-hartford','university-of-new-haven','quinnipiac-university','sacred-heart-university','southern-connecticut-state-university','trinity-college','western-connecticut-state-university','yale-university','connecticut-college','university-of-connecticut','wesleyan-university','central-connecticut-state-university','delaware-state-university','university-of-delaware','american-university','catholic-university-of-america','george-washington-university','howard-university','georgetown-university','university-of-the-district-of-columbia','barry-university','bethune--cookman-university','university-of-central-florida','eckerd-college','embry--riddle-aeronautical-university----daytona-beach','florida-a-and-m-university','florida-international-university','florida-southern-college','florida-state-university','university-of-miami','university-of-north-florida','nova-southeastern-university','rollins-college','university-of-south-florida','stetson-university','university-of-tampa','new-college-of-florida','jacksonville-university','saint-leo-university','southeastern-university----florida','university-of-west-florida','ave-maria-university','south-university----tampa','florida-atlantic-university','florida-institute-of-technology','university-of-florida','florida-gulf-coast-university','albany-state-university','augusta-state-university','columbus-state-university','emory-university','fort-valley-state-university','georgia-institute-of-technology','georgia-college--and--state-university','university-of-georgia','north-georgia-college--and--state-university','valdosta-state-university','georgia-gwinnett-college','agnes-scott-college','armstrong-atlantic-state-university','clark-atlanta-university','berry-college','covenant-college','georgia-southern-university','georgia-state-university','wesleyan-college','university-of-west-georgia','clayton-state-university','kennesaw-state-university','mercer-university','morehouse-college','oglethorpe-university','savannah-state-university','spelman-college','southern-polytechnic-state-university','university-of-hawaii-at-hilo','university-of-hawaii-at-manoa','hawaii-pacific-university','boise-state-university','idaho-state-university','brigham-young-university----idaho','university-of-idaho','augustana-college----rock-island','university-of-chicago','columbia-college-chicago','elmhurst-college','illinois-wesleyan-university','illinois-state-university','millikin-university','northwestern-university','northeastern-illinois-university','olivet-nazarene-university','southern-illinois-university-carbondale','southern-illinois-university-edwardsville','western-illinois-university','bradley-university','depaul-university','eastern-illinois-university','illinois-institute-of-technology','lewis-university','mckendree-university','north-central-college','northern-illinois-university','roosevelt-university','aurora-university','chicago-state-university','university-of-illinois-at-chicago','university-of-illinois-at-urbana--champaign','loyola-university-chicago','anderson-university----indiana','butler-university','earlham-college','hanover-college','indiana-university--purdue-university----fort-wayne','university-of-indianapolis','university-of-southern-indiana','indiana-university','indiana-wesleyan-university','purdue-university----calumet','saint-marys-college','valparaiso-university','purdue-university','ball-state-university','indiana-state-university','depauw-university','indiana-university----south-bend','university-of-notre-dame','taylor-university','coe-college','drake-university','grinnell-college','university-of-iowa','dordt-college','luther-college','university-of-northern-iowa','cornell-college','iowa-state-university','kansas-state-university','emporia-state-university','university-of-kansas','wichita-state-university','bellarmine-university','berea-college','university-of-kentucky']

#print list[0]

for thisSchool in school_list:
    #print thisSchool

    try:
        page = urllib2.urlopen("http://collegeprowler.com/" + thisSchool + "/admissions/student-polls/")

        soup = BeautifulSoup(page)

        table_one = soup.findAll("table")[0]

        happiness_label = table_one.findAll("td")[5].string #label
        #print happiness_label

        happiness_value = table_one.findAll("td")[4].string #value
        print happiness_value

        

        
    
    except  (IndexError):
         print "Oops! Try again..."
    
    
