# Ruby scraper for consultations from the Charity Commission
require 'nokogiri'
require 'uri'

DEPARTMENT = "Charity Commission for England and Wales"

def scrape_page(url)
  # Details of the consultation
  record = { 'URI' => url, 'department' => '', 'agency' => DEPARTMENT }
  # Any documents linked from the consultation page
  documents = []

  consult_html = ScraperWiki.scrape(url)
  consult_doc = Nokogiri::HTML(consult_html, nil, 'utf-8')

  record['title'] = consult_doc.css('meta[name="DC.Title"]')[0]['content']

  record['published_date'] = Date.parse(consult_doc.css('meta[name="DC.Date.Created"]')[0]['content']).to_s
  unless consult_doc.css('span[property="dc:issued"]').empty? 
    record['start_date'] = Date.parse(consult_doc.css('span[property="dc:issued"]')[0]['content']).to_s
  else
    puts "No start date present"
  end
  record['end_date'] = Date.parse(consult_doc.css('span[property="dc:valid"]')[0]['content']).to_s
  record['sponsor'] = ''
  record['description'] = consult_doc.css('p[property="dc:abstract"]').inner_html.gsub("\243", "&pound;").gsub("\240", " ").strip

  # Find any linked documents
  parsed_consult_url = URI.parse(record['URI'])
  consult_documents = []
  consult_doc.css('a[rel="dc:hasPart"]').each do |link|
    d = { 'consultation' => record['URI'], 'URI' => parsed_consult_url.merge(link['href'].gsub(" ", "%20")).to_s }
    d['title'] = link['title']
    consult_documents.push(d)
  end

  puts consult_documents.size.to_s+" documents: "+consult_documents.collect { |d| d['title'] }.join("; ")

  ScraperWiki.save_sqlite(['URI'], record, 'consultations')
  consult_documents.each do |d|
    ScraperWiki.save_sqlite(['URI'], d, 'documents')
  end
end


# The list of consultations is in a separate scraper, so we can just run through the results for that
# looking for ones relevant to this department
record_count = 0
ScraperWiki.getData('directgov_consultations').each do |consultation|
  if consultation['department'] == DEPARTMENT
    record_count = record_count + 1
    puts "Record #{record_count} "+consultation['permalink']
    scrape_page(consultation['permalink'])
  end
end

