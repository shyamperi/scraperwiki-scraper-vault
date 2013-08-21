import scraperwiki
import re
import urllib2
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
scraperwiki.sqlite.execute("CREATE TABLE role33 ('Index' string,'Role' string,'Title' string, 'contact' string)")
scraperwiki.sqlite.commit()
#scraperwiki.sqlite.execute("insert into  dukeurest values (?,?,?,?,?,?,?,?,?,?,?.?)", ('First Name' ,'Middle Initial' ,'Degree & Certifications' ,'Endowed Professorship' ,'Rank & Title' ,'Department' ,'College' ,'Office Location' , 'Laboratory Location' , 'Phone' ,'Fax' ,'Email' ))

scraperwiki.sqlite.commit()
#list = ['2127','7025','4390']

list = ['4390','5673','5828','6555','761','1422','6105','3765','3762','1731','3162','4903','4921','4492','1915','7740','4501','4841','6892','2530','3764','4504','4843','1126','1128','1894','1350','3440','1171','3641','4384','4069','3103','4352','4845','3643','5998','6324','3782','3880','4415','2127','1349','6326','4034','2582','1634','3866','1545','3113','4927','2614','1263','7089','4147','4040','4134','1906','4472','3616','6802','2779','7119','3569','1593','3105','6837','6476','4238','4245','6851','1134','4370','2321','2826','1139','1133','2467','3776','3107','1896','1146','2830','3120','3121','6108','6481','1376','6244','2469','3109','1854','5220','2618','2088','2804','3335','1468','2942','2718','931','1562','3212','4420','3114','913','3588','1736','1908','4236','4931','1568','5897','3111','4453','1898','4465','3635','2289','3115','1911','2852','4359','4294','7162','2855','3406','7548','1050','7025','3116','990','896','3122','1738','6698','4526','869','7943','7094','4418','4929','4433','4945','3818','6733','3658','1280','891','3126','2334','2750','1704','3417','7883','3131','3360','1862','4292','4949','3696','6984','7144','6588','3263','3025','3493','4439','2381','6330','6600','6547','2298','6337','4148','2476','3134','4488','6813','4894','1119','2247','4872','3128','3101','6195','4379','3714','4316','3698','2148','4312','2501','4567','2104','2338','2319','4540','6228','4297','2281','1597','2113','6879','3502','4573','2549','2389','4042','6715','3647','976','2499','2336','2500','3143','2292','3344','4576','4867','4940','4345','2361','4869','6840','4026','4491','2857','2399','3950','3945','4097','4201','2138','6814','3141','767','2742','1739','3701','3890','3561','4459','4434','4167','3276','2311','2359','7702','4270','4269','3255','8702','8703','6139','4575','4101','4085','1150','3823','6707','2893','6224','1336','3831','4274','4946','3461','3504','7030','2233','2772','2562','3145','4834','1262','1253','1259','5915','1414','4220','36','3350','2297','4873','3836','6546','7644','2944','3161','3264','2485','1872','1572','6397','6549','3810','6711','4396','2752','3460','3152','1001','3706','3148','3506','1227','4875','2805','1666','994','4322','4560','4545','2588','2227','4876','3027','6710','1444','3150','3267','4525','6944','4553','1232','4542','2945','759','4548','6625','6609','4114','981','3367','953','2512','4564','4565','7037','7040','6843','1248','3758','1045','1870','1140','2909','1861','1111','5446','4218','4831','3711','3710','1502','933','4122','6552','4045','1069','3731','7044','7008','6229','7069','6196','4030','6953','7148','6335','7103','6197','7050','6665','7149','6303','6211','6482','6713','7163','6169','6520','6202','2307','893','4017','4906','6338','2520','3125','4570','6601','4189','2445','2769','1203','4196','2137','3882','6894','2754','1212','3878','4279','4557','4331','3898','1138','2828','1183','4233','2456','1897','4406','1864','2310','1914','4429','1342','7057','4060','4437','7038','6103','6264','1905','4481']
pre = 'http://w20.education.state.mn.us/MdeOrgView/organization/show/'
#list = ['1698']
for l in list:
    print l
    url = pre + l
    page = urlopen(url).read()
    Soup = BeautifulStoneSoup(page)
    tab = Soup.findAll(name = 'table', attrs = {"class":"data-table table-condensed"})
    #print 'len is %d' %(len(tab))
    ij = 1
    if (len(tab) == 9):
        ij = 2
    if len(tab) >= 8:
        t3 = tab[ij]
        t4 = t3.findAll('tr')
        t5 = t4[1];
        col = t5.findAll('td')
        #print col
        #print col[0].string.strip(' ')
        
        role=col[0].span.abbr.renderContents().strip(' ')
        title=col[1].span.renderContents().strip(' ')
        #nam =col[2].span.a.renderContents().strip(' ') 
        #nam = nam.replace('"','')
        #re.sub('[\s+]',' ',nam);
        #nam.replace('\n','')
        contact =col[3].span.a.renderContents().strip(' ') 
        contact = contact.replace('\n','');
        re.sub('[\S+]','',contact)
        #print '%s %s ' %(nam,role)
        #
    else :
        role = 'Null'
    scraperwiki.sqlite.execute("insert into  role33 values (?,?,?,?)", (l,role,title,contact))
    scraperwiki.sqlite.commit()

    #print role
    #print title
    #print nam
    #print contact
    #
    #for row in t3.findAll('tr'):
    #    col = row.findAll('td')
    #    prvy = col[0].string.strip()
    #    druhy = col[1].string.strip()
    #print t5
    #t3.petrify
    #tab2 = tab.nextSibling
    #print tab2
    
