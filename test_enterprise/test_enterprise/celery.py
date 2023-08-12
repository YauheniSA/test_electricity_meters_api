import os
from celery import Celery

from test_enterprise.settings import M


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'test_enterprise.settings')

app = Celery('test_enterprise')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'every': {
        'task': 'electricity_meters.tasks.get_counter_values',
        'schedule': M,
    }
}
