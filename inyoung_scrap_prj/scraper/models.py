from django.db import models
import datetime

# Create your models here.
class TedFile(models.Model):
	title = models.CharField(max_length=50,default='name')
	talker_name = models.CharField(max_length=30, null=True)
	video_url = models.CharField(max_length=200, null=True)
	video_image = models.CharField(max_length=200, null=True)
	video_date = models.CharField(max_length=10, null=True)
	save_date = models.DateField(auto_now=True)

class MelonFile(models.Model):
	filename = models.CharField(max_length=20)
	date = models.DateTimeField()

