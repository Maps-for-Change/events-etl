from apscheduler.schedulers.blocking import BlockingScheduler
from etl.indivisible import main as indivisible


sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=60)
def timed_job():
    print('This job runs every 60 minute')
    try:
        indivisible.run()
    except ValueError as error:
        print('Caught this error: ' + repr(error))
    
sched.start()
