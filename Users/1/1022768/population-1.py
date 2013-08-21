import scraperwiki
from BeautifulSoup import BeautifulSoup

scraperwiki.metadata.save('data_columns',['Position','Language',' Internet users'])

def scrape_table(soup):
    data_table = soup.find("table",{"class":"wikitable sortable"})
    rows1 = data_table.findAll("tbody")

    rows = data_table.findAll("tr")
    for row in rows:
        record = {}
        table_cells = row.findAll("td")
        if table_cells: 
            record['Position'] = table_cells[0].text
            record['Language'] = table_cells[1].text
            record['Internet users'] = table_cells[2].text
            
            
            print record,'------------'
            scraperwiki.datastore.save(["Position"], record)
        

def scrape_and_look_for_next_link(url):
    html = scraperwiki.scrape(url)
    soup = BeautifulSoup(html)
    scrape_table(soup)
    


starting_url =  "http://en.wikipedia.org/wiki/Global_Internet_usage"
scrape_and_look_for_next_link(starting_url)