# https://devcenter.heroku.com/articles/clock-processes-python

from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management import call_command

sched = BlockingScheduler()


@sched.scheduled_job("cron", second=5)
def vote_reset():
    resp = call_command("vote_reset")  # Doesn't work...
    print(f"Job is done with {resp}")


sched.start()
