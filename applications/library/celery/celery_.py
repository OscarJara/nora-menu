from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nora.settings.local')
# assign project name
app = Celery('nora-menu')
# add django configuration file
app.config_from_object('django.conf:settings', namespace='CELERY')
# record of all decorated tasks within the task module
app.autodiscover_tasks()
# add redis url
app.conf.update(BROKER_URL = 'redis://localhost:6379/0') 