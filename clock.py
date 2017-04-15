# encoding=utf8

from apscheduler.schedulers.blocking import BlockingScheduler
from tasks import scrape_events

from rq import Queue
from worker import conn

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_for_scraping_events():
    print('Running Job for event....')
    q = Queue(connection=conn)
    result = q.enqueue(scrape_events.run, timeout=500)
    
sched.start()
