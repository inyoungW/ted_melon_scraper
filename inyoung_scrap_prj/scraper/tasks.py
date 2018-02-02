from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from  scraper.ted_scraper import *
from .models import TedFile

@task(name="sum_two_numbers")
def add(x, y):
	return x + y

@task(name="multiply_two_numbers")
def mul(x, y):
	total = x * (y * random.randint(3, 100))
	return total

@task(name="sum_list_numbers")
def xsum(numbers):
	return sum(numbers)


@task(name='check_new_update_ted')
def update():
	tedFiles = TedFile.objects.all()
	ted_dict= dict()
	for tedfile in tedFiles:
		ted_dict[tedfile.title]=tedfile
	new_ted_file = []
	talks = latest_talks()
	for talk in talks :
		if talk['title'] in ted_dict:
			break
		# save at db
		new_talk = TedFile(title = talk['title'], talker_name = talk['talker_name'], video_url=talk['video_url'],
			video_image= talk['video_image'], video_date = talk['video_date'])
		new_ted_file.append(new_talk)
		
	# Save new ted video info 
	new_ted_file.reverse()
	for new_ted in new_ted_file:
		new_ted.save()