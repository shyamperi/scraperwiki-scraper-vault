<?php
require "scraperwiki/simple_html_dom.php";
define("BASE_URL", "http://splitticket.moneysavingexpert.com/results.php?");


// Save a record to the data store.
function saveData($unique, $railway ) {
      scraperWiki::save_sqlite($unique, $railway );
}

function getLinks() {
    global $destination, $id, $from_city, $pisah, $i, $j;
    $id = 0;
            $froms= array('ABW','ABE','ACY','ABA','ABD','AUR','AVY','ABH','AGV','AGL','AYW','ACR','AAT','ACN','ACH','ACK','ACL','ACG','ACB','ACC','AML','ADD','ADW','ASN','ADM','ADC','ADL','AWK','AIG','ANS','AIN','AIR','ADR','AYP','ALB','ALD','AMT','AHT','AGT','AAP','AXP','ALX','ALF','ALO','ALW','ASS','ALM','ALR','ASG','ALN','ALP','ABC','AON','ALT','ALV','AMB','AMY','AMR','AMF','ANC','AND','ADV','ANZ','AGR','ANG','ANN','ANL','AFV','APP','APD','APF','APB','APS','ARB','ARD','AUI','ADS','ASB','ADN','ADK','AGS','ARG','ARL','ARM','AWT','ARN','ARR','ART','ARU','ACT','AUW','ASH','AHV','ABY','ASC','ASF','AFS','AFK','ASY','AHD','AHN','AHS','ANF','AWM','ASK','ALK','ASP','APG','AST','ATH','ATN','ATT','ATB','ATL','AUK','AUD','AUG','AVM','AVF','AVN','AXM','AYS','AYP','AYL','AYH','AYR','BAC','BAJ','BAG','BLD','BIO','BAB','BDK','BAL','BHC','BSI','BMB','BAM','BNV','BAN','BNG','3R','BAH','BAD','BSS','BB','BLL','BAR','BGI','BGD','BKG','BRT','BMG','BRM','BNH','BNS','BNI','BTB','BAA','BNL','BNY','BNP','BTG','BRR','BRL','BAV','BIF','BWS','BRY','BYD','BYI','BYL','BAU','BSO','BSK','BBL','BTH','BHG','BTL','BTT','BAK','BAT','BLB','BAY','BCF','BER','BRN','BSD','BSL','BEU','BEL','BEB','BCC','BEC','BKJ','BDM','BSJ','BDH','BMT','BEH','BDW','BEE','BKS','BLV','BLG','BGM','BLH','BLM','BLP','BEG','BVD','BEM','BEY','BEF','BEN','BTY','BYK','BAS','BFE','BKM','BKW','BYA','BBW','BRS','BRK','BWK','BES','BSC','BTO','BET','BYC','BEV','BEX','BXY','BXH','BCS','BIT','BKL','BID','BIW','BBK','BIC','BIL','BIG','BIN','BIY','BCG','BCH','BWD','BIK','BDL','BKC','BKQ','BKN','BKP','BHI','BMO','BHM','BSW','BIA','BBG','BIS','BIP','BPT','BTE','BBN','BFR','BKH','BHO','BPN','BPB','BPS','BKR','BLK','BAW','BFF','BLA','BAI','BKT','BKD','BLT','BLO','BSB','BLY','BLX','BWN','BLN','BYB','BOD','BOR','BOG','BGS','BON','BTD','BKA','BOC','BNW','BOT','BBS','BRG','BRH','BOH','BSN','6HT','17Q','BOE','BTF','BNE','BMH','BRV','BWB','BOP','BWG','BXW','BCE','BDQ','BDI','BOA','BDN','BTR','BTP','BML','BMY','BLE','BMP','BRP','BCN','BND','BSM','BYS','BDY','BRC','BFD','BRE','BWO','BEA','BRO','BGN','BDG','BWT','BDT','BRF','BGG','BGH','BTN','LRB','BMD','BNT','BPW','BRI','BHD','RBS','BNF','BRX','BGE','BDB','BSR','BCU','BHS','BCY','BOM','BMR','BMC','BMN','BMS','BMV','BSY','BSP','BPK','BKO','BME','BMF','BRA','BUH','BYF','BXB','BCV','BDA','BGA','BSU','BRW','BRU','BYN','BUC','BCK','BUK','BSV','BGL','BHR','BLW','BUE','BUG','BUY','BUW','BNA','BUD','BNM','BUU','BUB','BNC','BYM','BUI','BTS','BCB','BCJ','BUO','BUJ','BUT','BSE','BUS','BHK','BSH','BUL','BXD','BUX','BFN','BYE','CAD','CGW','Timetable','CPH','CWS','CAC','CDT','CIR','CSK','CDU','CAM','CBN','CBG','CBH','CBL','CMD','CMO','Timetable','ZCW','CNL','CNT','CAO','CST','CNN','CBE','CBW','CNY','CPU','CBB','CDD','CDB','CDF','CDQ','CDO','CDR','CRF','CAK','CAR','CTO','CLU','CMN','CML','CNF','CAN','CAY','CPK','CAG','CSH','CSB','CRS','CDY','CBP','CLC','CFD','CAS','CSM','CAT','CTF','CFB','CYS','CCT','CTL','CAU','CYB','CTH','CFH','CFO','CHW','CFR','CEF','CPN','CLN','CWC','CHG','CHC','CHX','CBY','CTN','CRT','CSR','CTE','CTM','CHT','CHU','CHE','CED','CEL','CHM','CLD','CNM','CPW','CYT','CHY','CHN','CSN','CSS','CTR','CRD','CHD','CLS','CSW','CNO','CCH','CIL','CHL','CHI','CLY','CPM','CHP','CRK','CIT','CHK','CHO','CRL','CLW','CHR','CHH','CTW','CHF','CTT','CIM','CTK','CLT','CLA','CPY','CLP','CLJ','CPT','CLR','CKS','CLV','CLG','CLE','CEA','CLI','CFN','CLH','CLK','CUW','CYK','CBC','CBS','COA','CSD','CSL','CGN','COL','CET','CEH','CLM','CLL','CNE','CWL','CWB','CME','COM','CNG','CNS','CON','CEY','CNP','CNW','COB','COO','CBR','COE','COP','CRB','COR','CKH','CKL','CPA','CRR','COY','CSY','COS','CSA','CGM','COT','CDS','CDN','COV','CWN','COW','CRA','CGD','CRM','CRV','CRW','CRY','CDI','CES','CSG','CWD','CRE','CKN','CWH','CNR','CCC','CRI','CFF','CFT','CMR','CMF','CKT','CRG','CFL','COI','CKY','CMY','CSO','CRH','COH','CWU','CWE','CRN','CRO','CYP','CUD','CUF','CUM','CUA','CUB','CUP','CUH','CUS','CUX','CMH','CWM','CYN','DDK','DSY','DAG','DAL','DAK','DAM','DMR','DLR','DLY','DLS','DLJ','DLK','DLT','DLW','DNY','DCT','DZY','DAR','DAN','DSM','DFD','DRT','DWN','DAT','DVN','DWL','DWW','Timetable','DEA','DEN','DNN','DGT','DGY','DHN','DLM','DBD','DNM','DGC','DMK','DNT','DTN','DEP','DBY','DBR','DKR','DPT','DEW','DID','DIG','DMH','Timetable','DNS','DMG','DGL','DIN','DND','DTG','DSL','DIS','DOC','DOD','DOL','DLH','DLG','DWD','DON','DCH','DCW','DOR','DKG','DPD','DKT','DMS','DDG','DVH','DVP','DVC','DVY','DOW','DRG','DYP','DRM','DRF','DRI','DTW','DRO','DMC','DFR','DRU','DMY','DUD','DDP','DFI','DRN','DST','DUL','DBC','DBE','DUM','DMF','DMP','DUN','DBL','DBG','DCG','DEE','DFL','DFE','DKD','DNL','DNO','DOT','DNG','DHM','DUR','DYC','DYF','EAG','EAL','ERL','EAR','EAD','ELD','EWD','ECR','EDY','EDW','EFL','EGF','EGR','EKL','EML','EMD','ETL','EWR','EBN','EBK','EST','ERA','ESL','EGN','EBD','EBV','ECC','ECS','ECL','EDL','EDN','EBR','EBT','EDG','HYM','EDP','EDB','EDR','EFF','EGG','EGH','EGT','EPH','ELG','ELP','ELE','ESD','ESW','ELR','ESM','ELS','ELW','ELO','ELY','EMP','EMS','ENC','ENL','ENF','ENT','EPS','EPD','ERD','ERI','ERH','ESH','EXR','ETC','EUS','EBA','EVE','EWE','EWW','EXC','EXD','EXT','EXG','EXM','EXN','EYN','FLS','FRB','FRF','FRL','FRW','FCN','FKG','FKK','FOC','FMR','FAL','FMT','NFA','FRM','FNB','FNN','FNC','FNH','FNR','FNW','ZFD','FLD','FAV','FGT','FAZ','FRN','FEA','FLX','FEL','FST','FNT','FEN','FER','FRY','FYS','FFA','FIL','FIT','FNY','FPK','FIN','FSB','FSG','FGH','FSK','FZW','FWY','FLE','FLM','FLN','FLT','FLI','FLF','FKC','FKW','FOD','FOG','FOH','FBY','FOR','FRS','FTM','FTW','FOK','FOX','FXN','FRT','FTN','FRE','FFD','FML','FRI','FZH','FRD','FRO','FLW','FNV','FZP','GNB','GBL','GCH','GRF','GGV','GAR','GRS','GSD','GSN','GSW','GMG','GTH','GVE','GST','GTY','GTW','GGJ','GER','GDP','GFN','GIG','GBD','GFF','GIL','GLM','GSC','GIP','GIR','GLS','GCW','GLC','PRA','GLQ','GLH','GLZ','GLE','GLF','GLG','GLT','GLO','GCR','GLY','GOB','GOD','GDL','GDN','GOE','GOF','GOL','GOM','GMY','GOO','GTR','GDH','GOR','GBS','GTO','GPO','GRK','GWN','GOX','GPK','GOS','GTN','GRA','GRT','GVH','GRV','GRY','GTA','GRB','GRC','GCT','GMV','GMN','GYM','GNL','GNR','GBK','GRL','GNF','GFD','GNH','GKC','GKW','GNW','GEA','GMD','GMB','GRN','GMT','GRP','GUI','GLD','GSY','GUN','GSL','GNT','GWE','GYP','HAB','HCB','HKC','HAC','HKW','HDM','HAD','HDF','HDW','HGF','HGG','HAG','HMY','HAL','HAS','HED','HFX','HLG','HID','HLR','HAI','HWH','HMT','HME','HNC','BKQ','HNW','HMM','HMD','HDH','HMP','HMC','HMW','HIA','HSD','HAM','HND','HTH','HAN','HPN','HRL','HDN','HRD','HLN','HWM','HWN','HRO','HPD','HRM','HGY','HRY','HRR','HGT','HRW','HOH','HTF','HBY','HPL','HTW','HPQ','HWC','HSL','HSK','HGS','HTE','HAT','HFS','HAP','HSG','HTY','HTN','HAV','HVN','HVF','HWD','HWB','HKH','HDB','HYR','HYS','HAY','HYL','HYM','HHE','HAZ','HCN','HDY','HDL','HDG','HLI','HHL','HLL','HXX','HAF','HWV','HTC','HBD','HEC','HDE','HNF','HEI','HLC','HLU','HLD','HMS','HSB','HML','HEN','HNG','HNL','HOT','HEL','HFD','HNB','HNH','HER','HFE','HFN','HES','HSW','HEV','HEW','HEX','HYD','HHB','HIB','HST','HWY','HGM','HIP','HIG','HHY','HTO','HLB','HLF','HLE','HLW','HIL','HLS','HYW','HNK','HIN','HNA','HIT','HGR','HOC','HBN','HOD','HCH','HLM','HOL','HHD','HLY','HMN','HYB','HON','HOY','HPA','HOK','HOO','HPE','HOP','HPT','HOR','HBP','HRN','HRS','HRH','HSY','HIR','HWI','HSC','HGN','HOU','HOV','HXM','HWW','HOW','HOZ','HOX','HYK','HBB','HKN','HUD','HUL','HUP','HCT','HGD','HUB','HUN','HNT','HNX','HUR','HUT','HUY','HYC','HYT','HKM','HYN','HYH','IBM','IFI','IFD','ILK','IMW','INC','INE','INT','INS','IGD','ING','INK','INP','INV','INH','INR','IPS','IRL','IRV','ISL','ISP','IVR','IVY','LVJ','JEQ','JOH','JHN','JOR','KSL','KSN','KEI','KEH','KEL','KVD','KEM','KMH','KMP','KMS','KML','KEN','KLY','KNE','KNS','KNL','KNR','KPA','KTH','KTN','KTW','KNT','KBK','KET','KWB','KWG','KEY','KYN','KDB','KID','KDG','KWL','KBN','KLD','KIL','KGT','KMK','KLM','KPT','KWN','KBC','KGM','KGH','KGX','KCM','KGL','KLN','KNN','KGN','KGP','KGS','KGE','KNG','KND','KIN','KIT','KBX','KKS','KIR','KKB','KBF','KSW','KDY','KRK','KKD','KKM','KKH','KKN','KWD','KTL','KIV','KVP','KNA','KBW','KNI','KCK','KNO','KNU','KNF','KYL','LDY','LAD','LAI','LRG','LKE','LAK');
$tos= array('ABW','ABE','ACY','ABA','ABD','AUR','AVY','ABH','AGV','AGL','AYW','ACR','AAT','ACN','ACH','ACK','ACL','ACG','ACB','ACC','AML','ADD','ADW','ASN','ADM','ADC','ADL','AWK','AIG','ANS','AIN','AIR','ADR','AYP','ALB','ALD','AMT','AHT','AGT','AAP','AXP','ALX','ALF','ALO','ALW','ASS','ALM','ALR','ASG','ALN','ALP','ABC','AON','ALT','ALV','AMB','AMY','AMR','AMF','ANC','AND','ADV','ANZ','AGR','ANG','ANN','ANL','AFV','APP','APD','APF','APB','APS','ARB','ARD','AUI','ADS','ASB','ADN','ADK','AGS','ARG','ARL','ARM','AWT','ARN','ARR','ART','ARU','ACT','AUW','ASH','AHV','ABY','ASC','ASF','AFS','AFK','ASY','AHD','AHN','AHS','ANF','AWM','ASK','ALK','ASP','APG','AST','ATH','ATN','ATT','ATB','ATL','AUK','AUD','AUG','AVM','AVF','AVN','AXM','AYS','AYP','AYL','AYH','AYR','BAC','BAJ','BAG','BLD','BIO','BAB','BDK','BAL','BHC','BSI','BMB','BAM','BNV','BAN','BNG','3R','BAH','BAD','BSS','BB','BLL','BAR','BGI','BGD','BKG','BRT','BMG','BRM','BNH','BNS','BNI','BTB','BAA','BNL','BNY','BNP','BTG','BRR','BRL','BAV','BIF','BWS','BRY','BYD','BYI','BYL','BAU','BSO','BSK','BBL','BTH','BHG','BTL','BTT','BAK','BAT','BLB','BAY','BCF','BER','BRN','BSD','BSL','BEU','BEL','BEB','BCC','BEC','BKJ','BDM','BSJ','BDH','BMT','BEH','BDW','BEE','BKS','BLV','BLG','BGM','BLH','BLM','BLP','BEG','BVD','BEM','BEY','BEF','BEN','BTY','BYK','BAS','BFE','BKM','BKW','BYA','BBW','BRS','BRK','BWK','BES','BSC','BTO','BET','BYC','BEV','BEX','BXY','BXH','BCS','BIT','BKL','BID','BIW','BBK','BIC','BIL','BIG','BIN','BIY','BCG','BCH','BWD','BIK','BDL','BKC','BKQ','BKN','BKP','BHI','BMO','BHM','BSW','BIA','BBG','BIS','BIP','BPT','BTE','BBN','BFR','BKH','BHO','BPN','BPB','BPS','BKR','BLK','BAW','BFF','BLA','BAI','BKT','BKD','BLT','BLO','BSB','BLY','BLX','BWN','BLN','BYB','BOD','BOR','BOG','BGS','BON','BTD','BKA','BOC','BNW','BOT','BBS','BRG','BRH','BOH','BSN','6HT','17Q','BOE','BTF','BNE','BMH','BRV','BWB','BOP','BWG','BXW','BCE','BDQ','BDI','BOA','BDN','BTR','BTP','BML','BMY','BLE','BMP','BRP','BCN','BND','BSM','BYS','BDY','BRC','BFD','BRE','BWO','BEA','BRO','BGN','BDG','BWT','BDT','BRF','BGG','BGH','BTN','LRB','BMD','BNT','BPW','BRI','BHD','RBS','BNF','BRX','BGE','BDB','BSR','BCU','BHS','BCY','BOM','BMR','BMC','BMN','BMS','BMV','BSY','BSP','BPK','BKO','BME','BMF','BRA','BUH','BYF','BXB','BCV','BDA','BGA','BSU','BRW','BRU','BYN','BUC','BCK','BUK','BSV','BGL','BHR','BLW','BUE','BUG','BUY','BUW','BNA','BUD','BNM','BUU','BUB','BNC','BYM','BUI','BTS','BCB','BCJ','BUO','BUJ','BUT','BSE','BUS','BHK','BSH','BUL','BXD','BUX','BFN','BYE','CAD','CGW','Timetable','CPH','CWS','CAC','CDT','CIR','CSK','CDU','CAM','CBN','CBG','CBH','CBL','CMD','CMO','Timetable','ZCW','CNL','CNT','CAO','CST','CNN','CBE','CBW','CNY','CPU','CBB','CDD','CDB','CDF','CDQ','CDO','CDR','CRF','CAK','CAR','CTO','CLU','CMN','CML','CNF','CAN','CAY','CPK','CAG','CSH','CSB','CRS','CDY','CBP','CLC','CFD','CAS','CSM','CAT','CTF','CFB','CYS','CCT','CTL','CAU','CYB','CTH','CFH','CFO','CHW','CFR','CEF','CPN','CLN','CWC','CHG','CHC','CHX','CBY','CTN','CRT','CSR','CTE','CTM','CHT','CHU','CHE','CED','CEL','CHM','CLD','CNM','CPW','CYT','CHY','CHN','CSN','CSS','CTR','CRD','CHD','CLS','CSW','CNO','CCH','CIL','CHL','CHI','CLY','CPM','CHP','CRK','CIT','CHK','CHO','CRL','CLW','CHR','CHH','CTW','CHF','CTT','CIM','CTK','CLT','CLA','CPY','CLP','CLJ','CPT','CLR','CKS','CLV','CLG','CLE','CEA','CLI','CFN','CLH','CLK','CUW','CYK','CBC','CBS','COA','CSD','CSL','CGN','COL','CET','CEH','CLM','CLL','CNE','CWL','CWB','CME','COM','CNG','CNS','CON','CEY','CNP','CNW','COB','COO','CBR','COE','COP','CRB','COR','CKH','CKL','CPA','CRR','COY','CSY','COS','CSA','CGM','COT','CDS','CDN','COV','CWN','COW','CRA','CGD','CRM','CRV','CRW','CRY','CDI','CES','CSG','CWD','CRE','CKN','CWH','CNR','CCC','CRI','CFF','CFT','CMR','CMF','CKT','CRG','CFL','COI','CKY','CMY','CSO','CRH','COH','CWU','CWE','CRN','CRO','CYP','CUD','CUF','CUM','CUA','CUB','CUP','CUH','CUS','CUX','CMH','CWM','CYN','DDK','DSY','DAG','DAL','DAK','DAM','DMR','DLR','DLY','DLS','DLJ','DLK','DLT','DLW','DNY','DCT','DZY','DAR','DAN','DSM','DFD','DRT','DWN','DAT','DVN','DWL','DWW','Timetable','DEA','DEN','DNN','DGT','DGY','DHN','DLM','DBD','DNM','DGC','DMK','DNT','DTN','DEP','DBY','DBR','DKR','DPT','DEW','DID','DIG','DMH','Timetable','DNS','DMG','DGL','DIN','DND','DTG','DSL','DIS','DOC','DOD','DOL','DLH','DLG','DWD','DON','DCH','DCW','DOR','DKG','DPD','DKT','DMS','DDG','DVH','DVP','DVC','DVY','DOW','DRG','DYP','DRM','DRF','DRI','DTW','DRO','DMC','DFR','DRU','DMY','DUD','DDP','DFI','DRN','DST','DUL','DBC','DBE','DUM','DMF','DMP','DUN','DBL','DBG','DCG','DEE','DFL','DFE','DKD','DNL','DNO','DOT','DNG','DHM','DUR','DYC','DYF','EAG','EAL','ERL','EAR','EAD','ELD','EWD','ECR','EDY','EDW','EFL','EGF','EGR','EKL','EML','EMD','ETL','EWR','EBN','EBK','EST','ERA','ESL','EGN','EBD','EBV','ECC','ECS','ECL','EDL','EDN','EBR','EBT','EDG','HYM','EDP','EDB','EDR','EFF','EGG','EGH','EGT','EPH','ELG','ELP','ELE','ESD','ESW','ELR','ESM','ELS','ELW','ELO','ELY','EMP','EMS','ENC','ENL','ENF','ENT','EPS','EPD','ERD','ERI','ERH','ESH','EXR','ETC','EUS','EBA','EVE','EWE','EWW','EXC','EXD','EXT','EXG','EXM','EXN','EYN','FLS','FRB','FRF','FRL','FRW','FCN','FKG','FKK','FOC','FMR','FAL','FMT','NFA','FRM','FNB','FNN','FNC','FNH','FNR','FNW','ZFD','FLD','FAV','FGT','FAZ','FRN','FEA','FLX','FEL','FST','FNT','FEN','FER','FRY','FYS','FFA','FIL','FIT','FNY','FPK','FIN','FSB','FSG','FGH','FSK','FZW','FWY','FLE','FLM','FLN','FLT','FLI','FLF','FKC','FKW','FOD','FOG','FOH','FBY','FOR','FRS','FTM','FTW','FOK','FOX','FXN','FRT','FTN','FRE','FFD','FML','FRI','FZH','FRD','FRO','FLW','FNV','FZP','GNB','GBL','GCH','GRF','GGV','GAR','GRS','GSD','GSN','GSW','GMG','GTH','GVE','GST','GTY','GTW','GGJ','GER','GDP','GFN','GIG','GBD','GFF','GIL','GLM','GSC','GIP','GIR','GLS','GCW','GLC','PRA','GLQ','GLH','GLZ','GLE','GLF','GLG','GLT','GLO','GCR','GLY','GOB','GOD','GDL','GDN','GOE','GOF','GOL','GOM','GMY','GOO','GTR','GDH','GOR','GBS','GTO','GPO','GRK','GWN','GOX','GPK','GOS','GTN','GRA','GRT','GVH','GRV','GRY','GTA','GRB','GRC','GCT','GMV','GMN','GYM','GNL','GNR','GBK','GRL','GNF','GFD','GNH','GKC','GKW','GNW','GEA','GMD','GMB','GRN','GMT','GRP','GUI','GLD','GSY','GUN','GSL','GNT','GWE','GYP','HAB','HCB','HKC','HAC','HKW','HDM','HAD','HDF','HDW','HGF','HGG','HAG','HMY','HAL','HAS','HED','HFX','HLG','HID','HLR','HAI','HWH','HMT','HME','HNC','BKQ','HNW','HMM','HMD','HDH','HMP','HMC','HMW','HIA','HSD','HAM','HND','HTH','HAN','HPN','HRL','HDN','HRD','HLN','HWM','HWN','HRO','HPD','HRM','HGY','HRY','HRR','HGT','HRW','HOH','HTF','HBY','HPL','HTW','HPQ','HWC','HSL','HSK','HGS','HTE','HAT','HFS','HAP','HSG','HTY','HTN','HAV','HVN','HVF','HWD','HWB','HKH','HDB','HYR','HYS','HAY','HYL','HYM','HHE','HAZ','HCN','HDY','HDL','HDG','HLI','HHL','HLL','HXX','HAF','HWV','HTC','HBD','HEC','HDE','HNF','HEI','HLC','HLU','HLD','HMS','HSB','HML','HEN','HNG','HNL','HOT','HEL','HFD','HNB','HNH','HER','HFE','HFN','HES','HSW','HEV','HEW','HEX','HYD','HHB','HIB','HST','HWY','HGM','HIP','HIG','HHY','HTO','HLB','HLF','HLE','HLW','HIL','HLS','HYW','HNK','HIN','HNA','HIT','HGR','HOC','HBN','HOD','HCH','HLM','HOL','HHD','HLY','HMN','HYB','HON','HOY','HPA','HOK','HOO','HPE','HOP','HPT','HOR','HBP','HRN','HRS','HRH','HSY','HIR','HWI','HSC','HGN','HOU','HOV','HXM','HWW','HOW','HOZ','HOX','HYK','HBB','HKN','HUD','HUL','HUP','HCT','HGD','HUB','HUN','HNT','HNX','HUR','HUT','HUY','HYC','HYT','HKM','HYN','HYH','IBM','IFI','IFD','ILK','IMW','INC','INE','INT','INS','IGD','ING','INK','INP','INV','INH','INR','IPS','IRL','IRV','ISL','ISP','IVR','IVY','LVJ','JEQ','JOH','JHN','JOR','KSL','KSN','KEI','KEH','KEL','KVD','KEM','KMH','KMP','KMS','KML','KEN','KLY','KNE','KNS','KNL','KNR','KPA','KTH','KTN','KTW','KNT','KBK','KET','KWB','KWG','KEY','KYN','KDB','KID','KDG','KWL','KBN','KLD','KIL','KGT','KMK','KLM','KPT','KWN','KBC','KGM','KGH','KGX','KCM','KGL','KLN','KNN','KGN','KGP','KGS','KGE','KNG','KND','KIN','KIT','KBX','KKS','KIR','KKB','KBF','KSW','KDY','KRK','KKD','KKM','KKH','KKN','KWD','KTL','KIV','KVP','KNA','KBW','KNI','KCK','KNO','KNU','KNF','KYL','LDY','LAD','LAI','LRG','LKE','LAK');
          
for ($i=1; $i<=count($froms); $i++){
            for ($j=1; $j<=count($froms); $j++){
      
            $url = "http://splitticket.moneysavingexpert.com/results.php?".\"$froms[$i]\"."&arrival=".\"$tos[$j]\"."&railcard=&travellers=adult&type=walkonsingle&hour=18&minute=41";
            $source = scraperWiki::scrape($url);
            $html = new simple_html_dom();
            $html->load($source);
            $id = $id+1;
            $ticketbodies = $html->find("div[@class='ticket']");
            $ticketvalues = $ticketbodies[0]->find("td[@class='ticketvalue']");
            $from_city= $ticketvalues[0]->innertext;
            $split_city= $ticketvalues[2]->innertext;
            $ticketvalues = $ticketbodies[1]->find("td[@class='ticketvalue']");
            $destination= $ticketvalues[2]->innertext;
            
            
                         $railway = array(
                         "id"=>$id,
                         "from_city"=>$from_city,                             
                         "destination"=>$destination,
                         "split_city"=>$split_city
                     
                        );
         // Save the record.
        saveData(array("id","from_city", "destination", "split_city"), $railway );
        $html->clear();
        unset($html);
   
}}
}
getLinks();
?>