require 'nokogiri'
require 'open-uri'

url = 'http://montreal.fr.craigslist.ca/rid/'

html = open(url)
doc = Nokogiri::HTML(html)

cities = ['toronto', 'ottawa', 'boston', 'new york', 'nyc', 'windsor', 'kingston', 'cornwall', 'sudbury', 'niagara', 'sherbrooke', 'NY', 'TO', 'QC', 'Quebec City', 'border', 'lacolle']

listings = doc.css("p").map { |node| 
  { 
    'url' => URI.parse(node.at_css("a").attribute("href")),
    'content' => node.at_css("a").content
  }
}

listings.each do |listing|
  listing['destination'] = (listing['content'].downcase[/(#{cities.join("|")})/] || "N/A").gsub("nyc", "new york")
end

ScraperWiki.save_sqlite(unique_keys=['url'], data=listings)
