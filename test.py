# from etl.indivisible import main as indivisible
# 
# try:
#     indivisible.run()
# except ValueError as error:
#     print('Caught this error: ' + repr(error))

from etl.lib.crm import bluestatedigital as bsd
from etl.lib.base import export

source_url = "http://go.berniesanders.com/page/event/search_results"
scraper = bsd.EventsScraper(source_url, "Bernie Sanders")

# returns minified_data
scraper.run()

# export.Exporter.s3_export(scraper.get_data())
