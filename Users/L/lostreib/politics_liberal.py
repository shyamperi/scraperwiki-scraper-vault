import scraperwiki
import urllib2
from BeautifulSoup import BeautifulSoup

# Blank Python

school_list = ['north-dakota-state-university','university-of-akron','ashland-university','baldwin--wallace-college','bowling-green-state-university','case-western-reserve-university','cedarville-university','central-state-university','university-of-cincinnati','cleveland-state-university','university-of-dayton','denison-university','hiram-college','john-carroll-university','kent-state-university','miami-university','oberlin-college','ohio-state-university','ohio-university','otterbein-university','university-of-toledo','wittenberg-university','xavier-university','kenyon-college','university-of-mount-union','ohio-wesleyan-university','franciscan-university-of-steubenville','college-of-wooster','youngstown-state-university','university-of-findlay','mount-vernon-nazarene-university','ohio-northern-university','wright-state-university','cameron-university','oklahoma-christian-university','oklahoma-city-university','oral-roberts-university','university-of-tulsa','university-of-central-oklahoma','oklahoma-state-university','university-of-oklahoma','lewis--and--clark-college','oregon-state-university','university-of-oregon','university-of-portland','southern-oregon-university','willamette-university','western-oregon-university','george-fox-university','linfield-college','pacific-university','portland-state-university','reed-college','arcadia-university','bucknell-university','carnegie-mellon-university','cedar-crest-college','dickinson-college','east-stroudsburg-university-of-pennsylvania','franklin--and--marshall-college','geneva-college','gettysburg-college','grove-city-college','haverford-college','indiana-university-of-pennsylvania','kutztown-university-of-pennsylvania','la-roche-college','la-salle-university','lincoln-university-of-pennsylvania','lock-haven-university','mercyhurst-college','messiah-college','penn-state-altoona','penn-state','university-of-pittsburgh----johnstown','university-of-pittsburgh','point-park-university','saint-francis-university','university-of-scranton','susquehanna-university','ursinus-college','washington--and--jefferson-college','west-chester-university-of-pennsylvania','westminster-college----pennsylvania','york-college-pennsylvania','bloomsburg-university-of-pennsylvania','california-university-of-pennsylvania','clarion-university-of-pennsylvania','drexel-university','elizabethtown-college','lafayette-college','misericordia-university','muhlenberg-college','university-of-pennsylvania','philadelphia-university','robert-morris-university','saint-vincent-college','slippery-rock-university','swarthmore-college','temple-university','wilkes-university','allegheny-college','bryn-mawr-college','chatham-university','duquesne-university','edinboro-university','gannon-university','juniata-college','lehigh-university','millersville-university-of-pennsylvania','saint-josephs-university','shippensburg-university-of-pennsylvania','villanova-university','widener-university','brown-university','bryant-university','providence-college','rhode-island-college','johnson--and--wales-university','university-of-rhode-island','roger-williams-university','salve-regina-university','converse-college','francis-marion-university','furman-university','south-carolina-state-university','university-of-south-carolina----upstate','voorhees-college','benedict-college','college-of-charleston','claflin-university','newberry-college','university-of-south-carolina','winthrop-university','anderson-university----south-carolina','charleston-southern-university','clemson-university','lander-university','coastal-carolina-university','south-dakota-state-university','university-of-south-dakota','belmont-university','lipscomb-university','middle-tennessee-state-university','sewanee----the-university-of-the-south','university-of-tennessee','university-of-tennessee----martin','vanderbilt-university','austin-peay-state-university','rhodes-college','university-of-tennessee----chattanooga','east-tennessee-state-university','freed--hardeman-university','lee-university','university-of-memphis','southern-adventist-university','tennessee-state-university','tennessee-technological-university','texas-a-and-m-university----corpus-christi','dallas-baptist-university','university-of-houston----downtown','university-of-the-incarnate-word','university-of-mary-hardin--baylor','southern-methodist-university','southwestern-university','stephen-f-austin-state-university','tarleton-state-university','texas-a-and-m-university','university-of-texas----arlington','university-of-texas----austin','university-of-texas----dallas','texas-christian-university','university-of-texas----san-antonio','texas-tech-university','texas-womans-university','trinity-university','west-texas-a--and--m-university','abilene-christian-university','angelo-state-university','texas-a-and-m-university----commerce','lamar-university','university-of-texas----pan-american','university-of-texas----pan-american','rice-university','university-of-texas----el-paso','university-of-texas----tyler','austin-college','baylor-university','houston-baptist-university','university-of-houston','texas-a-and-m-international-university','midwestern-state-university','university-of-texas----brownsville','prairie-view-a--and--m-university','sam-houston-state-university','texas-state-university','texas-a-and-m-university----kingsville','texas-southern-university','brigham-young-university','university-of-utah','weber-state-university','westminster-college----utah','utah-state-university','southern-utah-university','middlebury-college','university-of-vermont','marlboro-college','champlain-college','christopher-newport-university','hampton-university','hollins-university','liberty-university','norfolk-state-university','radford-university','roanoke-college','shenandoah-university','virginia-commonwealth-university','university-of-virginia','college-of-william--and--mary','james-madison-university','mary-baldwin-college','marymount-university','virginia-state-university','george-mason-university','university-of-mary-washington','old-dominion-university','university-of-richmond','washington--and--lee-university','gonzaga-university','saint-martins-university','seattle-university','washington-state-university','university-of-washington','western-washington-university','central-washington-university','pacific-lutheran-university','whitman-college','eastern-washington-university','university-of-puget-sound','seattle-pacific-university','marshall-university','west-virginia-university','alverno-college','beloit-college','carthage-college','lawrence-university','marquette-university','university-of-wisconsin----eau-claire','university-of-wisconsin----green-bay','university-of-wisconsin----oshkosh','university-of-wisconsin----stout','university-of-wisconsin----stevens-point','ripon-college','university-of-wisconsin----whitewater','university-of-wisconsin','university-of-wisconsin----milwaukee','university-of-wyoming']

#print list[0]

for thisSchool in school_list:
    #print thisSchool

    try:
        page = urllib2.urlopen("http://collegeprowler.com/" + thisSchool + "/diversity/student-polls/")

        soup = BeautifulSoup(page)

        table_five = soup.findAll("table")[0]

        politics_label = table_five.findAll("td")[4].string #label
        #print politics_label

        politics_value = table_five.findAll("td")[5].string #value
        print politics_value

        

        
    
    except  (IndexError):
         print "Oops! Try again..."
    
    scraperwiki.sqlite.save([], {thisSchool: politics_value})
