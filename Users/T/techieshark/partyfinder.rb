# Blank Ruby


require 'nokogiri' 

committees = [13967,
14232,
5587,
193,
13356,
13294,
11528,
2690,
12631,
5399,
5690,
14592,
12127,
15145,
125,
147,
11508,
5885,
15319,
5434,
4821,
2225,
3477,
3215,
12891,
3481,
4112,
13635,
13926,
3420,
6446,
4247,
4897,
3545,
11487,
5458,
15255,
2362,
6106,
470,
14060,
4335,
6104,
12510,
2423,
4797,
893,
4680,
4270,
1430,
2278,
5133,
14201,
5079,
15469,
14052,
3584,
14198,
4831,
11927,
14277,
12916,
4155,
1670,
4813,
15330,
10967,
931,
14349,
4726,
4090,
15627,
11708,
4893,
14014,
4653,
13866,
15237,
3073,
5677,
11767,
14225,
3591,
15143,
15103,
15001,
11227,
3482,
5254,
13326,
2392,
13475,
13327,
12498,
4259,
4727,
5707,
461,
2740,
13042,
12267,
10288,
5571,
5089,
91,
4241,
15394,
15576,
13998,
3701,
5107,
4681,
5152,
682,
15858,
12511,
14049,
15621,
3362,
15298,
5583,
13163,
4792,
5591,
4454,
2752,
13920,
5724,
14065,
14601,
5158,
5718,
5719,
13289,
5709,
4752,
5290,
13354,
12642,
5261,
4826,
4318,
5714,
8125,
5208,
4846,
4824,
2367,
4212,
2758,
4152,
4022,
1471]


def getParty(id) 
  html = ScraperWiki::scrape("https://secure.sos.state.or.us/orestar/sooDetail.do?cneCommitteeId=#{id}")
  #p html
         
  doc = Nokogiri::HTML html
  doc.search("table table tr").each do |v|
    cells = v.search 'td'
    
    # find cell with value 'Party Affiliation'
    cells.each_with_index do |cell, i| 
      if cell.inner_html.match(".*Party Affiliation.*")
        data = { committee: id,
                 party: cells[i+1].inner_html.split().join(' ') 
               }
        #puts data.to_json 
        #puts "#{id}, #{cells[i+1].inner_html.split().join(' ')}"
        ScraperWiki::save_sqlite(['committee'], data)  
        break
      end
    end
  end
end

 

committees.each do |id| 
  getParty(id)
end