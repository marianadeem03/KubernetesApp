import os
from celery import shared_task
from celery import Celery
from celery.schedules import crontab


@shared_task
def sample_periodic_task():
    print("This is a periodic task!")


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sample_task': {
        'task': 'config.celery.sample_periodic_task',
        'schedule': crontab(minute='*/1'),  # Run every minute
    },
}
