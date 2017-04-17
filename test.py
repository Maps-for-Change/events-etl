import json
# from etl.indivisible import main as indivisible
# 
# try:
#     indivisible.run()
# except ValueError as error:
#     print('Caught this error: ' + repr(error))

from etl.lib.crm import nationbuilder as nb
from etl.lib.base import export

scraper = nb.EventsScraper("https://site.nationbuilder.com", \
                            access_token="1651c2ef7e300300753f0cc1f49e793a55d111c7c", \
                            calendar_id=4, \
                            slug="slug",
                            event_types={"Phonebank": "phonebank"})
d = scraper.retrieve()
trans = scraper.translate(d)

print(json.dumps(trans))

# source_url = "http://go.berniesanders.com/page/event/search_results"
# scraper = bsd.EventsScraper(source_url, "Bernie Sanders")
# 
# # returns minified_data
# scraper.run()

# export.Exporter.s3_export(scraper.get_data())
