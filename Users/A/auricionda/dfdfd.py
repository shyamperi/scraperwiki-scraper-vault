import scraperwiki
import lxml.html
a=['http://www.ted.com/profiles/1522598',
'http://www.ted.com/profiles/1521398',
'http://www.ted.com/profiles/1520165',
'http://www.ted.com/profiles/1516355',
'http://www.ted.com/profiles/1516274',
'http://www.ted.com/profiles/1514513',
'http://www.ted.com/profiles/1512202',
'http://www.ted.com/profiles/1511991',
'http://www.ted.com/profiles/1510640',
'http://www.ted.com/profiles/1486484',
'http://www.ted.com/profiles/1483663',
'http://www.ted.com/profiles/1477136',
'http://www.ted.com/profiles/1475463',
'http://www.ted.com/profiles/1474934',
'http://www.ted.com/profiles/1473661',
'http://www.ted.com/profiles/1472569',
'http://www.ted.com/profiles/1463461',
'http://www.ted.com/profiles/1456481',
'http://www.ted.com/profiles/1451222',
'http://www.ted.com/profiles/1442229',
'http://www.ted.com/profiles/1441703',
'http://www.ted.com/profiles/1409214',
'http://www.ted.com/profiles/1404258',
'http://www.ted.com/profiles/1403580',
'http://www.ted.com/profiles/1389900',
'http://www.ted.com/profiles/1389728',
'http://www.ted.com/profiles/1380142',
'http://www.ted.com/profiles/1370786',
'http://www.ted.com/profiles/1366927',
'http://www.ted.com/profiles/1362844',
'http://www.ted.com/profiles/1362733',
'http://www.ted.com/profiles/1360491',
'http://www.ted.com/profiles/1358862',
'http://www.ted.com/profiles/1358789',
'http://www.ted.com/profiles/1357548',
'http://www.ted.com/profiles/1355110',
'http://www.ted.com/profiles/1350051',
'http://www.ted.com/profiles/1344778',
'http://www.ted.com/profiles/1341146',
'http://www.ted.com/profiles/1339286',
'http://www.ted.com/profiles/1339195',
'http://www.ted.com/profiles/1337498',
'http://www.ted.com/profiles/1336932',
'http://www.ted.com/profiles/1332422',
'http://www.ted.com/profiles/1331979',
'http://www.ted.com/profiles/1330727',
'http://www.ted.com/profiles/1325720',
'http://www.ted.com/profiles/1324920',
'http://www.ted.com/profiles/1323159',
'http://www.ted.com/profiles/1321911',
'http://www.ted.com/profiles/1321126',
'http://www.ted.com/profiles/1318302',
'http://www.ted.com/profiles/1315109',
'http://www.ted.com/profiles/1312586',
'http://www.ted.com/profiles/1310886',
'http://www.ted.com/profiles/1310366',
'http://www.ted.com/profiles/1310334',
'http://www.ted.com/profiles/1308054',
'http://www.ted.com/profiles/1300260',
'http://www.ted.com/profiles/1298350',
'http://www.ted.com/profiles/1297227',
'http://www.ted.com/profiles/1290764',
'http://www.ted.com/profiles/1282511',
'http://www.ted.com/profiles/1281306',
'http://www.ted.com/profiles/1271411',
'http://www.ted.com/profiles/1270642',
'http://www.ted.com/profiles/1262356',
'http://www.ted.com/profiles/1260109',
'http://www.ted.com/profiles/1259311',
'http://www.ted.com/profiles/1257985',
'http://www.ted.com/profiles/1251065',
'http://www.ted.com/profiles/1248372',
'http://www.ted.com/profiles/1245827',
'http://www.ted.com/profiles/1244721',
'http://www.ted.com/profiles/1244578',
'http://www.ted.com/profiles/1239440',
'http://www.ted.com/profiles/1239397',
'http://www.ted.com/profiles/1238990',
'http://www.ted.com/profiles/1237484',
'http://www.ted.com/profiles/1234121',
'http://www.ted.com/profiles/1232946',
'http://www.ted.com/profiles/1232245',
'http://www.ted.com/profiles/1231568',
'http://www.ted.com/profiles/1231280',
'http://www.ted.com/profiles/1227039',
'http://www.ted.com/profiles/1224843',
'http://www.ted.com/profiles/1220473',
'http://www.ted.com/profiles/1218813',
'http://www.ted.com/profiles/1217374',
'http://www.ted.com/profiles/1217070',
'http://www.ted.com/profiles/1217033',
'http://www.ted.com/profiles/1215150',
'http://www.ted.com/profiles/1210864',
'http://www.ted.com/profiles/1210606',
'http://www.ted.com/profiles/1202519',
'http://www.ted.com/profiles/1202048',
'http://www.ted.com/profiles/1201257',
'http://www.ted.com/profiles/1200861',
'http://www.ted.com/profiles/1199578',
'http://www.ted.com/profiles/1199517',
'http://www.ted.com/profiles/1199254',
'http://www.ted.com/profiles/1197754',
'http://www.ted.com/profiles/1195486',
'http://www.ted.com/profiles/1188709',
'http://www.ted.com/profiles/1188230',
'http://www.ted.com/profiles/1187194',
'http://www.ted.com/profiles/1186982',
'http://www.ted.com/profiles/1186470',
'http://www.ted.com/profiles/1186456',
'http://www.ted.com/profiles/1185461',
'http://www.ted.com/profiles/1184990',
'http://www.ted.com/profiles/1180007',
'http://www.ted.com/profiles/1173725',
'http://www.ted.com/profiles/1167361',
'http://www.ted.com/profiles/1163347',
'http://www.ted.com/profiles/1158770',
'http://www.ted.com/profiles/1158040',
'http://www.ted.com/profiles/1155243',
'http://www.ted.com/profiles/1152624',
'http://www.ted.com/profiles/1151889',
'http://www.ted.com/profiles/1150048',
'http://www.ted.com/profiles/1148013',
'http://www.ted.com/profiles/1147506',
'http://www.ted.com/profiles/1142816',
'http://www.ted.com/profiles/1141214',
'http://www.ted.com/profiles/1136348',
'http://www.ted.com/profiles/1133150',
'http://www.ted.com/profiles/1125730',
'http://www.ted.com/profiles/1114442',
'http://www.ted.com/profiles/1113698',
'http://www.ted.com/profiles/1110096',
'http://www.ted.com/profiles/1108643',
'http://www.ted.com/profiles/1105818',
'http://www.ted.com/profiles/1102846',
'http://www.ted.com/profiles/1102434',
'http://www.ted.com/profiles/1101366',
'http://www.ted.com/profiles/1101026',
'http://www.ted.com/profiles/1091136',
'http://www.ted.com/profiles/1083384',
'http://www.ted.com/profiles/1078412',
'http://www.ted.com/profiles/1076214',
'http://www.ted.com/profiles/1073520',
'http://www.ted.com/profiles/1067194',
'http://www.ted.com/profiles/1065005',
'http://www.ted.com/profiles/1054545',
'http://www.ted.com/profiles/1050674',
'http://www.ted.com/profiles/1043506',
'http://www.ted.com/profiles/1039868',
'http://www.ted.com/profiles/1039651',
'http://www.ted.com/profiles/1037912',
'http://www.ted.com/profiles/1024430',
'http://www.ted.com/profiles/1020391',
'http://www.ted.com/profiles/1014407',
'http://www.ted.com/profiles/1013702',
'http://www.ted.com/profiles/1010708',
'http://www.ted.com/profiles/1010556',
'http://www.ted.com/profiles/1009079',
'http://www.ted.com/profiles/1004615',
'http://www.ted.com/profiles/1004316',
'http://www.ted.com/profiles/1004103',
'http://www.ted.com/profiles/1004102',
'http://www.ted.com/profiles/999308',
'http://www.ted.com/profiles/993102',
'http://www.ted.com/profiles/989042',
'http://www.ted.com/profiles/988811',
'http://www.ted.com/profiles/988440',
'http://www.ted.com/profiles/987969',
'http://www.ted.com/profiles/987823',
'http://www.ted.com/profiles/985850',
'http://www.ted.com/profiles/984837',
'http://www.ted.com/profiles/983523',
'http://www.ted.com/profiles/983081',
'http://www.ted.com/profiles/975135',
'http://www.ted.com/profiles/973794',
'http://www.ted.com/profiles/972967',
'http://www.ted.com/profiles/961329',
'http://www.ted.com/profiles/959982',
'http://www.ted.com/profiles/959875',
'http://www.ted.com/profiles/956995',
'http://www.ted.com/profiles/955597',
'http://www.ted.com/profiles/952983',
'http://www.ted.com/profiles/946658',
'http://www.ted.com/profiles/943715',
'http://www.ted.com/profiles/942190',
'http://www.ted.com/profiles/934281',
'http://www.ted.com/profiles/933785',
'http://www.ted.com/profiles/931430',
'http://www.ted.com/profiles/928648',
'http://www.ted.com/profiles/923668',
'http://www.ted.com/profiles/922444',
'http://www.ted.com/profiles/922234',
'http://www.ted.com/profiles/922034',
'http://www.ted.com/profiles/918376',
'http://www.ted.com/profiles/918128',
'http://www.ted.com/profiles/916627',
'http://www.ted.com/profiles/913188',
'http://www.ted.com/profiles/912640',
'http://www.ted.com/profiles/906792',
'http://www.ted.com/profiles/906681',
'http://www.ted.com/profiles/904627',
'http://www.ted.com/profiles/903386',
'http://www.ted.com/profiles/902481',
'http://www.ted.com/profiles/902341',
'http://www.ted.com/profiles/902205',
'http://www.ted.com/profiles/901288',
'http://www.ted.com/profiles/900857',
'http://www.ted.com/profiles/899868',
'http://www.ted.com/profiles/899845',
'http://www.ted.com/profiles/898831',
'http://www.ted.com/profiles/898357',
'http://www.ted.com/profiles/897466',
'http://www.ted.com/profiles/896779',
'http://www.ted.com/profiles/884720',
'http://www.ted.com/profiles/882779',
'http://www.ted.com/profiles/882448',
'http://www.ted.com/profiles/882399',
'http://www.ted.com/profiles/880563',
'http://www.ted.com/profiles/880337',
'http://www.ted.com/profiles/880271',
'http://www.ted.com/profiles/880244',
'http://www.ted.com/profiles/880141',
'http://www.ted.com/profiles/879821',
'http://www.ted.com/profiles/879181',
'http://www.ted.com/profiles/879138',
'http://www.ted.com/profiles/879067',
'http://www.ted.com/profiles/878745',
'http://www.ted.com/profiles/878518',
'http://www.ted.com/profiles/877621',
'http://www.ted.com/profiles/876266',
'http://www.ted.com/profiles/875163',
'http://www.ted.com/profiles/874723',
'http://www.ted.com/profiles/873998',
'http://www.ted.com/profiles/873383',
'http://www.ted.com/profiles/873260',
'http://www.ted.com/profiles/873103',
'http://www.ted.com/profiles/872756',
'http://www.ted.com/profiles/872361',
'http://www.ted.com/profiles/871756',
'http://www.ted.com/profiles/871595',
'http://www.ted.com/profiles/870133',
'http://www.ted.com/profiles/869933',
'http://www.ted.com/profiles/869031',
'http://www.ted.com/profiles/867928',
'http://www.ted.com/profiles/867921',
'http://www.ted.com/profiles/867001',
'http://www.ted.com/profiles/866659',
'http://www.ted.com/profiles/864909',
'http://www.ted.com/profiles/864702',
'http://www.ted.com/profiles/863991',
'http://www.ted.com/profiles/863459',
'http://www.ted.com/profiles/863373',
'http://www.ted.com/profiles/863363',
'http://www.ted.com/profiles/862684',
'http://www.ted.com/profiles/861828',
'http://www.ted.com/profiles/861341',
'http://www.ted.com/profiles/861340',
'http://www.ted.com/profiles/861280',
'http://www.ted.com/profiles/861200',
'http://www.ted.com/profiles/860876',
'http://www.ted.com/profiles/860714',
'http://www.ted.com/profiles/860643',
'http://www.ted.com/profiles/860418',
'http://www.ted.com/profiles/860246',
'http://www.ted.com/profiles/860121',
'http://www.ted.com/profiles/860005',
'http://www.ted.com/profiles/859284',
'http://www.ted.com/profiles/859228',
'http://www.ted.com/profiles/858939',
'http://www.ted.com/profiles/858347',
'http://www.ted.com/profiles/857980',
'http://www.ted.com/profiles/857801',
'http://www.ted.com/profiles/857620',
'http://www.ted.com/profiles/857581',
'http://www.ted.com/profiles/857564',
'http://www.ted.com/profiles/857307',
'http://www.ted.com/profiles/856972',
'http://www.ted.com/profiles/855874',
'http://www.ted.com/profiles/855539',
'http://www.ted.com/profiles/855130',
'http://www.ted.com/profiles/854308',
'http://www.ted.com/profiles/853959',
'http://www.ted.com/profiles/853949',
'http://www.ted.com/profiles/852733',
'http://www.ted.com/profiles/852390',
'http://www.ted.com/profiles/851867',
'http://www.ted.com/profiles/851702',
'http://www.ted.com/profiles/851359',
'http://www.ted.com/profiles/851334',
'http://www.ted.com/profiles/851092',
'http://www.ted.com/profiles/850565',
'http://www.ted.com/profiles/850449',
'http://www.ted.com/profiles/850383',
'http://www.ted.com/profiles/850213',
'http://www.ted.com/profiles/849745',
'http://www.ted.com/profiles/849559',
'http://www.ted.com/profiles/849082',
'http://www.ted.com/profiles/848925',
'http://www.ted.com/profiles/848864',
'http://www.ted.com/profiles/848859',
'http://www.ted.com/profiles/848572',
'http://www.ted.com/profiles/848503',
'http://www.ted.com/profiles/848206',
'http://www.ted.com/profiles/847792',
'http://www.ted.com/profiles/847181',
'http://www.ted.com/profiles/847141',
'http://www.ted.com/profiles/846823',
'http://www.ted.com/profiles/846584',
'http://www.ted.com/profiles/846539',
'http://www.ted.com/profiles/846197',
'http://www.ted.com/profiles/846035',
'http://www.ted.com/profiles/845542',
'http://www.ted.com/profiles/845454',
'http://www.ted.com/profiles/845311',
'http://www.ted.com/profiles/844051',
'http://www.ted.com/profiles/842471',
'http://www.ted.com/profiles/842284',
'http://www.ted.com/profiles/841242',
'http://www.ted.com/profiles/840993',
'http://www.ted.com/profiles/840634',
'http://www.ted.com/profiles/840496',
'http://www.ted.com/profiles/840390',
'http://www.ted.com/profiles/840212',
'http://www.ted.com/profiles/839599',
'http://www.ted.com/profiles/839449',
'http://www.ted.com/profiles/839015',
'http://www.ted.com/profiles/838908',
'http://www.ted.com/profiles/838373',
'http://www.ted.com/profiles/837924',
'http://www.ted.com/profiles/837479',
'http://www.ted.com/profiles/836859',
'http://www.ted.com/profiles/836759',
'http://www.ted.com/profiles/836477',
'http://www.ted.com/profiles/836367',
'http://www.ted.com/profiles/836140',
'http://www.ted.com/profiles/834504',
'http://www.ted.com/profiles/832734',
'http://www.ted.com/profiles/832690',
'http://www.ted.com/profiles/832216',
'http://www.ted.com/profiles/831545',
'http://www.ted.com/profiles/831336',
'http://www.ted.com/profiles/830846',
'http://www.ted.com/profiles/830621',
'http://www.ted.com/profiles/830584',
'http://www.ted.com/profiles/830497',
'http://www.ted.com/profiles/830457',
'http://www.ted.com/profiles/830229',
'http://www.ted.com/profiles/829129',
'http://www.ted.com/profiles/829042',
'http://www.ted.com/profiles/828950',
'http://www.ted.com/profiles/826866',
'http://www.ted.com/profiles/826780',
'http://www.ted.com/profiles/823860',
'http://www.ted.com/profiles/822665',
'http://www.ted.com/profiles/822563',
'http://www.ted.com/profiles/822518',
'http://www.ted.com/profiles/821990',
'http://www.ted.com/profiles/821932',
'http://www.ted.com/profiles/821142',
'http://www.ted.com/profiles/820594',
'http://www.ted.com/profiles/820255',
'http://www.ted.com/profiles/819909',
'http://www.ted.com/profiles/819626',
'http://www.ted.com/profiles/819543',
'http://www.ted.com/profiles/819493',
'http://www.ted.com/profiles/818541',
'http://www.ted.com/profiles/818170',
'http://www.ted.com/profiles/818089',
'http://www.ted.com/profiles/817332',
'http://www.ted.com/profiles/817184',
'http://www.ted.com/profiles/817039',
'http://www.ted.com/profiles/816261',
'http://www.ted.com/profiles/815396',
'http://www.ted.com/profiles/813146',
'http://www.ted.com/profiles/812693',
'http://www.ted.com/profiles/811443',
'http://www.ted.com/profiles/811425',
'http://www.ted.com/profiles/811368',
'http://www.ted.com/profiles/809815',
'http://www.ted.com/profiles/809297',
'http://www.ted.com/profiles/809264',
'http://www.ted.com/profiles/809240',
'http://www.ted.com/profiles/809228',
'http://www.ted.com/profiles/809194',
'http://www.ted.com/profiles/809174',
'http://www.ted.com/profiles/809159',
'http://www.ted.com/profiles/809146',
'http://www.ted.com/profiles/809125',
'http://www.ted.com/profiles/809101',
'http://www.ted.com/profiles/809093',
'http://www.ted.com/profiles/809022',
'http://www.ted.com/profiles/809003',
'http://www.ted.com/profiles/808983',
'http://www.ted.com/profiles/808981',
'http://www.ted.com/profiles/808962',
'http://www.ted.com/profiles/808944',
'http://www.ted.com/profiles/808924',
'http://www.ted.com/profiles/808893',
'http://www.ted.com/profiles/808337',
'http://www.ted.com/profiles/807789',
'http://www.ted.com/profiles/807665',
'http://www.ted.com/profiles/806808',
'http://www.ted.com/profiles/806546',
'http://www.ted.com/profiles/805396',
'http://www.ted.com/profiles/804701',
'http://www.ted.com/profiles/803866',
'http://www.ted.com/profiles/803601',
'http://www.ted.com/profiles/803445',
'http://www.ted.com/profiles/803291',
'http://www.ted.com/profiles/801949',
'http://www.ted.com/profiles/801887',
'http://www.ted.com/profiles/801769',
'http://www.ted.com/profiles/801642',
'http://www.ted.com/profiles/801484',
'http://www.ted.com/profiles/800942',
'http://www.ted.com/profiles/799639',
'http://www.ted.com/profiles/799403',
'http://www.ted.com/profiles/798838',
'http://www.ted.com/profiles/798797',
'http://www.ted.com/profiles/798746',
'http://www.ted.com/profiles/798112',
'http://www.ted.com/profiles/797217',
'http://www.ted.com/profiles/796921',
'http://www.ted.com/profiles/796908',
'http://www.ted.com/profiles/796405',
'http://www.ted.com/profiles/796109',
'http://www.ted.com/profiles/794863',
'http://www.ted.com/profiles/794750',
'http://www.ted.com/profiles/793799',
'http://www.ted.com/profiles/792740',
'http://www.ted.com/profiles/792280',
'http://www.ted.com/profiles/791838',
'http://www.ted.com/profiles/790018',
'http://www.ted.com/profiles/788600',
'http://www.ted.com/profiles/788404',
'http://www.ted.com/profiles/788163',
'http://www.ted.com/profiles/787849',
'http://www.ted.com/profiles/787808',
'http://www.ted.com/profiles/787328',
'http://www.ted.com/profiles/787305',
'http://www.ted.com/profiles/786878',
'http://www.ted.com/profiles/784823',
'http://www.ted.com/profiles/784385',
'http://www.ted.com/profiles/784379',
'http://www.ted.com/profiles/784366',
'http://www.ted.com/profiles/784356',
'http://www.ted.com/profiles/784345',
'http://www.ted.com/profiles/784332',
'http://www.ted.com/profiles/784242',
'http://www.ted.com/profiles/784013',
'http://www.ted.com/profiles/783725',
'http://www.ted.com/profiles/783372',
'http://www.ted.com/profiles/782356',
'http://www.ted.com/profiles/781977',
'http://www.ted.com/profiles/781729',
'http://www.ted.com/profiles/781324',
'http://www.ted.com/profiles/781265',
'http://www.ted.com/profiles/780323',
'http://www.ted.com/profiles/779287',
'http://www.ted.com/profiles/778743',
'http://www.ted.com/profiles/778040',
'http://www.ted.com/profiles/777181',
'http://www.ted.com/profiles/777122',
'http://www.ted.com/profiles/776482',
'http://www.ted.com/profiles/775085',
'http://www.ted.com/profiles/773282',
'http://www.ted.com/profiles/772829',
'http://www.ted.com/profiles/772428',
'http://www.ted.com/profiles/770608',
'http://www.ted.com/profiles/769283',
'http://www.ted.com/profiles/766669',
'http://www.ted.com/profiles/766587',
'http://www.ted.com/profiles/766005',
'http://www.ted.com/profiles/764849',
'http://www.ted.com/profiles/764793',
'http://www.ted.com/profiles/763533',
'http://www.ted.com/profiles/763070',
'http://www.ted.com/profiles/762935',
'http://www.ted.com/profiles/762353',
'http://www.ted.com/profiles/761596',
'http://www.ted.com/profiles/761189',
'http://www.ted.com/profiles/761137',
'http://www.ted.com/profiles/759061',
'http://www.ted.com/profiles/757676',
'http://www.ted.com/profiles/756458',
'http://www.ted.com/profiles/756373',
'http://www.ted.com/profiles/755416',
'http://www.ted.com/profiles/755297',
'http://www.ted.com/profiles/754866',
'http://www.ted.com/profiles/753877',
'http://www.ted.com/profiles/753070',
'http://www.ted.com/profiles/753018',
'http://www.ted.com/profiles/752503',
'http://www.ted.com/profiles/752218',
'http://www.ted.com/profiles/751923',
'http://www.ted.com/profiles/751879',
'http://www.ted.com/profiles/751705',
'http://www.ted.com/profiles/751122',
'http://www.ted.com/profiles/751079',
'http://www.ted.com/profiles/750439',
'http://www.ted.com/profiles/750164',
'http://www.ted.com/profiles/749488',
'http://www.ted.com/profiles/749080',
'http://www.ted.com/profiles/748841',
'http://www.ted.com/profiles/748839',
'http://www.ted.com/profiles/748808',
'http://www.ted.com/profiles/748486',
'http://www.ted.com/profiles/747956',
'http://www.ted.com/profiles/747947',
'http://www.ted.com/profiles/747805',
'http://www.ted.com/profiles/746337',
'http://www.ted.com/profiles/745909',
'http://www.ted.com/profiles/745137',
'http://www.ted.com/profiles/744553',
'http://www.ted.com/profiles/743254',
'http://www.ted.com/profiles/742954',
'http://www.ted.com/profiles/741603',
'http://www.ted.com/profiles/741574',
'http://www.ted.com/profiles/741412',
'http://www.ted.com/profiles/740966',
'http://www.ted.com/profiles/739359',
'http://www.ted.com/profiles/739018',
'http://www.ted.com/profiles/737382',
'http://www.ted.com/profiles/737178',
'http://www.ted.com/profiles/736427',
'http://www.ted.com/profiles/736174',
'http://www.ted.com/profiles/735552',
'http://www.ted.com/profiles/735507',
'http://www.ted.com/profiles/735099',
'http://www.ted.com/profiles/734853',
'http://www.ted.com/profiles/733818',
'http://www.ted.com/profiles/733771',
'http://www.ted.com/profiles/733504',
'http://www.ted.com/profiles/732895',
'http://www.ted.com/profiles/732825',
'http://www.ted.com/profiles/732795',
'http://www.ted.com/profiles/732507',
'http://www.ted.com/profiles/732501',
'http://www.ted.com/profiles/732401',
'http://www.ted.com/profiles/732324',
'http://www.ted.com/profiles/731913',
'http://www.ted.com/profiles/731579',
'http://www.ted.com/profiles/731122',
'http://www.ted.com/profiles/730992',
'http://www.ted.com/profiles/730929',
'http://www.ted.com/profiles/730464',
'http://www.ted.com/profiles/730029',
'http://www.ted.com/profiles/729649',
'http://www.ted.com/profiles/729333',
'http://www.ted.com/profiles/729319',
'http://www.ted.com/profiles/728933',
'http://www.ted.com/profiles/728882',
'http://www.ted.com/profiles/728075',
'http://www.ted.com/profiles/727975',
'http://www.ted.com/profiles/727526',
'http://www.ted.com/profiles/727458',
'http://www.ted.com/profiles/725358',
'http://www.ted.com/profiles/724906',
'http://www.ted.com/profiles/724725',
'http://www.ted.com/profiles/724387',
'http://www.ted.com/profiles/723791',
'http://www.ted.com/profiles/723606',
'http://www.ted.com/profiles/723601',
'http://www.ted.com/profiles/719826',
'http://www.ted.com/profiles/719390',
'http://www.ted.com/profiles/713742',
'http://www.ted.com/profiles/704920',
'http://www.ted.com/profiles/704729',
'http://www.ted.com/profiles/703893',
'http://www.ted.com/profiles/703265',
'http://www.ted.com/profiles/701518',
'http://www.ted.com/profiles/699850',
'http://www.ted.com/profiles/699372',
'http://www.ted.com/profiles/698887',
'http://www.ted.com/profiles/697262',
'http://www.ted.com/profiles/697260',
'http://www.ted.com/profiles/696474',
'http://www.ted.com/profiles/695867',
'http://www.ted.com/profiles/695858',
'http://www.ted.com/profiles/695049',
'http://www.ted.com/profiles/694713',
'http://www.ted.com/profiles/694050',
'http://www.ted.com/profiles/693726',
'http://www.ted.com/profiles/693120',
'http://www.ted.com/profiles/693087',
'http://www.ted.com/profiles/693068',
'http://www.ted.com/profiles/692903',
'http://www.ted.com/profiles/692418',
'http://www.ted.com/profiles/691446',
'http://www.ted.com/profiles/689616',
'http://www.ted.com/profiles/689525',
'http://www.ted.com/profiles/688786',
'http://www.ted.com/profiles/688025',
'http://www.ted.com/profiles/686517',
'http://www.ted.com/profiles/686263',
'http://www.ted.com/profiles/685945',
'http://www.ted.com/profiles/684109',
'http://www.ted.com/profiles/683760',
'http://www.ted.com/profiles/682948',
'http://www.ted.com/profiles/682765',
'http://www.ted.com/profiles/682750',
'http://www.ted.com/profiles/680119',
'http://www.ted.com/profiles/680061',
'http://www.ted.com/profiles/679220',
'http://www.ted.com/profiles/678960',
'http://www.ted.com/profiles/678770',
'http://www.ted.com/profiles/678673',
'http://www.ted.com/profiles/678443',
'http://www.ted.com/profiles/678400',
'http://www.ted.com/profiles/678074',
'http://www.ted.com/profiles/677985',
'http://www.ted.com/profiles/677516',
'http://www.ted.com/profiles/677360',
'http://www.ted.com/profiles/677348',
'http://www.ted.com/profiles/677266',
'http://www.ted.com/profiles/676363',
'http://www.ted.com/profiles/676299',
'http://www.ted.com/profiles/676113',
'http://www.ted.com/profiles/674674',
'http://www.ted.com/profiles/674304',
'http://www.ted.com/profiles/673456',
'http://www.ted.com/profiles/673444',
'http://www.ted.com/profiles/672973',
'http://www.ted.com/profiles/672413',
'http://www.ted.com/profiles/672393',
'http://www.ted.com/profiles/672194',
'http://www.ted.com/profiles/671824',
'http://www.ted.com/profiles/671750',
'http://www.ted.com/profiles/671598',
'http://www.ted.com/profiles/670868',
'http://www.ted.com/profiles/670699',
'http://www.ted.com/profiles/670550',
'http://www.ted.com/profiles/670317',
'http://www.ted.com/profiles/669645',
'http://www.ted.com/profiles/668719',
'http://www.ted.com/profiles/667318',
'http://www.ted.com/profiles/667232',
'http://www.ted.com/profiles/666850',
'http://www.ted.com/profiles/666421',
'http://www.ted.com/profiles/666379',
'http://www.ted.com/profiles/666090',
'http://www.ted.com/profiles/665463',
'http://www.ted.com/profiles/664967',
'http://www.ted.com/profiles/664564',
'http://www.ted.com/profiles/664542',
'http://www.ted.com/profiles/663939',
'http://www.ted.com/profiles/663580',
'http://www.ted.com/profiles/662553',
'http://www.ted.com/profiles/662531',
'http://www.ted.com/profiles/662113',
'http://www.ted.com/profiles/660434',
'http://www.ted.com/profiles/660214',
'http://www.ted.com/profiles/659785',
'http://www.ted.com/profiles/659513',
'http://www.ted.com/profiles/657882',
'http://www.ted.com/profiles/657660',
'http://www.ted.com/profiles/657646',
'http://www.ted.com/profiles/656829',
'http://www.ted.com/profiles/656400',
'http://www.ted.com/profiles/655813',
'http://www.ted.com/profiles/655643',
'http://www.ted.com/profiles/655319',
'http://www.ted.com/profiles/655191',
'http://www.ted.com/profiles/654766',
'http://www.ted.com/profiles/654618',
'http://www.ted.com/profiles/653862',
'http://www.ted.com/profiles/653566',
'http://www.ted.com/profiles/652214',
'http://www.ted.com/profiles/652169',
'http://www.ted.com/profiles/652166',
'http://www.ted.com/profiles/652108',
'http://www.ted.com/profiles/652074',
'http://www.ted.com/profiles/651828',
'http://www.ted.com/profiles/649936',
'http://www.ted.com/profiles/649387',
'http://www.ted.com/profiles/649259',
'http://www.ted.com/profiles/647932',
'http://www.ted.com/profiles/647673',
'http://www.ted.com/profiles/647512',
'http://www.ted.com/profiles/647061',
'http://www.ted.com/profiles/647046',
'http://www.ted.com/profiles/646933',
'http://www.ted.com/profiles/646476',
'http://www.ted.com/profiles/645821',
'http://www.ted.com/profiles/645518',
'http://www.ted.com/profiles/645202',
'http://www.ted.com/profiles/644685',
'http://www.ted.com/profiles/644415',
'http://www.ted.com/profiles/644126',
'http://www.ted.com/profiles/644121',
'http://www.ted.com/profiles/644095',
'http://www.ted.com/profiles/643767',
'http://www.ted.com/profiles/643737',
'http://www.ted.com/profiles/643324',
'http://www.ted.com/profiles/643276',
'http://www.ted.com/profiles/642858',
'http://www.ted.com/profiles/642809',
'http://www.ted.com/profiles/642521',
'http://www.ted.com/profiles/641798',
'http://www.ted.com/profiles/640177',
'http://www.ted.com/profiles/637822',
'http://www.ted.com/profiles/637637',
'http://www.ted.com/profiles/636924',
'http://www.ted.com/profiles/635944',
'http://www.ted.com/profiles/635544',
'http://www.ted.com/profiles/635279',
'http://www.ted.com/profiles/634563',
'http://www.ted.com/profiles/633584',
'http://www.ted.com/profiles/633363',
'http://www.ted.com/profiles/632390',
'http://www.ted.com/profiles/632318',
'http://www.ted.com/profiles/632244',
'http://www.ted.com/profiles/631199',
'http://www.ted.com/profiles/630762',
'http://www.ted.com/profiles/630666',
'http://www.ted.com/profiles/630448',
'http://www.ted.com/profiles/630246',
'http://www.ted.com/profiles/630047',
'http://www.ted.com/profiles/629430',
'http://www.ted.com/profiles/629354',
'http://www.ted.com/profiles/629080',
'http://www.ted.com/profiles/628680',
'http://www.ted.com/profiles/628061',
'http://www.ted.com/profiles/628028',
'http://www.ted.com/profiles/627987',
'http://www.ted.com/profiles/626762',
'http://www.ted.com/profiles/626644',
'http://www.ted.com/profiles/626435',
'http://www.ted.com/profiles/626293',
'http://www.ted.com/profiles/625682',
'http://www.ted.com/profiles/625521',
'http://www.ted.com/profiles/623998',
'http://www.ted.com/profiles/623873',
'http://www.ted.com/profiles/623756',
'http://www.ted.com/profiles/623348',
'http://www.ted.com/profiles/622584',
'http://www.ted.com/profiles/622548',
'http://www.ted.com/profiles/621796',
'http://www.ted.com/profiles/621737',
'http://www.ted.com/profiles/621496',
'http://www.ted.com/profiles/621353',
'http://www.ted.com/profiles/620751',
'http://www.ted.com/profiles/620404',
'http://www.ted.com/profiles/619100',
'http://www.ted.com/profiles/618332',
'http://www.ted.com/profiles/617694',
'http://www.ted.com/profiles/616609',
'http://www.ted.com/profiles/616101',
'http://www.ted.com/profiles/616025',
'http://www.ted.com/profiles/615877',
'http://www.ted.com/profiles/615335',
'http://www.ted.com/profiles/615151',
'http://www.ted.com/profiles/615091',
'http://www.ted.com/profiles/614631',
'http://www.ted.com/profiles/614494',
'http://www.ted.com/profiles/614350',
'http://www.ted.com/profiles/614118',
'http://www.ted.com/profiles/612993',
'http://www.ted.com/profiles/612484',
'http://www.ted.com/profiles/612251',
'http://www.ted.com/profiles/611968',
'http://www.ted.com/profiles/611468',
'http://www.ted.com/profiles/611227',
'http://www.ted.com/profiles/611204',
'http://www.ted.com/profiles/611116',
'http://www.ted.com/profiles/610497',
'http://www.ted.com/profiles/610377',
'http://www.ted.com/profiles/609706',
'http://www.ted.com/profiles/608514',
'http://www.ted.com/profiles/608205',
'http://www.ted.com/profiles/608153',
'http://www.ted.com/profiles/607609',
'http://www.ted.com/profiles/607442',
'http://www.ted.com/profiles/607178',
'http://www.ted.com/profiles/606721',
'http://www.ted.com/profiles/606289',
'http://www.ted.com/profiles/606232',
'http://www.ted.com/profiles/605938',
'http://www.ted.com/profiles/605932',
'http://www.ted.com/profiles/605853',
'http://www.ted.com/profiles/605382',
'http://www.ted.com/profiles/604886',
'http://www.ted.com/profiles/604600',
'http://www.ted.com/profiles/604434',
'http://www.ted.com/profiles/604359',
'http://www.ted.com/profiles/604219',
'http://www.ted.com/profiles/604098',
'http://www.ted.com/profiles/603508',
'http://www.ted.com/profiles/603038',
'http://www.ted.com/profiles/602365',
'http://www.ted.com/profiles/601778',
'http://www.ted.com/profiles/601328',
'http://www.ted.com/profiles/601299',
'http://www.ted.com/profiles/601068',
'http://www.ted.com/profiles/600439',
'http://www.ted.com/profiles/600188',
'http://www.ted.com/profiles/599837',
'http://www.ted.com/profiles/598746',
'http://www.ted.com/profiles/598304',
'http://www.ted.com/profiles/597715',
'http://www.ted.com/profiles/596435',
'http://www.ted.com/profiles/596425',
'http://www.ted.com/profiles/596365',
'http://www.ted.com/profiles/595683',
'http://www.ted.com/profiles/595662',
'http://www.ted.com/profiles/594678',
'http://www.ted.com/profiles/594641',
'http://www.ted.com/profiles/593918',
'http://www.ted.com/profiles/593757',
'http://www.ted.com/profiles/593330',
'http://www.ted.com/profiles/592792',
'http://www.ted.com/profiles/592396',
'http://www.ted.com/profiles/592111',
'http://www.ted.com/profiles/591783',
'http://www.ted.com/profiles/591282',
'http://www.ted.com/profiles/590964',
'http://www.ted.com/profiles/590859',
'http://www.ted.com/profiles/590641',
'http://www.ted.com/profiles/590400',
'http://www.ted.com/profiles/589766',
'http://www.ted.com/profiles/589563',
'http://www.ted.com/profiles/589510',
'http://www.ted.com/profiles/589132',
'http://www.ted.com/profiles/588807',
'http://www.ted.com/profiles/587474',
'http://www.ted.com/profiles/586364',
'http://www.ted.com/profiles/585088',
'http://www.ted.com/profiles/584467',
'http://www.ted.com/profiles/584201',
'http://www.ted.com/profiles/583327',
'http://www.ted.com/profiles/583149',
'http://www.ted.com/profiles/582791',
'http://www.ted.com/profiles/582395',
'http://www.ted.com/profiles/581299',
'http://www.ted.com/profiles/580520',
'http://www.ted.com/profiles/579598',
'http://www.ted.com/profiles/579341',
'http://www.ted.com/profiles/579318',
'http://www.ted.com/profiles/579299',
'http://www.ted.com/profiles/578983',
'http://www.ted.com/profiles/578514',
'http://www.ted.com/profiles/577510',
'http://www.ted.com/profiles/576793',
'http://www.ted.com/profiles/576490',
'http://www.ted.com/profiles/576139',
'http://www.ted.com/profiles/576031',
'http://www.ted.com/profiles/575586',
'http://www.ted.com/profiles/575432',
'http://www.ted.com/profiles/575283',
'http://www.ted.com/profiles/575164',
'http://www.ted.com/profiles/575126',
'http://www.ted.com/profiles/574824',
'http://www.ted.com/profiles/574204',
'http://www.ted.com/profiles/573937',
'http://www.ted.com/profiles/573628',
'http://www.ted.com/profiles/573580',
'http://www.ted.com/profiles/573520',
'http://www.ted.com/profiles/572619',
'http://www.ted.com/profiles/571819',
'http://www.ted.com/profiles/571774',
'http://www.ted.com/profiles/571770',
'http://www.ted.com/profiles/571154',
'http://www.ted.com/profiles/571037',
'http://www.ted.com/profiles/571003',
'http://www.ted.com/profiles/570577',
'http://www.ted.com/profiles/570209',
'http://www.ted.com/profiles/569889',
'http://www.ted.com/profiles/569875',
'http://www.ted.com/profiles/566202',
'http://www.ted.com/profiles/566084',
'http://www.ted.com/profiles/565653',
'http://www.ted.com/profiles/565627',
'http://www.ted.com/profiles/565490',
'http://www.ted.com/profiles/564529',
'http://www.ted.com/profiles/563071',
'http://www.ted.com/profiles/562816',
'http://www.ted.com/profiles/562435',
'http://www.ted.com/profiles/562327',
'http://www.ted.com/profiles/560135',
'http://www.ted.com/profiles/559802',
'http://www.ted.com/profiles/558727',
'http://www.ted.com/profiles/558680',
'http://www.ted.com/profiles/558652',
'http://www.ted.com/profiles/558649',
'http://www.ted.com/profiles/557701',
'http://www.ted.com/profiles/557321',
'http://www.ted.com/profiles/556546',
'http://www.ted.com/profiles/556153',
'http://www.ted.com/profiles/555213',
'http://www.ted.com/profiles/555021',
'http://www.ted.com/profiles/554986',
'http://www.ted.com/profiles/553979',
'http://www.ted.com/profiles/553971',
'http://www.ted.com/profiles/553915',
'http://www.ted.com/profiles/553774',
'http://www.ted.com/profiles/553732',
'http://www.ted.com/profiles/553623',
'http://www.ted.com/profiles/553611',
'http://www.ted.com/profiles/553472',
'http://www.ted.com/profiles/553463',
'http://www.ted.com/profiles/552376',
'http://www.ted.com/profiles/551959',
'http://www.ted.com/profiles/551878',
'http://www.ted.com/profiles/551580',
'http://www.ted.com/profiles/550709',
'http://www.ted.com/profiles/550688',
'http://www.ted.com/profiles/550643',
'http://www.ted.com/profiles/550637',
'http://www.ted.com/profiles/550608',
'http://www.ted.com/profiles/550180',
'http://www.ted.com/profiles/549401',
'http://www.ted.com/profiles/549055',
'http://www.ted.com/profiles/548863',
'http://www.ted.com/profiles/548775',
'http://www.ted.com/profiles/548520',
'http://www.ted.com/profiles/548260',
'http://www.ted.com/profiles/547722',
'http://www.ted.com/profiles/547598',
'http://www.ted.com/profiles/546497',
'http://www.ted.com/profiles/546219',
'http://www.ted.com/profiles/545996',
'http://www.ted.com/profiles/545775',
'http://www.ted.com/profiles/545227',
'http://www.ted.com/profiles/545192',
'http://www.ted.com/profiles/544629',
'http://www.ted.com/profiles/544358',
'http://www.ted.com/profiles/544258',
'http://www.ted.com/profiles/543139',
'http://www.ted.com/profiles/543137',
'http://www.ted.com/profiles/541415',
'http://www.ted.com/profiles/541317',
'http://www.ted.com/profiles/541224',
'http://www.ted.com/profiles/539649',
'http://www.ted.com/profiles/539532',
'http://www.ted.com/profiles/539097',
'http://www.ted.com/profiles/539031',
'http://www.ted.com/profiles/538203',
'http://www.ted.com/profiles/538158',
'http://www.ted.com/profiles/537534',
'http://www.ted.com/profiles/537508',
'http://www.ted.com/profiles/537381',
'http://www.ted.com/profiles/537165',
'http://www.ted.com/profiles/536413',
'http://www.ted.com/profiles/536354',
'http://www.ted.com/profiles/536073',
'http://www.ted.com/profiles/535922',
'http://www.ted.com/profiles/535071',
'http://www.ted.com/profiles/534511',
'http://www.ted.com/profiles/532150',
'http://www.ted.com/profiles/531794',
'http://www.ted.com/profiles/531608',
'http://www.ted.com/profiles/530982',
'http://www.ted.com/profiles/529726',
'http://www.ted.com/profiles/529465',
'http://www.ted.com/profiles/529390',
'http://www.ted.com/profiles/528955',
'http://www.ted.com/profiles/528558',
'http://www.ted.com/profiles/528542',
'http://www.ted.com/profiles/527542',
'http://www.ted.com/profiles/527536',
'http://www.ted.com/profiles/527487',
'http://www.ted.com/profiles/527344',
'http://www.ted.com/profiles/527033',
'http://www.ted.com/profiles/526490',
'http://www.ted.com/profiles/525721',
'http://www.ted.com/profiles/525163',
'http://www.ted.com/profiles/524567',
'http://www.ted.com/profiles/524289',
'http://www.ted.com/profiles/524013',
'http://www.ted.com/profiles/523726',
'http://www.ted.com/profiles/523268',
'http://www.ted.com/profiles/523100',
'http://www.ted.com/profiles/522980',
'http://www.ted.com/profiles/522651',
'http://www.ted.com/profiles/522123',
'http://www.ted.com/profiles/521845',
'http://www.ted.com/profiles/521771',
'http://www.ted.com/profiles/521402',
'http://www.ted.com/profiles/521109',
'http://www.ted.com/profiles/520905',
'http://www.ted.com/profiles/520752',
'http://www.ted.com/profiles/520690',
'http://www.ted.com/profiles/520118',
'http://www.ted.com/profiles/519411',
'http://www.ted.com/profiles/519052',
'http://www.ted.com/profiles/518922',
'http://www.ted.com/profiles/518847',
'http://www.ted.com/profiles/518821',
'http://www.ted.com/profiles/518773',
'http://www.ted.com/profiles/517778',
'http://www.ted.com/profiles/517677',
'http://www.ted.com/profiles/517430',
'http://www.ted.com/profiles/516771',
'http://www.ted.com/profiles/516334',
'http://www.ted.com/profiles/516063',
'http://www.ted.com/profiles/514743',
'http://www.ted.com/profiles/514388',
'http://www.ted.com/profiles/514086',
'http://www.ted.com/profiles/513447',
'http://www.ted.com/profiles/513302',
'http://www.ted.com/profiles/512954',
]
b=2
about=str('')
n=str
g=0
x=str
while b !=5: 
    html = scraperwiki.scrape(str(a[b]))
    root = lxml.html.fromstring(html)
    for el in root.cssselect("p.intro"):
        about=el.text
    f=html.count("dd")
    for el in root.cssselect("div.col dd")[0]:            
        lugar=el.tail
    for el in root.cssselect("div.col dd")[1]:            
        x=el.text
    scraperwiki.sqlite.save(unique_keys=['orden'],data={'orden':b,'about':about,'lugar':lugar,'id':str(a[b]),'x':x})
    b=b+1
    about=str('')
    g=0

