import scraperwiki
import lxml.html

html = []
root = []

html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Agri­cola+Daniella&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Agricola+El+Consuelo,+S+de+RL+de+CV&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Agricola+El+Rosal+S.A+de+C.V.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Agricola+Pony+S.A.+de+C.V.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Andrew+&+Williamson&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Andrew+Smith+Company&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Babe+Farms&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Baja+Premium+Fresh&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=BeachSide+Produce,+LLC.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Better+Produce&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=BJ+Brothers+Produce,+LLC.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Boggiatto+Produce,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=BoniPak+Produce+Company&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Brooks+Tropicals,+LLC&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Cal-Cel+Marketing&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=California+Giant,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=CC+Tropicales+S.A.+de+C.+V.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Central+West+Produce&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Channel+Islands+Farms,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Chieftain+Harvesting+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Christopher+Ranch+L.L.C.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Church+Brothers&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Circle+Produce+Co.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Classic+Salads&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Coastline+Produce&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Combs+Produce/First+Choice+Distributing&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Custom+Produce+Sales&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Divine+Flavor,+LLC&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Driscoll+Strawberry+Associates,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Duda+Farm+Fresh+Foods,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Eclipse+Berry+Farms,+L.L.C.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Expo+Fresh+San+Vicente+Camalu+SPR+de+RI&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape("http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Farmer's+Best+International,+LLC&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort="))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Five+Crowns+Marketing&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape("http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Frank's+Distributing+of+Produce,+LLC&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort="))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Fresh+Farms+(MJ+International+Marketing+LLC)&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Fresh+Kist+Produce,+L.L.C&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Fresh+Quest+Produce&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Freshway+Foods&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Frutas+Selectas+de+Tijuana,+S+de+RL+de+CV&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Gargiulo,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=General+Produce,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=George+Amaral+Ranches+Inc&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=GR+Produce,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Harris+Farms/Harris+Fresh&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=HC+Produce,+LCC&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Heller+Bros.+Packing+Corp&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Hugh+H.+Branch+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=J-C+Distributing,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Kaliroy+Produce,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Kingdom+Fresh+Produce,+Inc&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Limoneira+Company&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Mann+Packing+Company,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=MAS+Melons+&+Grapes&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Metz+Fresh,+LLC&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Meyer+Tomatoes&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Misionero+Vegetables&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Naturipe+Farms,+LLC.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=New+Lime+Co.+LLC.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=NewStar+Fresh+Foods,+LLC&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Ocean+Mist+Farms&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Pacific+International+Marketing&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Pacific+Tomato+Growers,+Ltd.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Pappas+Produce+Company&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Pinos+Produce,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Pismo+Oceano+Vegetable+Exchange&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Prime+Time+International&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Red+Blossom+Farms,+Inc&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Righetti+Farms+LLC&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Rio+Queen+Citrus,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=River+Ranch+Fresh+Foods&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=RM+Produce+Corporation&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Royal+Flavor&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=S&H+Packing+&+Sales+Co+Inc&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Salad+Savoy+Corporation&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=San+Miguel+Produce,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Sanbon,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Santa+Barbara+Farms+LLC&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Santa+Sweets,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Shuman+Produce,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Sigma+Sales,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Simonian+Fruit+Co.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape("http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Six+L's/Custom+Pak,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort="))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Sun+Coast+Farms+Sales,+LLC.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Sun+World+International&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=SunFed&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Sunnyside+Packing+Company&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Sunrise+Growers-Frozsun+Foods&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Taylor+Farms&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=United+Greenhouse,+LLC.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Valores+Horticolas+del+Pacifico+S.A.+de+C.V.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Watsonville+Produce,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Well+Pict+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=West+Lake+Fresh&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))
html.append(scraperwiki.scrape('http://google2.fda.gov/search?client=FDAgov&site=FDAgov-Recalls-Safety&output=xml_no_dtd&proxystylesheet=FDAgov&ie=UTF-8&oe=UTF-8&as_q=Wiers+Farms,+Inc.&num=100&btnG=Search&as_epq=&as_oq=&as_eq=&restrictBox=FDAgov-Recalls-Safety&lr=&as_ft=e&as_filetype=pdf&as_occt=any&as_dt=i&as_sitesearch=&sort='))

for x in html:
    root.append(lxml.html.fromstring(x))

for y in root:
    for el in y.cssselect("p.g a"):
        data = {
            'URL' : el.attrib['href']
        }
        scraperwiki.sqlite.save(unique_keys=['URL'], data=data)

