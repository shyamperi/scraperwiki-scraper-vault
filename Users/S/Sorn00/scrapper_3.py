###############################################################################
# START HERE: Tutorial 3: More advanced scraping. Shows how to follow 'next' 
# links from page to page: use functions, so you can call the same code 
# repeatedly. SCROLL TO THE BOTTOM TO SEE THE START OF THE SCRAPER.
###############################################################################

import scraperwiki
from BeautifulSoup import BeautifulSoup

# define the order our columns are displayed in the datastore
scraperwiki.metadata.save('data_columns', 'Critic')

# scrape_table function: gets passed an individual page to scrape




def scrape_table(soup):
    
    tds = soup.findAll('td') # get all the <td> tags
for td in tds:
    #print td # the full HTML tag
    print td.text # just the text inside the HTML tag
    record = { "td" : td.text } # column name and value
    scraperwiki.datastore.save(["td"], record) # save the records one by one

    #data_table = soup.find("table", { "class" : "data" })
    #rows = data_table.findAll("tr")
    #for row in rows:
        # Set up our data record - we'll need it later
        #record = {}
        #table_cells = row.findAll("td")
        #if table_cells: 
            #record['Artist'] = table_cells[0].text
            #record['Album'] = table_cells[1].text
            #record['Released'] = table_cells[2].text
            #record['Sales (m)'] = table_cells[4].text
            # Print out the data we've gathered
            #print record, '------------'
            # Finally, save the record to the datastore - 'Artist' is our unique key
            #scraperwiki.datastore.save(["Artist"], record)
        
# scrape_and_look_for_next_link function: calls the scrape_table
# function, then hunts for a 'next' link: if one is found, calls itself again
def scrape_and_look_for_next_link(url):
    html = scraperwiki.scrape(url)
    soup = BeautifulSoup(html)
    scrape_table(soup)
    next_link = soup.find("a", { "class" : "next" })
    print next_link
    if next_link:
        next_url = base_url + next_link['href']
        print next_url
        scrape_and_look_for_next_link(next_url)

# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------
base_url = 'http://www.rottentomatoes.com/critics/authors.php'
starting_url = base_url
scrape_and_look_for_next_link(starting_url)
