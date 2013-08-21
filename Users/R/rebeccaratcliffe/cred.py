                                                                     
                                                                     
                                                                     
                                             
import scraperwiki

# Blank Python

# typical URL is http://www.london-gazette.co.uk/id/issues/60112/notices/1568529
# list of URLs collected by scraper at https://scraperwiki.com/scrapers/bankruptcies/
# Downloaded as CSV and codes extracted in Google Docs by using =RIGHT(A2, 7)
# Cycle through a list of those codes, created by using the =JOIN formula in Google Docs

#If you want to understand this scraper - start at the bottom where it says 'base_url'

import scraperwiki
#import urlparse
import lxml.html
from lxml import etree

#TM - set debug on or off
debug = False

# search for a span property by XPath
def search_by_span_attribute(root, attribute, value):
    foundVal = root.xpath("//span[@" + attribute + "='" + value + "']")
    if foundVal:
        if debug:
            print attribute + " " + value + " found with text: " + foundVal[0].text
        return foundVal[0].text
    else:
        if debug:
            print attribute + " not found."
        return ""

# custom search
def search_xpath(root, xpath):
    foundVal = root.xpath(xpath)
    if foundVal:
        if debug:
            print xpath + " returned text: " + foundVal[0].text
        return foundVal[0].text
    else:
        if debug:
            print xpath + " returned no results found."
        return ""

#Create a function called 'scrape_table' which is called in the function 'scrape_page' below
#The 'scrape_page' function also passed the contents of the page to this function as 'root'
def scrape_table(root):
    #Create a new empty record
    record = {}

    record['pubdate'] = search_by_span_attribute(root, "property", "g:hasPublicationDate")
    record['noticecode'] = search_by_span_attribute(root, "property", "g:hasNoticeCode")
    #TM - you'll need to look for an example of this from page source when you come across one that should have it... unless it is the same as court:courtName below?
    #record['registry'] = search_by_span_attribute(root, "property",
    record['company number'] = search_by_span_attribute(root, "property", "organisation:companyNumber")
    record['company name'] = search_by_span_attribute(root, "property", "organisation:name")
    record['nature of business'] = search_by_span_attribute(root, "property", "organisation:natureOfBusiness")
    #record['trade classification'] = search_by_span_attribute(root, "property",
    record['date of appointment'] = search_by_span_attribute(root, "property", "corp-insolvency:dateOfAppointment")
    #TM - this one is a bit special as there are two that match it if you search for just the "vCard:label" property. To guarantee the right one, we have to customize the XPath a bit...
    record['registered office of company'] = search_xpath(root, "//span[@rel='organisation:hasRegisteredOffice']//span[@property='vCard:label']")
    #record['sector'] = search_by_span_attribute(root, "property",
    record['date of appointment'] = search_by_span_attribute(root, "property", "corp-insolvency:dateOfAppointment")
    record['court'] = search_by_span_attribute(root, "property", "court:courtName")
    #record['date'] = search_by_span_attribute(root, "property", #same as date?
    #record['urlcode'] = search_by_span_attribute(root, "property",
    record['ID'] = item

    scraperwiki.sqlite.save(["ID"], record)
       

#this creates a new function and (re)names whatever parameter is passed to it - i.e. 'next_link' below - as 'url'
def scrape_page(url):
    #now 'url' is scraped with the scraperwiki library imported above, and the contents put into a new object, 'html'
    html = scraperwiki.scrape(url)
    #TM - commented out the below print
    #print html
    #now we use the lxml.html function imported above to convert 'html' into a new object, 'root'
    #TM - except we are now using etree!
    #root = lxml.html.fromstring(html)
    root = etree.HTML(html)
    #now we call another function on root, which we write - above
    scrape_table(root)

#START HERE: This is the part of the URL which all our pages share
base_url = 'http://www.london-gazette.co.uk/issues/'

#And these are the numbers which we need to complete that URL to make each individual URL
#This array has been compiled using the =JOIN formula in Google Docs on a column of URL codes
codes =['60149/notices/1593419', '60153/notices/1595954', '60019/notices/1505046', '60022/notices/1505703', '60023/notices/1506909', '60033/notices/1514024', '60036/notices/1516732', '60036/notices/1516733', '60036/notices/1515568', '60036/notices/1515350', '60041/notices/1518786', '60041/notices/1518787', '60049/notices/1522547', '60050/notices/1524772', '60050/notices/1524898', '60051/notices/1525766', '60053/notices/1526434', '60055/notices/1528508', '60057/notices/1531306', '60061/notices/1533579', '60063/notices/1535536', '60063/notices/1535537', '60063/notices/1535538', '60067/notices/1538467', '60067/notices/1538468', '60070/notices/1541194', '60070/notices/1541195', '60070/notices/1541196', '60070/notices/1541197', '60072/notices/1542539', '60073/notices/1543045', '60073/notices/1541507', '60080/notices/1547878', '60081/notices/1547384', '60082/notices/1550207', '60082/notices/1550264', '60087/notices/1553556', '60087/notices/1551722', '60093/notices/1557658', '60097/notices/1559584', '60097/notices/1559585', '60098/notices/1558935', '60098/notices/1560413', '60100/notices/1561314', '60102/notices/1562192', '60102/notices/1562195', '60103/notices/1561442', '60103/notices/1563433', '60103/notices/1561409', '60104/notices/1562417', '60105/notices/1564880', '60109/notices/1567294', '60109/notices/1567296', '60110/notices/1568043', '60110/notices/1565968', '60110/notices/1568044', '60110/notices/1568045', '60112/notices/1569716', '60113/notices/1568264', '60113/notices/1570129', '60113/notices/1568255', '60114/notices/1571025', '60115/notices/1571796', '60115/notices/1570303', '60115/notices/1570336', '60116/notices/1571209', '60116/notices/1571250', '60116/notices/1572722', '60118/notices/1572371', '60119/notices/1573003', '60119/notices/1572982', '60122/notices/1574954', '60122/notices/1576332', '60122/notices/1576333', '60122/notices/1576334', '60124/notices/1576664', '60126/notices/1578110', '60126/notices/1576558', '60128/notices/1579492', '60128/notices/1579493', '60133/notices/1583915', '60135/notices/1585821', '60139/notices/1587591', '60139/notices/1587592', '60140/notices/1586924', '60143/notices/1588698', '60145/notices/1591397', '60145/notices/1591398', '60146/notices/1591617', '60146/notices/1591618', '60146/notices/1590536', '60151/notices/1595784', '60153/notices/1597358', '60153/notices/1595965', '60154/notices/1598236', '60155/notices/1599007', '60157/notices/1600454', '60158/notices/1600994', '60159/notices/1601963', '60019/notices/1505112', '60019/notices/1505047', '60021/notices/1504984', '60021/notices/1504980', '60021/notices/1504987', '60021/notices/1505888', '60021/notices/1505889', '60022/notices/1505637', '60022/notices/1505458', '60022/notices/1505702', '60022/notices/1505672', '60023/notices/1506029', '60024/notices/1507778', '60024/notices/1506831', '60024/notices/1506834', '60024/notices/1507642', '60026/notices/1507020', '60026/notices/1507553', '60027/notices/1508448', '60027/notices/1508450', '60027/notices/1508345', '60027/notices/1508356', '60027/notices/1508363', '60027/notices/1508349', '60027/notices/1507733', '60027/notices/1508335', '60028/notices/1510558', '60028/notices/1509241', '60028/notices/1508591', '60028/notices/1510225', '60028/notices/1510559', '60028/notices/1510560', '60029/notices/1510299', '60029/notices/1510325', '60029/notices/1511493', '60030/notices/1511241', '60030/notices/1510476', '60032/notices/1512148', '60032/notices/1511403', '60032/notices/1512999', '60033/notices/1514025', '60033/notices/1514026', '60033/notices/1512865', '60034/notices/1513914', '60034/notices/1513667', '60034/notices/1513414', '60034/notices/1514629', '60035/notices/1513981', '60035/notices/1513961', '60035/notices/1514714', '60035/notices/1514668', '60036/notices/1515672', '60039/notices/1516619', '60039/notices/1516515', '60039/notices/1516511', '60039/notices/1517569', '60039/notices/1516538', '60039/notices/1516112', '60039/notices/1516548', '60039/notices/1516545', '60039/notices/1516493', '60041/notices/1518788', '60041/notices/1516672', '60041/notices/1516684', '60041/notices/1516656', '60042/notices/1518411', '60042/notices/1519267', '60042/notices/1518426', '60043/notices/1518719', '60043/notices/1519316', '60043/notices/1520448', '60043/notices/1519982', '60044/notices/1520215', '60044/notices/1520965', '60044/notices/1519490', '60047/notices/1520345', '60047/notices/1521914', '60047/notices/1521915', '60047/notices/1521148', '60047/notices/1521916', '60048/notices/1521353', '60049/notices/1522077', '60049/notices/1522384', '60049/notices/1522533', '60050/notices/1524897', '60050/notices/1523670', '60050/notices/1523672', '60050/notices/1523651', '60051/notices/1524245', '60051/notices/1525667', '60053/notices/1525046', '60053/notices/1525431', '60054/notices/1526139', '60054/notices/1526522', '60054/notices/1526130', '60054/notices/1526101', '60054/notices/1525979', '60055/notices/1526855', '60055/notices/1528507', '60055/notices/1526793', '60055/notices/1526787', '60055/notices/1526577', '60055/notices/1526824', '60055/notices/1526311', '60055/notices/1526736', '60056/notices/1528018', '60056/notices/1528629', '60056/notices/1528547', '60056/notices/1527130', '60056/notices/1530627', '60056/notices/1528570', '60057/notices/1529748', '60057/notices/1529767', '60057/notices/1529541', '60057/notices/1529813', '60057/notices/1529759', '60057/notices/1529751', '60057/notices/1529822', '60060/notices/1532382', '60060/notices/1531257', '60060/notices/1530606', '60060/notices/1530195', '60061/notices/1531663', '60061/notices/1531898', '60061/notices/1531664', '60061/notices/1531665', '60062/notices/1533065', '60062/notices/1532555', '60062/notices/1532556', '60062/notices/1533025', '60062/notices/1533936', '60062/notices/1533998', '60062/notices/1533087', '60063/notices/1534500', '60064/notices/1535204', '60064/notices/1535237', '60064/notices/1536467', '60064/notices/1534892', '60064/notices/1535243', '60066/notices/1536417', '60066/notices/1536418', '60066/notices/1537511', '60066/notices/1536253', '60067/notices/1537281', '60067/notices/1537238', '60067/notices/1536777', '60067/notices/1535877', '60067/notices/1537241', '60068/notices/1539478', '60068/notices/1538120', '60068/notices/1538085', '60068/notices/1539479', '60069/notices/1539210', '60069/notices/1539173', '60069/notices/1538353', '60069/notices/1538392', '60069/notices/1539162', '60070/notices/1539836', '60072/notices/1540850', '60072/notices/1540829', '60072/notices/1540927', '60072/notices/1542538', '60072/notices/1540870', '60072/notices/1542540', '60073/notices/1541904', '60073/notices/1541955', '60073/notices/1543312', '60074/notices/1542743', '60074/notices/1543936', '60074/notices/1542816', '60074/notices/1542762', '60076/notices/1544819', '60076/notices/1544733', '60076/notices/1544736', '60079/notices/1545680', '60079/notices/1545690', '60079/notices/1545693', '60079/notices/1545849', '60079/notices/1545636', '60080/notices/1547813', '60080/notices/1546446', '60080/notices/1547879', '60080/notices/1546499', '60080/notices/1546373', '60081/notices/1547396', '60081/notices/1547752', '60081/notices/1548848', '60081/notices/1549006', '60081/notices/1547420', '60081/notices/1548497', '60081/notices/1547034', '60081/notices/1547744', '60081/notices/1547723', '60082/notices/1548899', '60082/notices/1548281', '60082/notices/1548932', '60082/notices/1549778', '60082/notices/1548297', '60082/notices/1548577', '60083/notices/1549638', '60083/notices/1549645', '60083/notices/1550852', '60083/notices/1549165', '60083/notices/1549176', '60083/notices/1551290', '60083/notices/1551291', '60083/notices/1549592', '60083/notices/1549177', '60083/notices/1549527', '60083/notices/1549188', '60083/notices/1549544', '60083/notices/1551302', '60085/notices/1549799', '60085/notices/1551941', '60085/notices/1551942', '60085/notices/1549834', '60085/notices/1550473', '60085/notices/1549877', '60085/notices/1551944', '60086/notices/1549748', '60086/notices/1550771', '60086/notices/1551440', '60086/notices/1551349', '60086/notices/1552395', '60086/notices/1552079', '60086/notices/1553045', '60087/notices/1552632', '60089/notices/1553460', '60089/notices/1553466', '60089/notices/1554775', '60089/notices/1552914', '60089/notices/1553911', '60089/notices/1553089', '60090/notices/1554153', '60090/notices/1553649', '60090/notices/1554206', '60090/notices/1553680', '60092/notices/1556776', '60092/notices/1555822', '60092/notices/1554490', '60092/notices/1555336', '60092/notices/1554486', '60093/notices/1555559', '60093/notices/1555703', '60094/notices/1557222', '60094/notices/1557200', '60094/notices/1557245', '60094/notices/1557133', '60094/notices/1556744', '60094/notices/1558468', '60097/notices/1559582', '60097/notices/1559583', '60097/notices/1557471', '60097/notices/1557477', '60097/notices/1558600', '60097/notices/1558221', '60097/notices/1558165', '60097/notices/1558242', '60097/notices/1557859', '60097/notices/1557860', '60098/notices/1560412', '60098/notices/1559179', '60098/notices/1558961', '60098/notices/1559273', '60098/notices/1559766', '60098/notices/1559807', '60100/notices/1561313', '60100/notices/1559967', '60100/notices/1559463', '60100/notices/1559974', '60102/notices/1561129', '60102/notices/1562193', '60102/notices/1562194', '60102/notices/1561080', '60102/notices/1561133', '60102/notices/1562324', '60103/notices/1563173', '60103/notices/1563430', '60103/notices/1561941', '60103/notices/1563431', '60103/notices/1563432', '60103/notices/1561972', '60103/notices/1561823', '60103/notices/1561841', '60103/notices/1561467', '60104/notices/1562415', '60104/notices/1562416', '60104/notices/1562387', '60104/notices/1562119', '60104/notices/1562388', '60104/notices/1562389', '60104/notices/1562390', '60104/notices/1562396', '60104/notices/1563997', '60105/notices/1563888', '60105/notices/1563922', '60105/notices/1563891', '60105/notices/1563934', '60105/notices/1563884', '60105/notices/1564881', '60105/notices/1563963', '60105/notices/1563973', '60105/notices/1563101', '60108/notices/1564106', '60108/notices/1564109', '60108/notices/1565105', '60108/notices/1564825', '60108/notices/1564602', '60108/notices/1566182', '60108/notices/1564774', '60108/notices/1564777', '60108/notices/1564124', '60108/notices/1564576', '60109/notices/1565735', '60109/notices/1565606', '60109/notices/1565643', '60109/notices/1566260', '60109/notices/1565661', '60109/notices/1565592', '60109/notices/1565688', '60109/notices/1565000', '60109/notices/1567122', '60110/notices/1566379', '60110/notices/1567966', '60110/notices/1567967', '60110/notices/1566355', '60110/notices/1565969', '60110/notices/1566394', '60110/notices/1566388', '60110/notices/1566339', '60110/notices/1565728', '60110/notices/1566349', '60110/notices/1566921', '60110/notices/1565821', '60112/notices/1566961', '60112/notices/1566975', '60112/notices/1567861', '60112/notices/1567724', '60112/notices/1567821', '60112/notices/1566976', '60112/notices/1567735', '60112/notices/1567837', '60112/notices/1566590', '60112/notices/1567817', '60112/notices/1568916', '60112/notices/1566962', '60112/notices/1567858', '60112/notices/1566571', '60112/notices/1566611', '60112/notices/1567834', '60112/notices/1567811', '60112/notices/1566991', '60112/notices/1568898', '60113/notices/1568682', '60113/notices/1568734', '60113/notices/1568790', '60113/notices/1568764', '60113/notices/1569992', '60113/notices/1568645', '60113/notices/1568641', '60113/notices/1568643', '60113/notices/1570128', '60113/notices/1568671', '60113/notices/1568657', '60113/notices/1569978', '60113/notices/1568798', '60113/notices/1569979', '60113/notices/1568719', '60113/notices/1568256', '60113/notices/1568759', '60114/notices/1569909', '60114/notices/1569860', '60114/notices/1571024', '60114/notices/1569233', '60114/notices/1569221', '60114/notices/1569807', '60114/notices/1569798', '60114/notices/1569222', '60114/notices/1570559', '60114/notices/1570205', '60114/notices/1568927', '60114/notices/1568930', '60114/notices/1568976', '60114/notices/1569234', '60114/notices/1569246', '60114/notices/1568969', '60114/notices/1569842', '60115/notices/1571106', '60115/notices/1570875', '60115/notices/1570073', '60115/notices/1571795', '60115/notices/1571107', '60115/notices/1571547', '60115/notices/1570311', '60115/notices/1570790', '60116/notices/1572909', '60116/notices/1571614', '60118/notices/1573766', '60118/notices/1573576', '60118/notices/1571714', '60118/notices/1573767', '60118/notices/1572553', '60118/notices/1571707', '60119/notices/1572651', '60119/notices/1573363', '60119/notices/1573331', '60119/notices/1573287', '60119/notices/1574695', '60119/notices/1573021', '60119/notices/1573357', '60121/notices/1575342', '60121/notices/1574439', '60121/notices/1574100', '60121/notices/1574651', '60122/notices/1574591', '60122/notices/1575263', '60124/notices/1576072', '60124/notices/1576030', '60124/notices/1576663', '60124/notices/1575495', '60124/notices/1575733', '60124/notices/1576003', '60124/notices/1576056', '60126/notices/1576247', '60126/notices/1576962', '60126/notices/1577046', '60126/notices/1577024', '60126/notices/1576965', '60126/notices/1577999', '60126/notices/1577032', '60127/notices/1577782', '60127/notices/1577144', '60127/notices/1577423', '60128/notices/1578243', '60128/notices/1578548', '60128/notices/1578582', '60128/notices/1578656', '60128/notices/1578236', '60129/notices/1579569', '60129/notices/1579361', '60129/notices/1580640', '60129/notices/1578883', '60129/notices/1579607', '60129/notices/1580790', '60130/notices/1580442', '60130/notices/1580464', '60130/notices/1580071', '60130/notices/1581866', '60130/notices/1580493', '60132/notices/1581519', '60132/notices/1581413', '60133/notices/1581709', '60133/notices/1582554', '60133/notices/1581685', '60134/notices/1583449', '60134/notices/1583503', '60134/notices/1583446', '60134/notices/1583464', '60134/notices/1583478', '60134/notices/1583004', '60135/notices/1584089', '60135/notices/1583763', '60135/notices/1585211', '60135/notices/1584490', '60135/notices/1584487', '60138/notices/1585417', '60138/notices/1584771', '60138/notices/1586830', '60138/notices/1586635', '60139/notices/1586121', '60139/notices/1586144', '60139/notices/1586092', '60139/notices/1587492', '60139/notices/1586100', '60139/notices/1585555', '60139/notices/1587624', '60140/notices/1587267', '60140/notices/1588632', '60140/notices/1588429', '60140/notices/1586571', '60140/notices/1586555', '60141/notices/1587969', '60141/notices/1589425', '60141/notices/1588195', '60141/notices/1588115', '60143/notices/1590230', '60143/notices/1590233', '60143/notices/1589661', '60143/notices/1590105', '60143/notices/1589129', '60143/notices/1589020', '60143/notices/1589010', '60143/notices/1589101', '60143/notices/1589106', '60143/notices/1589119', '60145/notices/1590021', '60146/notices/1590892', '60146/notices/1591616', '60146/notices/1590949', '60146/notices/1590860', '60146/notices/1590862', '60146/notices/1590876', '60146/notices/1591619', '60146/notices/1590947', '60146/notices/1592129', '60147/notices/1590998', '60147/notices/1591446', '60147/notices/1591748', '60148/notices/1592907', '60148/notices/1592486', '60148/notices/1594030', '60148/notices/1594031', '60148/notices/1592900', '60148/notices/1592789', '60149/notices/1594710', '60149/notices/1593036', '60151/notices/1593872', '60151/notices/1594602', '60151/notices/1593840', '60151/notices/1595785', '60151/notices/1594586', '60152/notices/1595397', '60152/notices/1595568', '60152/notices/1595424', '60152/notices/1595360', '60153/notices/1596226', '60153/notices/1595585', '60153/notices/1597190', '60153/notices/1595955', '60153/notices/1596236', '60153/notices/1596261', '60153/notices/1596229', '60153/notices/1597468', '60153/notices/1596203', '60153/notices/1596277', '60154/notices/1598044', '60154/notices/1598237', '60154/notices/1596872', '60154/notices/1598146', '60154/notices/1598147', '60154/notices/1596777', '60155/notices/1597941', '60155/notices/1597960', '60155/notices/1597897', '60155/notices/1597976', '60155/notices/1599112', '60155/notices/1597723', '60155/notices/1598009', '60155/notices/1597985', '60157/notices/1600253', '60157/notices/1598969', '60158/notices/1599746', '60158/notices/1599561', '60158/notices/1599676', '60159/notices/1600607', '60159/notices/1600973', '60159/notices/1600661', '60159/notices/1600664', '60019/notices/1505003', '60021/notices/1505919', '60022/notices/1506423', '60022/notices/1505663', '60022/notices/1505659', '60023/notices/1506161', '60023/notices/1505823', '60026/notices/1507561', '60027/notices/1508449', '60027/notices/1507745', '60028/notices/1509204', '60028/notices/1509265', '60028/notices/1508586', '60029/notices/1511555', '60030/notices/1511168', '60030/notices/1511183', '60030/notices/1510032', '60033/notices/1512944', '60034/notices/1514618', '60034/notices/1514619', '60036/notices/1515316', '60039/notices/1515779', '60041/notices/1516708', '60042/notices/1518024', '60042/notices/1517731', '60042/notices/1518396', '60042/notices/1518404', '60043/notices/1519322', '60043/notices/1519360', '60047/notices/1521564', '60049/notices/1522845', '60050/notices/1523717', '60050/notices/1523719', '60050/notices/1523558', '60050/notices/1523559', '60050/notices/1523560', '60050/notices/1523681', '60051/notices/1524617', '60051/notices/1524523', '60051/notices/1524581', '60053/notices/1525421', '60053/notices/1526435', '60054/notices/1526136', '60054/notices/1525539', '60055/notices/1526310', '60055/notices/1528165', '60056/notices/1528605', '60057/notices/1531290', '60060/notices/1530193', '60060/notices/1531186', '60061/notices/1533175', '60061/notices/1532356', '60062/notices/1533077', '60062/notices/1533062', '60062/notices/1532980', '60062/notices/1533053', '60062/notices/1533107', '60063/notices/1534560', '60063/notices/1534544', '60063/notices/1534556', '60064/notices/1535396', '60064/notices/1534864', '60067/notices/1537349', '60067/notices/1537310', '60067/notices/1537265', '60068/notices/1538667', '60068/notices/1538668', '60068/notices/1538066', '60068/notices/1538131', '60070/notices/1539285', '60070/notices/1539787', '60073/notices/1543044', '60073/notices/1541892', '60073/notices/1541890', '60073/notices/1541240', '60074/notices/1543937', '60074/notices/1542729', '60075/notices/1545046', '60079/notices/1545670', '60079/notices/1545747', '60079/notices/1545783', '60080/notices/1546473', '60080/notices/1547814', '60081/notices/1547029', '60081/notices/1547739', '60081/notices/1549007', '60081/notices/1549008', '60082/notices/1548552', '60082/notices/1548569', '60083/notices/1550857', '60083/notices/1550855', '60085/notices/1550458', '60085/notices/1550492', '60085/notices/1551943', '60086/notices/1551462', '60087/notices/1552616', '60089/notices/1553434', '60089/notices/1552867', '60090/notices/1554105', '60093/notices/1556249', '60094/notices/1558299', '60094/notices/1557197', '60094/notices/1558300', '60097/notices/1558230', '60097/notices/1557466', '60097/notices/1558197', '60097/notices/1558203', '60097/notices/1558200', '60102/notices/1560815', '60102/notices/1561004', '60102/notices/1561100', '60102/notices/1560816', '60102/notices/1561096', '60103/notices/1561849', '60104/notices/1562750', '60104/notices/1563996', '60105/notices/1563900', '60105/notices/1563121', '60105/notices/1563109', '60105/notices/1563124', '60105/notices/1563959', '60108/notices/1564798', '60108/notices/1564746', '60108/notices/1564931', '60108/notices/1564838', '60108/notices/1564833', '60109/notices/1564967', '60109/notices/1566473', '60109/notices/1564978', '60110/notices/1567982', '60110/notices/1566903', '60110/notices/1566849', '60110/notices/1566904', '60110/notices/1566905', '60112/notices/1566614', '60112/notices/1566619', '60112/notices/1567794', '60112/notices/1566578', '60112/notices/1567824', '60113/notices/1568637', '60113/notices/1568815', '60113/notices/1568727', '60113/notices/1568660', '60113/notices/1568731', '60113/notices/1568803', '60114/notices/1569845', '60114/notices/1570204', '60114/notices/1570558', '60114/notices/1569912', '60115/notices/1570859', '60115/notices/1570823', '60115/notices/1570787', '60116/notices/1570950', '60118/notices/1573768', '60119/notices/1573234', '60119/notices/1574637', '60121/notices/1574436', '60121/notices/1575246', '60121/notices/1573723', '60124/notices/1575990', '60126/notices/1576240', '60126/notices/1576252', '60128/notices/1579774', '60128/notices/1578551', '60128/notices/1577951', '60128/notices/1578560', '60128/notices/1579775', '60128/notices/1579776', '60128/notices/1578574', '60128/notices/1579662', '60129/notices/1580754', '60130/notices/1581729', '60132/notices/1581444', '60132/notices/1581409', '60132/notices/1581429', '60133/notices/1582647', '60134/notices/1583684', '60134/notices/1583398', '60134/notices/1583982', '60134/notices/1584734', '60135/notices/1583778', '60138/notices/1585441', '60138/notices/1586636', '60139/notices/1586103', '60140/notices/1587424', '60140/notices/1588430', '60140/notices/1588431', '60141/notices/1588165', '60143/notices/1589075', '60143/notices/1589039', '60145/notices/1590047', '60145/notices/1591218', '60147/notices/1591002', '60147/notices/1592964', '60147/notices/1591011', '60148/notices/1592854', '60148/notices/1593888', '60151/notices/1594559', '60151/notices/1594536', '60151/notices/1594605', '60152/notices/1595421', '60152/notices/1595481', '60153/notices/1597467', '60154/notices/1596875', '60154/notices/1598145', '60154/notices/1596401', '60154/notices/1596398', '60155/notices/1599143', '60155/notices/1597881', '60157/notices/1598899', '60157/notices/1599952', '60158/notices/1599586', '60158/notices/1599553', '60158/notices/1599554', '60158/notices/1601063', '60158/notices/1599619', '60158/notices/1599616', '60029/notices/1511583', '60041/notices/1518789', '60056/notices/1528619', '60062/notices/1532979', '60063/notices/1534552', '60097/notices/1558172', '60100/notices/1559959', '60112/notices/1567751', '60113/notices/1569400', '60124/notices/1576032', '60128/notices/1578540', '60143/notices/1589116', '60021/notices/1504991', '60024/notices/1506800', '60043/notices/1520402', '60051/notices/1524584', '60064/notices/1535267', '60081/notices/1548042', '60108/notices/1564922', '60033/notices/1513951', '60080/notices/1545918', '60094/notices/1557117', '60105/notices/1563864']

#go through the schoolIDs array above, and for each ID...
for item in codes:
    #show it in the console
    print item
    #create a URL called 'next_link' which adds that ID to the end of the base_url variable
    next_link = base_url+item
    #pass that new concatenated URL to a function, 'scrape_page', which is scripted above
    scrape_page(next_link)


