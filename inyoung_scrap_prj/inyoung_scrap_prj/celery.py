from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab

# Django의 세팅 모듈을 Celery의 기본으로 사용하도록 등록합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inyoung_scrap_prj.settings')

from django.conf import settings  # noqa

app = Celery('inyoung_scrap_prj')

# 문자열로 등록한 이유는 Celery Worker가 Windows를 사용할 경우 
# 객체를 pickle로 묶을 필요가 없다는 것을 알려주기 위함입니다.
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
	'add-every-one-hour-contrab': {
		'task': 'check_new_update_ted',
		'schedule': crontab(minute='*/30'),
	},

}