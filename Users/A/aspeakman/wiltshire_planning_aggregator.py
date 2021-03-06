# Planning applications aggregator for Durham County Council

#This is a unitary authority with planning structure devolved to 4 districts.
#This scraper collects together all applications from the 3 sources.

import scraperwiki
import gc

scraperwiki.sqlite.attach('planningexplorer_system_planning_applications_2', 'planningexplorer')
scraperwiki.sqlite.attach('acolnet_system_planning_applications_2', 'acolnet')
scraperwiki.sqlite.attach('idox_system_planning_applications', 'idox')

systems = {
    'South and East Wiltshire': { 'type': 'planningexplorer', 'table': 'Wiltshire' },
    'North Wiltshire': { 'type': 'acolnet', 'table': 'NorthWiltshire' },
    'West Wiltshire': { 'type': 'idox', 'table': 'WestWiltshire' },
}

num_saved = 0
for k, v in systems.items():
    try:
        sql = '* from ' + v['type'] + '.' + v['table']
        data = scraperwiki.sqlite.select(sql)
        for datum in data:
            datum['district'] = k
        scraperwiki.sqlite.save(['uid'], data)
        print 'Source:', k, ' (saved', len(data), 'rows)'
        num_saved += len(data)
        data = None
        gc.collect()
    except:
        print 'Error:', k, ' (no data aggregated)'
print "Total applications stored =", num_saved

scraperwiki.sqlite.execute("create index if not exists date_scraped_manual_index on swdata (date_scraped)")
scraperwiki.sqlite.execute("create index if not exists start_date_manual_index on swdata (start_date)")



# Planning applications aggregator for Durham County Council

#This is a unitary authority with planning structure devolved to 4 districts.
#This scraper collects together all applications from the 3 sources.

import scraperwiki
import gc

scraperwiki.sqlite.attach('planningexplorer_system_planning_applications_2', 'planningexplorer')
scraperwiki.sqlite.attach('acolnet_system_planning_applications_2', 'acolnet')
scraperwiki.sqlite.attach('idox_system_planning_applications', 'idox')

systems = {
    'South and East Wiltshire': { 'type': 'planningexplorer', 'table': 'Wiltshire' },
    'North Wiltshire': { 'type': 'acolnet', 'table': 'NorthWiltshire' },
    'West Wiltshire': { 'type': 'idox', 'table': 'WestWiltshire' },
}

num_saved = 0
for k, v in systems.items():
    try:
        sql = '* from ' + v['type'] + '.' + v['table']
        data = scraperwiki.sqlite.select(sql)
        for datum in data:
            datum['district'] = k
        scraperwiki.sqlite.save(['uid'], data)
        print 'Source:', k, ' (saved', len(data), 'rows)'
        num_saved += len(data)
        data = None
        gc.collect()
    except:
        print 'Error:', k, ' (no data aggregated)'
print "Total applications stored =", num_saved

scraperwiki.sqlite.execute("create index if not exists date_scraped_manual_index on swdata (date_scraped)")
scraperwiki.sqlite.execute("create index if not exists start_date_manual_index on swdata (start_date)")



