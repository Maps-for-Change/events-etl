# encoding=utf8

from etl.lib.crm import bluestatedigital as bsd
from etl.lib.base import export


def run():
    print('RUN] Running Job to get events....')
    # source_url = "http://go.berniesanders.com/page/event/search_results"
    # scraper = bsd.EventsScraper(source_url, "Chris Murphy for CT")
    # scraper.run()
    # export.Exporter.s3_export(scraper.get_data())
