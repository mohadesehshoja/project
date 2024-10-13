from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core', backend='redis://localhost')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {"crontab": {"task": "home.views.my_task_2", "schedule": 2, "options": {"expires": 10}}}

