import scraperwiki
import requests as req
import lxml.html as lh

# Blank Python

def scrape():
    urls = ["https://github.com/blog/" + str(num) for num in range(1200, 1305)]
    data = []
    for url in urls:
        html = req.get(url, verify=False).content
        root = lh.fromstring(html)
        el = root.cssselect('.entry-content')
        if len(el):
            el = el[0]
            text = el.text_content()
            if 'drink' in text.lower():
                print url
                data.append({'blog': url, 'text': text, 'html': lh.tostring(el)})
    scraperwiki.sqlite.save(unique_keys=['blog'], data=data)


drinks = ['https://github.com/blog/163',
 'https://github.com/blog/196',
 'https://github.com/blog/214',
 'https://github.com/blog/323',
 'https://github.com/blog/452',
 'https://github.com/blog/459',
 'https://github.com/blog/472',
 'https://github.com/blog/476',
 'https://github.com/blog/484',
 'https://github.com/blog/486',
 'https://github.com/blog/487',
 'https://github.com/blog/498',
 'https://github.com/blog/514',
 'https://github.com/blog/532',
 'https://github.com/blog/547',
 'https://github.com/blog/556',
 'https://github.com/blog/557',
 'https://github.com/blog/558',
 'https://github.com/blog/568',
 'https://github.com/blog/576',
 'https://github.com/blog/580',
 'https://github.com/blog/587',
 'https://github.com/blog/594',
 'https://github.com/blog/604',
 'https://github.com/blog/613',
 'https://github.com/blog/625',
 'https://github.com/blog/632',
 'https://github.com/blog/634',
 'https://github.com/blog/635',
 'https://github.com/blog/718',
 'https://github.com/blog/727',
 'https://github.com/blog/728',
 'https://github.com/blog/734',
 'https://github.com/blog/735',
 'https://github.com/blog/756',
 'https://github.com/blog/759',
 'https://github.com/blog/771',
 'https://github.com/blog/777',
 'https://github.com/blog/782',
 'https://github.com/blog/787',
 'https://github.com/blog/790',
 'https://github.com/blog/795',
 'https://github.com/blog/804',
 'https://github.com/blog/813',
 'https://github.com/blog/816',
 'https://github.com/blog/819',
 'https://github.com/blog/822',
 'https://github.com/blog/828',
 'https://github.com/blog/833',
 'https://github.com/blog/845',
 'https://github.com/blog/850',
 'https://github.com/blog/855',
 'https://github.com/blog/860',
 'https://github.com/blog/866',
 'https://github.com/blog/871',
 'https://github.com/blog/885',
 'https://github.com/blog/890',
 'https://github.com/blog/891',
 'https://github.com/blog/903',
 'https://github.com/blog/908',
 'https://github.com/blog/914',
 'https://github.com/blog/916',
 'https://github.com/blog/917',
 'https://github.com/blog/921',
 'https://github.com/blog/922',
 'https://github.com/blog/923',
 'https://github.com/blog/925',
 'https://github.com/blog/930',
 'https://github.com/blog/931',
 'https://github.com/blog/933',
 'https://github.com/blog/935',
 'https://github.com/blog/939',
 'https://github.com/blog/944',
 'https://github.com/blog/950',
 'https://github.com/blog/955',
 'https://github.com/blog/956',
 'https://github.com/blog/960',
 'https://github.com/blog/971',
 'https://github.com/blog/979',
 'https://github.com/blog/982',
 'https://github.com/blog/984',
 'https://github.com/blog/990',
 'https://github.com/blog/1014',
 'https://github.com/blog/1016',
 'https://github.com/blog/1023',
 'https://github.com/blog/1027',
 'https://github.com/blog/1029',
 'https://github.com/blog/1032',
 'https://github.com/blog/1053',
 'https://github.com/blog/1059',
 'https://github.com/blog/1060',
 'https://github.com/blog/1064',
 'https://github.com/blog/1065',
 'https://github.com/blog/1066',
 'https://github.com/blog/1071',
 'https://github.com/blog/1073',
 'https://github.com/blog/1074',
 'https://github.com/blog/1076',
 'https://github.com/blog/1085',
 'https://github.com/blog/1088',
 'https://github.com/blog/1094',
 'https://github.com/blog/1095',
 'https://github.com/blog/1096',
 'https://github.com/blog/1100',
 'https://github.com/blog/1114',
 'https://github.com/blog/1115',
 'https://github.com/blog/1122',
 'https://github.com/blog/1128',
 'https://github.com/blog/1129',
 'https://github.com/blog/1131',
 'https://github.com/blog/1134',
 'https://github.com/blog/1138',
 'https://github.com/blog/1139',
 'https://github.com/blog/1150',
 'https://github.com/blog/1155',
 'https://github.com/blog/1156',
 'https://github.com/blog/1157',
 'https://github.com/blog/1163',
 'https://github.com/blog/1164',
 'https://github.com/blog/1168',
 'https://github.com/blog/1170',
 'https://github.com/blog/1185',
 'https://github.com/blog/1189',
 'https://github.com/blog/1190',
 'https://github.com/blog/1194',
 'https://github.com/blog/1196',
 'https://github.com/blog/1197',
 'https://github.com/blog/1198',
 'https://github.com/blog/1199',
 'https://github.com/blog/1203',
 'https://github.com/blog/1218',
 'https://github.com/blog/1219',
 'https://github.com/blog/1220',
 'https://github.com/blog/1221',
 'https://github.com/blog/1224',
 'https://github.com/blog/1234',
 'https://github.com/blog/1235',
 'https://github.com/blog/1243',
 'https://github.com/blog/1248',
 'https://github.com/blog/1249',
 'https://github.com/blog/1254',
 'https://github.com/blog/1255',
 'https://github.com/blog/1257',
 'https://github.com/blog/1258',
 'https://github.com/blog/1259',
 'https://github.com/blog/1266',
 'https://github.com/blog/1268',
 'https://github.com/blog/1272',
 'https://github.com/blog/1280',
 'https://github.com/blog/1281',
 'https://github.com/blog/1285',
 'https://github.com/blog/1286',
 'https://github.com/blog/1291']


for url in drinks:
    html = req.get(url, verify=False).content
    root = lh.fromstring(html)
    el = root.cssselect('.entry-content')
    title = root.cssselect('.title')[0].text_content().strip()
    if len(el):
        el = el[0]
        text = el.text_content()
        if 'drink' in text.lower():
            print url
            data.append({'blog': url, 'title': title, 'text': text, 'html': lh.tostring(el)})
    scraperwiki.sqlite.save(unique_keys=['blog'], data=data)