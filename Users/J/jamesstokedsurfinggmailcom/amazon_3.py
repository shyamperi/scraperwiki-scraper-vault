import scraperwiki
import lxml.html
import re
import time


amazon_url = ["http://www.amazon.com/Paradise-Coaltion-FLORA-Surfboard-Traction/dp/B008S344PI/ref=sr_1_1?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-1&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-SNAPPER-Surfboard-Traction/dp/B008S33AP8/ref=sr_1_2?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-2&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-ANYWHERE-Surfboard-Traction/dp/B008S2ZFDE/ref=sr_1_3?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-3&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-FLORA-Surfboard-Traction/dp/B008S344HQ/ref=sr_1_4?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-4&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-KNUCKER-Surfboard-Traction/dp/B008S34566/ref=sr_1_5?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-5&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-TRES-Surfboard-Traction/dp/B008S33CGU/ref=sr_1_6?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-6&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-MAC-Surfboard-Traction/dp/B008S339AY/ref=sr_1_7?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-7&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-PAZ-Surfboard-Traction/dp/B008S33A7Q/ref=sr_1_8?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-8&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-Skimboard-Surfboard-Traction/dp/B008S336G6/ref=sr_1_9?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-9&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-ALLIANCE-Surfboard-Traction/dp/B008S2Z5V6/ref=sr_1_10?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-10&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-PAZ-Surfboard-Traction/dp/B008S33AFI/ref=sr_1_11?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-11&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-CORE-Surfboard-Traction/dp/B008S343F4/ref=sr_1_12?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-12&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-Skimboard-Surfboard-Traction/dp/B008S3366Q/ref=sr_1_13?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-13&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-CORE-Surfboard-Traction/dp/B008S343PO/ref=sr_1_14?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-14&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-Skimboard-Surfboard-Traction/dp/B008S33706/ref=sr_1_15?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-15&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-Skimboard-Surfboard-Traction/dp/B008S3377Y/ref=sr_1_16?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-16&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-Skimboard-Surfboard-Traction/dp/B008S345E8/ref=sr_1_17?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-17&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-CORE-Surfboard-Traction/dp/B008S34426/ref=sr_1_18?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-18&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-MAC-Surfboard-Traction/dp/B008S338M8/ref=sr_1_19?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-19&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-SNAPPER-Surfboard-Traction/dp/B008S33B5C/ref=sr_1_20?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-20&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-Skimboard-Surfboard-Traction/dp/B008S336SY/ref=sr_1_21?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-21&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-ANYWHERE-Surfboard-Traction/dp/B008S2ZBKG/ref=sr_1_22?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-22&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-ALLIANCE-Surfboard-Traction/dp/B008S2Z53E/ref=sr_1_23?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-23&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-SNAPPER-Surfboard-Traction/dp/B008S33AXU/ref=sr_1_24?s=sporting-goods&ie=UTF8&qid=1347824572&sr=1-24&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-BOOST-Surfboard-Traction/dp/B008S342GY/ref=sr_1_25?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-25&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-PAZ-Surfboard-Traction/dp/B008S339YK/ref=sr_1_26?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-26&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-BOOST-Surfboard-Traction/dp/B008S3428C/ref=sr_1_27?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-27&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-TRES-Surfboard-Traction/dp/B008S33BFC/ref=sr_1_28?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-28&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-ALLIANCE-Surfboard-Traction/dp/B008S2Z7AU/ref=sr_1_29?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-29&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-BOOST-Surfboard-Traction/dp/B008S342NM/ref=sr_1_30?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-30&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-TRES-Surfboard-Traction/dp/B008S33BPC/ref=sr_1_31?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-31&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-Skimboard-Surfboard-Traction/dp/B008S337LA/ref=sr_1_32?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-32&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-ANYWHERE-Surfboard-Traction/dp/B008S2Z8SG/ref=sr_1_33?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-33&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-MAC-Surfboard-Traction/dp/B008S338VY/ref=sr_1_34?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-34&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-ANYWHERE-Surfboard-Traction/dp/B008S2ZD8G/ref=sr_1_35?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-35&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-Skimboard-Surfboard-Traction/dp/B008S338BY/ref=sr_1_36?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-36&keywords=paradise+coalition","http://www.amazon.com/Paradise-coalition-KNUCKER-Surfboard-Traction/dp/B008S344WQ/ref=sr_1_37?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-37&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-FLORA-Surfboard-Traction/dp/B008S344AS/ref=sr_1_38?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-38&keywords=paradise+coalition","http://www.amazon.com/Paradise-Coaltion-Skimboard-Surfboard-Traction/dp/B008S33832/ref=sr_1_39?s=sporting-goods&ie=UTF8&qid=1347827952&sr=1-39&keywords=paradise+coalition"]

for url in range(0,39):
    html = scraperwiki.scrape(amazon_url[url])
    time.sleep(.2)
    root = lxml.html.fromstring(html)
    entered = "false"
    productname = ""
    rem = ""
    
    for pro in root.cssselect("span#btAsinTitle"):
        productname = pro.text
        
    for el in root.cssselect("div#quantityDropdownDiv select"):
        
        rem = len(el)
        entered = "true"
    
    if entered == "false":
        for x in root.cssselect("span.availGreen"):
            rem = x.text.split("left",1)[0].split("Only",1)[1]

    data = {}
    localtime = time.asctime( time.localtime(time.time()) )
    data['Extracted_Time'] = localtime
    data['Product Name'] = productname
    data['Items Remaining'] = rem
    scraperwiki.sqlite.save(['Extracted_Time'], data)