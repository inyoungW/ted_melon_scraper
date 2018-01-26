from django.db import models

# Create your models here.
class TedFile(models.Model):
	filename = models.CharField(max_length=20)
	date = models.DateTimeField()

class MelonFile(models.Model):
	filename = models.CharField(max_length=20)
	date = models.DateTimeField()