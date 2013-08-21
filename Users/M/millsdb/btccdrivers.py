from mechanize import Browser
from BeautifulSoup import BeautifulSoup

import scraperwiki
from scraperwiki import sqlite
mech = Browser()

url = 'http://www.btcc.net/html/standings.php?standings_id=1&season_id=56'

page = mech.open(url)
html = page.read()
soup = BeautifulSoup(html)

table = soup.find("table", { "summary" : "Driver Standings Table" })


for row in table.findAll('tr')[1:50]:
    col = row.findAll('td')
    
    pos = col[0].string
    pos = pos.lstrip("0")

    driver = col[1].string

    points = col[2].string

    data = (pos, driver, points)
    scraperwiki.sqlite.save(unique_keys=["pos"], data={"pos":pos, "driver":driver, "points":points})

