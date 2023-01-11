import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("app")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "fetch-items-periodically": {
        "task": "app.spreadsheets.tasks.get_items",
        "schedule": crontab(minute=0, hour="*/3"),
    },
}
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
