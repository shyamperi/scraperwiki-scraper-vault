import scraperwiki
import lxml.html



#functions

def getHTMLvalue(el, css, atr='text', index=0):
    try:
        lst = el.cssselect(css)
        val = ''
        if lst != None and len(lst) > 0:
            if index==0 or len(lst) >= index +1:
                if atr=='text':
                    val = lst[index].text_content()
                else:
                    val = lst[index].attrib.get(atr)
    
        return val
    except:
        return ''





postcodes = ['RM14','RM15','RM11','RM12','RM3','RM2','CM14','RM19','RM20','RM13','RM1','RM17','CM13','RM16','RM7','CM15','DA9','RM10','RM5','DA10','DA8','DA1','DA2','RM9','DA17','RM8','RM6','RM4','RM18','DA18','DA11','DA7','DA6','SE2','IG3','SS15','DA5','CM12','DA4','SE28','CM5','DA12','DA3','IG11','SS17','CM4','BR8','DA16','IG6','IG7','IG2','SS16','IG1','CM11','DA13','DA14','DA15','IG5','SE18','CM16','SS14','E12','E6','IG4','IG10','BR5','SE9','IG9','E7','IG8','E13','E16','SE7','E18','SS13','BR7','CM17','E11','TN15','BR6','CM18','SS12','SE3','E15','SE12','ME2','CM1','E20','SE10','CM20','CM2','SS11','CM99','E4','E10','TN14','BR1','CM19','CM21','ME6','E17','TN13','E14','EN9','SE13','E3','BR2','ME1','CM92','ME19','SE8','SE6','ME3','E9','SS7','CM22','ME4','SE4','ME20','SE14','E5','EN3','CM98','SE16','SS8','E1','BR4','E1W','E2','E8','BR3','N9','EN8','E98','SE23','CM23','ME5','E77','N18','ME7','TN16','N17','SE15','TN10','N16','EN10','SS6','N81','ME18','CM6','SE26','EN11','N15','EC3N','EN1','EC3A','SG10','TN11','SE1P','CM24','EC3M','SE22','EC3R','SE20','EC2A','EC3V','EC2M','EC2N','EC4R','EC1Y','EC2R','SE1','EC4N','TN9','EC2Y','EC2V','ME16','N1','N5','SE17','EC1V','SE5','EC4M','EC4V','N4','N1P','CM3','EC1M','EN7','SE21','EC1A','ME99','N21','EN2','EC1R','N13','EC1N','SE25','EC4A','EC4Y','SE19','EC3P','SE24','EC2P','EC50','EC4P','EC1P','N22','SE11','ME8','WC2A','WC1X','WC1R','N7','SS9','WC1V','SG12','SS5','ME14','N8','WC1N','CR0','SE27','WC2R','SW9','WC2B','WC2E','N1C','WC1H','WC2N','WC1B','WC2H','N19','WC1A','CR90','SW2','WC1E','W1D','RH8','CR9','ME15','W1A','NW26','NW1W','SW1A','CR7','CR2','SW1Y','SW1H','W1T','CR6','W1F','N14','SW1P','TN8','SW8','SG11','TN4','SW95','W1W','W1B','NW1','SW1E','NW5','W1S','N11','SW1V','N6','SG13','N10','SW4','W1J','TN2','W1G','SW16','W1C','TN1','W1K','SW1W','W1U','SS0','TN12','SW1X','CM77','W1H','SW12','CR44','SW3','N2','CR3','EN4','TN3','NW3','CR8','SW11','SG14','SS22','CM7','NW8','SW7','N20','SW17','N12','SS99','SS4','CM8','CR4','SS2','CB11','SM6','SW10','W2','RH9','W9','SW5','NW6','N3','W8','NW11','SS1','EN6','SW18','EN5','SM5','SW6','RH7','CR5','CM9','ME17','W14','CB10','W11','W10','NW2','SG9','TN7','SW19','NW4','SM4','SM1','W6','ME11','AL9','SW15','TN5','NW7','SM2','ME9','TN6','RH19','SW20','W12','NW10','RH18','ME10','AL7','SM3','SW13','SM7','NW9','SS3','RH1','TN17','W4','TN20','W3','KT4','AL8','AL10','SW14','AL6','CO9','HA8','SG3','KT3','SG2','WD6','HA9','ME12','CB9','KT17','KT20','TW9','RH2','TN19','W5','TN18','HA0','KT19','KT2','RH6','KT5','TW8','CB21','HA7','TW10','KT18','CM0','KT1','TN27','SG1','SG8','W13','HA3','WD7','KT6','CB22','TN21','TN22','KT9','TW1','RH77','W7','AL4','HA1','TW7','UB6','RH10','TW11','CO5','TN32','KT21','AL1','KT7','AL2','HA2','TW2','WD23','RH3','SG7','TW3','UB1','UB5','CO6','SG4','KT8','KT10','RH11','SG6','UB2','TW12','TN30','CO8','HA5','CB2','TW5','KT22','CB1','RH17','TW4','RH16','WD19','WD25','CB5','UB18','AL5','WD24','UB4','BN8','ME13','HA4','TN33','TW13','CB3','CO3','WD17','AL3','RH4','BN27','CB4','CO10','WD18','HA6','SG5','UB3','TW14','WD99','TW16','KT23','KT12','CB8','WD5','SG15','TN26','CO2','KT11','CB25','RH5','RH15','UB11','UB10','TW6','TN23','CB23','CO1','BN7','TN31','SG16','TW17','TN39','TW15','BN26','UB7','KT13','WD4','BN24','TN24','TN40','TN37','UB8','LU2','TN38','CO4','CB24','HP2','SG18','KT24','BN6','IP29','WD3','TN35','BN23','TN34','UB9','HP3','LU1','BN22','RH12','TN36','SG17','TW19','SG19','BN20','HP1','BN21','TW18','SL0','KT14','KT15','BN9','RH13','TN25','BN25','LU3','CT5','KT16','BN45','BN10','SL95','CO7','LU4','GU23','BN51','BN2','CB7','BN1','SL3','IP33','SL9','BN5','IP28','TW20','BN88','BN50','IP32','BN52','HP8','BN3','PE27','IP7','GU25','GU22','GU5','CT2','GU6','CB6','LU5','BN41','HP4','GU4','PE19','CT4','LU6','CT1','SL2','TN29','MK45','BN42','IP30','HP6','GU21','HP7','CT6','BN44','SL1','GU1','HP5','TN28','BN43','SL4','CO16','PE29','CO11','HP9','GU2','RH14','GU24','CO15','PE16','PE28','MK42','IP31','MK41','IP27','BN15','SL5','GU20','CT21','MK40','GU3','MK44','GU7','HP23','GU18','BN99','IP8','RH20','HP10','BN14','GU19','SL8','PE26','BN11','SL60','HP15','IP9','CT3','CT18','BN13','SL6','LU7','IP24','HP16','GU8','IP2','PE15','MK43','CT50','IP26','IP14','HP13','CO13','HP11','IP1','BN12','CT19','CT20','GU16','IP6','RG12','GU15','RG42','GU12','PE38','IP3','SL7','CO14','IP4','CT7','HP12','GU95','CO12','GU28','GU14','BN16','MK7','MK17','HP22','GU11','GU47','GU17','MK10','RG45','MK2','CT8','CT15','PE14','MK1','BN17','PE7','GU27','CT13','HP21','IP5','BN18','HP20','IP10','HP14','GU26','HP27','GU9','MK3','CT17','CT16','RG40','PE33','MK15','MK6','GU46','GU10','RG10','MK16','MK9','CT12','PE13','HP19','CT9','NN10','RG41','PE2','MK46','GU51','IP22','MK4','IP23','GU52','MK14','MK5','PE1','IP11','MK13','GU29','PE3','NN9','NN29','HP17','CT11','CT14','PE37','GU30','MK8','RG5','PE34','CT10','IP98','IP25','PE4','PO22','OX39','MK77','RG9','PE5','MK12','GU35','PE99','RG6','PE8','NR17','MK11','PE30','NR16','NN8','PE6','RG2','IP12','IP13','PO21','PE32','MK19','RG4','RG27','RG1','RG29','PE12','GU33','OX9','IP21','PO19','OX49','NN15','PO18','HP18','RG30','NN14','GU31','PE35','NN16','NR19','PO20','MK18','RG31','NN3','GU34','NR18','PE11','PE9','NN4','NN1','NN17','GU32','NN18','IP20','RG7','NN2','NN7','PE31','NR9','RG24','RG8','NR20','PE10','NR15','NN5','RG21','PO10','NN12','OX44','OX10','PE36','IP17','RG26','NR21','RG22','OX33','PO9','PE20','PO8','NN6','RG23','PE21','NR4','NR5','PO11','IP19','IP15','OX26','RG25','NR8','OX27','LE15','PO7','NR22','IP16','NR2','NR35','SO24','LE16','OX3','NN13','OX4','LE94','NR1','NR99','NR3','NR6','NR14','PO6','PE22','OX11','PO3','NR23','NG33','OX25','NR24','NR7','RG19','RG18','PO4','PO2','NR10','OX1','OX14','PO1','PO5','OX2','OX5','NG34','PO17','SO32','NR34','PO16','NR25','RG14','PO12','NN11','PE25','IP18','PO35','RG20','PE24','PO34','NR13','OX13','PO13','PE23','RG28','NG31','NR11','OX17','PO15','PO14','SO23','OX20','SO21','PO33','LE13','SO22','NG32','NR26','LN10','OX16','PO36','LE8','OX12','SO30','LE14','NR28','NR12','LN9','SO31','NR33','LE17','SO50','PO37','LN13','OX29','NR27','LE18','LN4','CV21','LE5','SO97','LE2','NR32','CV22','PO32','SO53','OX15','SO18','SO19','LE7','LE21','CV23','PO31','LE87','LE1','OX28','NR31','LE41','RG17','SO17','LN12','LE4','PO38','NR29','SP10','SO14','CV47','LE19','LE95','PO30','LE3','SO52','SO45','SO15','SO16','NR30','SP11','LN5','LN3','NG13','SO20','OX7','SN7','LN11','LE9','NG24','SO51','LE6','LN6','OX18','LN2','SO40','CV33','NG12','NG23','LE12','LN1','LE10','LN8','LE11','CV31','CV2','CV3','PO41','CV32','SO42','NG25','CV36','SP9','SN8','NG4','NG14','NG2','SO43','CV12','CV1','NG11','CV11','CV35','CV8','CV6','DN36','NG3','CV34','CV13','PO40','NG1','SO41','LE67','NG90','SN99','NG80','PO39','SN6','SN3','NG7','CV5','GL56','CV10','NG5','CV4','DN33','DN35','DN37','LN7','NG9','DN32','CV7','DN34','DE74','NG8','SN1','DN31','NG22','SN2','NG6','NG10','SN26','SN38','SN9','SP4','SN25','CV37','DN41','LE55','BH25','NG15','NG21','CV9','GL55','SN4','DN21','SN5','LE65','DE72','SP5','SP1','DN38','DN40','DE7','DN22','DE73','SP2','NG16','GL54','DN39','DN20','NG18','SP6','NG70','DE12','BH24','GL7','B93','NG19','B95','BH23','DE24','DE75','B46','HU19','NG17','B40','DE21','DE11','WR12','DE99','NG20','B78','HU12','B94','B50','DN16','B77','B37','DE1','DE23','DN19','B91','B92','DN10','BH6','B49','B79','DE5','DE22','DN17','BH31','S80','DN18','BH7','B26','DE15','B33','B34','DE55','B36','BH5','DN15','B90','DE3','WR11','S81','SN10','BH8','SN11','DN9','B35','B27','HU1','HU9','B76','B80','DE56','B25','HU3','HU2','BH22','DE14','HU13','BH1','B28','HU4','BH9','HU8','DE65','BH3','HU5','S44','BH10','B47','BH2','HU14','B98','B24','B8','B10','HU10','B11','B9','HU7','B72','B75','HU6','BH4','SP3','B13','B14','BH11','DE13','HU11','DN11','HU16','B73','B12','B96','S45','B23','B7','BH12','B97','S25','BH13','B5','B4','SN15','S43','GL52','B6','B48','SN16','GL53','B2','B99','B38','S42','B30','B3','BH21','WS14','BH14','B1','B74','HU20','HU15','B19','B44','B15','GL50','WS13','S26','S21','B18','B29','B16','BH17','B20','B42','S49','DN1','DN3','DN4','S41','HU18','DN8','HU17','B31','WR10','BH18','S40','BH15','DN7','WR7','GL51','S66','B21','DN55','B17','S20','DN2','SN12','B43','DE4','B66','B45','BH19','WS9','B67','B32','DN12','GL8','GL20','B60','WS5','B68','S13','BH16','DN5','DE6','S12','WS8','WS7','B71','S65','GL3','WS4','S60','S18','BA13','SN14','B61','B70','GL6','WS1','DN14','B62','S14','SN13','BA14','B69','BA12','YO43','B65','S64','GL5','WS15','WS2','S95','WS3','S8','S2','S9','WS10','GL4','B63','S62','DN6','S96','B64','SP7','S99','S98','S7','S61','S17','DY4','S1','S4','S97','ST14','WR8','WR9','S3','GL1','DY2','S63','BA15','S11','WV12','WR4','WS6','WV13','DT11','WS12','YO25','S5','WR5','DY9','WS11','WV14','WR99','DY1','S10','GL2','DE45','GL10','DY5','BH20','S6','WV11','WR3','GL9','WR1','WR78','S73','YO15','GL19','YO16','DY8','DY3','S74','S32','WR2','YO8','WV2','WF9','S35','YO42','WV1','WV10','SP8','DY6','BA11','WV4','S72','DY10','GL11','WV3','BA1','WV9','WF11','S70','WF8','WR14','BA2','ST10','GL12','S71','DY7','WV6','DY11','WF7','WV5','DY13','WR13','ST18','ST17','DT10','ST19','WV8','BS37','YO19','YO41','S33','S75','ST16','WF10','YO14','GL18','S36','BA9','ST11','WF6','DY12','GL13','SK17','BA8','WR6','YO10','BS30','LS25','YO23','BA10','WF4','BS36','HR8','YO1','GL14','BA3','YO31','ST13','WF90','BS31','YO90','YO24','ST15','WV7','WF2','YO91','WF1','LS24','BS15','BS16','YO17','ST3','LS26','GL17','YO11','YO32','YO30','ST9','YO60','YO12','ST12','BS39','WV15','WF5','BS35','WF3','YO26','ST2','BS5','HD8','BA7','GL15','BS32','BA4','LS15','LS88','ST20','BS4','BS14','BS34','DT2','DT1','SK23','YO13','BS0','ST4','WF12','BS98','LS99','BS7','DT9','BS99','LS10','BS2','TF11','ST1','LS23','LS14','DY14','ST21','LS98','BS1','HR7','LS9','BS6','WF13','HR9','WV16','BS3','LS11','BS10','ST6','BS13','DT3','BS80','LS8','LS27','WF17','GL16','DT5','LS1','LS2','BS8','DT4','HD9','ST8','WF14','BS9','YO18','SK22','LS7','WF16','LS3','ST5','LS22','ST55','HD5','LS12','LS6','WF15','LS4','TF10','LS17','BS41','TF7','HD4','SK13','TF3','HD1','WR15','BD11','LS5','BA5','BD19','HD2','TF2','BS11','TF12','SK11','TF8','SK10','LS13','TF4','YO61','CW12','NP16','ST7','BA21','BA22','LS16','BS40','SK12','LS28','HD3','HD6','YO62','BA20','LS18','HD7','BD4','HR1','BD12','SK6','HX5','TF1','SK14','NP25','BA6','BD3','HG5','BD5','TA11','SK15','BD6','BS48','SK7','BD2','BD99','BD1','BS20','LS19','HX4','HG2','SK2','TF13','BD10','OL5','HX3','BD7','OL3','YO22','YO51','SK16','TF5','HG1','CW3','BA16','BD8','TA15','HX1','NP26','SK1','TF9','OL6','BD98','BS27','M34','BD14','LS20','BD9','SK3','LS21','TF6','BD18','SK9','OL7','SK5','BD17','HX6','OL4','SY8','CW11','SK8','SK4','TA14','HX2','BS49','HR4','BD13','HR2','YO21','BD15','M43','TA12','OL8','M18','BS25','CW4','BS28','M19','OL1','OL95','CW98','M35','BD16','DT8','CW2','HR6','HG3','CW1','M11','BD97','BS21','OL2','M22','M20','M12','M90','OL9','YO7','TA18','TA16','M14','M13','BS26','TA10','TA13','M40','LS29','BS29','DT6','M23','HX7','M61','M99','M1','M4','OL15','NP15','M60','M21','M15','OL16','M2','WA16','M16','CW10','M9','TA17','CW5','M24','BD21','M3','WA15','M8','HG4','OL11','BD22','M7','M33','M5','M32','TS13','BS22','M50','OL12','WA14','BS24','OL14','TA7','SY2','NP18','SY6','M6','OL10','M17','M25','BD20','SY1','NP19','SY99','CW7','TA9','TA19','M45','M41','BS23','TS9','SY3','CW9','TS12','M30','M27','TS14','SY4','BL9','DL6','SY13','SY7','NP20','OL13','M31','TA8','WA13','M26','SY5','NP7','M44','DL7','TA6','NP44','TS11','TA20','CW8','BL8','M28','NP10','TS7','NP4','DT7','TS8','BL0','TS6','BL4','TS10','M38','BB4','TS15','TS3','CW6','BL78','BB8','BL2','BB10','TA3','TS4','M29','TS5','EX13','HR5','BB11','BL11','BL3','BD23','BB94','TS17','WA4','BB9','SY14','TS1','CF3','WA1','TS16','TS2','CF30','LD8','SY9','BL1','M46','TA5','BB18','WN7','WA3','BL7','NP11','WA2','HR3','TS18','BB12','TA2','WA55','TA1','NP13','CF23','TS20','BL5','TS19','TS23','DL8','CF99','CF24','NP8','BB5','CF95','SY12','WA5','CF10','DL9','LD7','TS25','WA6','TS22','EX24','EX12','CF11','CF64','CF91','WA7','NP12','WA12','DL10','BL6','CF14','WN2','NP23','TS24','BB3','TS26','DL1','CH3','CF83','DL98','BB6','WN4','DL3','CF82','BB1','NP24','CF5','TS21','DL2','CF81','WA8','WN1','WN3','BB7','CF63','BB2','WA9','NP22','TS27','EX14','WA88','CF15','SY15','LL13','CH2','SY11','WA11','CH88','CH99','WN5','TA21','WN6','CF46','WA10','PR6','TA4','TS28','L35','CH1','DL5','CF62','TS29','L24','CH70','L26','BD24','SR8','CH4','PR7','DL11','LL12','CF38','CF37','L27','CH65','L34','DL17','CH34','EX10','LL14','L36','DL4','L25','SY10','CF45','LL11','WN8','CH66','DH6','TA23','CF48','SY21','EX11','PR5','CF47','L19','PR25','L28','L16','SY22','L14','SR7','DL16','LD3','L18','DL14','CF72','EX15','L12','L15','PR0','PR26','L17','L33','CF39','L13','DH5','L32','CH5','PR1','LD1','L11','PR11','CH62','LL20','EX9','SY16','LD2','DH99','L7','DH1','PR2','L8','DH97','SR2','CF43','CF40','L6','L40','SR3','L10','CF44','CF71','L70','CH32','L67','L69','L73','DL15','CH63','L1','SR1','L4','L74','DH4','CH64','L9','L3','L5','L39','L2','L71','CF41','CF61','SR4','SR9','L68','CH33','L31','L75','CH42','L80','CH25','SR6','CH7','DL12','L20','SR5','DH7','L30','L72','PR3','CH41','EX8','CF35','L21','EX5','NE38','CF42','DH3','CH44','L29','CH26','TA24','DH2','CH43','CH27','NE36','CH60','PR4','CH31','NE37','EX16','CH45','CH6','NE35','NE34','L22','DH98','CH61','L23','EX3','CH30','NE33','CH49','NE32','CF31','TA22','NE85','CF32','CH28','LD6','CH46','NE10','NE9','NE31','SY17','L38','DH9','EX7','PR9','EX1','LD4','NE30','LA2','DL13','NE29','NE83','NE82','EX2','NE92','NE88','PR8','EX4','NE28','NE8','NE6','NE11','L37','CH48','LA6','NE98','CH47','NE99','NE26','NE1','LL15','LA10','CH29','TQ14','NE16','NE27','NE7','NE2','NE25','CH8','SY18','NE4','CF34','DH8','CA17','NE12','LD5','NE39','FY8','TQ1','NE21','FY0','NE3','LL21','LA1','NE17','CF33','NE5','TQ2','EX6','TQ5','CF36','NE15','NE40','NE13','NE23','FY4','FY6','NE24','FY3','SA13','TQ3','TQ4','LA5','LA4','NE41','TQ12','FY1','NE42','LA3','FY2','FY5','NE43','SA11','NE22','SY19','EX17','TQ6','SA9','LL16','NE64','LA7','FY7','NE20','NE62','NE63','SA12','NE44','SA10','LL17','SA20','LL19','CA16','NE18','LA9','EX36','LL23','TQ13','LA8','EX35','NE45','SA8','TQ9','NE61','LL18','LA11','SA7','NE46','TQ11','SA6','SA80','EX18','SA1','CA9','NE47','SA99','SY20','LL22','CA10','SA18','SA19','SA5','TQ7','TQ10','TQ8','LA23','SY25','EX37','SA2','NE65','LA12','LA13','LL40','EX32','SA4','SA3','LA15','LL24','EX19','NE19','LA14','LL29','LA22','PL21','LL26','LA16','EX31','CA11','EX20','NE66','LA17','LA21','NE49','SA14','NE48','SY24','EX34','LL28','LL27','SY23','LL25','SA48','LL35','LA20','LA18','LL31','LL39','SA15','LL41','NE67','LL32','LL30','PL8','SA32','LL36','EX38','EX33','NE68','LL38','PL7','SA40','LL42','LL37','PL20','CA8','NE69','PL9','LL34','CA4','SA16','LL43','PL6','PL95','PL19','LL47','SA39','LL44','EX21','LL45','EX39','PL3','NE70','PL4','LL48','SA17','LA19','LL46','CA12','SA46','LL33','PL1','PL5','PL2','SA31','PL18','CA1','CA18','SA47','LL49','CA19','NE71','PL16','CA99','CA2','PL10','CA3','PL12','CA5','SA44','SA45','PL11','CA6','LL57','EX22','PL17','LL58','CA20','LL52','SA33','LL51','LL59','LL55','PL15','LL56','CA21','SA38','TD15','CA13','CA7','CA23','DG16','LL54','CA22','CA26','DG14','LL75','TD12','CA25','LL61','TD8','CA24','LL74','LL76','LL60','SA35','TD5','LL73','CA27','LL72','EX23','PL14','LL78','CA28','SA37','LL77','PL13','SA36','SA34','DG13','CA14','LL70','CA15','TD9','DG12','SA43','CA95','TD14','LL69','LL62','LL53','TD11','LL71','TD10','SA69','SA41','LL68','TD6','SA67','SA70','PL32','LL66','LL63','SA66','PL35','TD3','TD4','SA68','PL23','PL22','DG11','LL64','TD7','LL67','PL33','PL34','TD1','PL31','PL30','PL24','TD13','SA63','SA42','LL65','TD2','PL29','PL25','SA71','SA72','DG1','EH43','PL26','PL27','EH42','SA61','SA65','EH44','DG2','SA73','DG10','DG5','SA64','EH40','EH36','EH38','TR9','PL28','SA62','EH41','EH45','EH34','TR2','EH37','EH39','EH35','EH23','DG6','TR8','EH33','EH31','TR7','EH22','EH32','TR1','DG7','EH19','EH24','DG3','EH18','EH21','EH25','EH20','EH26','EH17','TR11','EH46','KY10','TR3','EH15','EH16','TR4','TR6','TR10','ML12','EH8','EH9','EH10','EH7','EH13','KY9','EH1','EH99','EH6','EH2','TR5','EH3','EH11','EH14','EH5','EH91','EH12','TR16','EH4','TR12','EH95','TR15','KY8','EH27','DG4','KY16','KY1','EH28','KY3','TR14','KY2','EH53','EH29','TR13','EH30','EH55','EH54','KY7','EH52','ML11','DD11','DD7','KY15','KY6','KY11','KY5','DG8','KY4','KY99','EH47','TR27','DD6','DD5','DD10','EH48','ML8','EH49','DD4','DD1','KY12','ML7','TR26','EH51','DD3','TR17','KY14','DD2','TR20','TR93','ML2','ML9','KY13','KA18','AB30','AB39','DD9','FK3','TR18','ML10','PH14','FK2','ML1','FK1','DD8','AB12','ML3','AB99','ML6','ML4','FK14','FK5','AB11','PH2','AB10','TR19','PH12','ML5','AB25','G71','AB15','AB24','KA17','AB13','FK4','FK13','FK10','AB14','AB16','KA5','G72','PH13','G67','G70','AB22','FK6','G74','KA16','G75','AB23','KA6','G68','FK12','PH1','G69','G34','G79','KA4','AB32','G32','FK11','AB21','PH11','FK7','G73','G65','AB31','G33','G45','PH3','G76','G31','PH4','G40','G44','PH10','KA19','G42','FK9','G66','G21','G5','G1','G90','G9','G77','G43','G58','G46','G2','KA1','DG9','G4','G41','G64','KA7','KA8','G22','G3','KA9','FK15','KA3','KA26','G20','G51','AB41','G53','PH5','G12','G23','G11','KA2','FK8','G52','G78','PH7','AB51','G14','PH8','AB42','G13','KA10','AB34','G61','FK16','G62','PA1','PA2','PA4','G15','KA11','PA3','KA12','G81','PA5','PA8','AB33','PA9','G60','PH6','KA13','PA10','KA15','G63','PH9','PA6','PA7','AB35','AB52','KA20','PA12','KA14','PA11','FK17','KA24','BT22','KA25','KA21','KA22','AB43','AB53','G82','PA13','AB36','PH16','PH15','BT21','BT30','KA23','G83','PA14','FK18','KA29','AB54','FK19','KA30','PA15','PH18','KA28','BT19','BT23','BT20','PA16','AB44','BT33','G84','PA17','FK21','AB45','PA19','TR21','PA18','KA27','TR25','BT24','BT16','TR24','BT31','AB55','TR23','PA23','AB37','TR22','BT18','PA20','BT38','BT5','BT4','BT8','BT6','AB38','BT3','BT7','FK20','BT2','BT1','AB56','BT9','BT15','BT37','PH17','PH25','BT40','PA24','BT12','BT13','BT10','BT14','BT27','IV32','BT34','PH26','BT11','BT26','BT17','PH22','BT36','PH24','PA22','BT25','PH21','BT28','PA26','PA21','PH19','PH23','PA28','BT39','PH20','PA27','PA25','PA36','IV30','BT32','PA32','IV31','PA29','PH30','BT29','BT67','PA33','IV36','BT35','IV13','BT66','BT65','BT63','PA30','BT41','BT64','PA31','PA41','IV12','BT62','BT42','PA35','BT43','PH50','PH31','BT44','IV2','PH49','IV99','BT60','IV1','BT61','IV3','IV10','PH32','PH34','BT54','IV9','IV11','PA37','IV63','IV20','PH33','IV8','PA34','PA38','IV5','PA60','PH35','IV18','BT71','IV4','IV19','BT53','KW2','BT45','IV6','IV7','KW3','KW7','IV17','PA42','BT68','KW8','IV16','KW6','IV15','KW5','IV25','BT80','KW9','BT46','PA63','KW1','KW10','PA64','PA46','BT57','PA45','IV14','BT70','PA65','BT69','PA62','PA43','BT51','BT52','PA44','BT56','IV28','PH37','IV24','PA80','PA48','BT55','PA49','PA61','KW12','BT77','PA70','PA47','PA71','PA72','PA69','BT76','PH38','PH36','KW14','BT49','PA67','PA68','KW13','KW11','BT79','BT75','KW15','PH39','PA73','PH40','PA75','IV23','PA66','KW17','BT92','PH41','PA74','PA76','KW16','IV53','BT78','IV40','BT47','IV43','IV52','IV45','IV44','IV41','BT94','IV54','IV42','BT48','PH42','BT82','IV46','BT74','IV26','IV49','IV27','IV22','ZE3','BT81','PA78','PH43','IV48','IV21','BT93','PA77','ZE1','PH44','IV47','IV51','IV56','ZE2','IV55','HS4','HS1','HS9','HS2','HS8','HS3','HS5','HS7','HS6']
    
baseurl = 'http://www.just-eat.co.uk'
#postcodes = ['rm1', 'rm2', 'rm3']

for postcode in postcodes:
    url = 'http://www.just-eat.co.uk/area/' + postcode
    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html)
    for restaurant in root.cssselect(".restaurantWithLogo"):
        record = {}
        record['name'] = getHTMLvalue(restaurant, "h3")
        link = getHTMLvalue(restaurant, "h3 a", "href")
        record['link'] = link
        record['url'] = baseurl + link
        record['address'] = getHTMLvalue(restaurant, "address")
        record['foodtype'] = getHTMLvalue(restaurant, '.restaurantCuisines').replace("Type of food", "")
        
        #get BT details

        scraperwiki.sqlite.save(['link'], record)
        #print name, link, address, foodtype