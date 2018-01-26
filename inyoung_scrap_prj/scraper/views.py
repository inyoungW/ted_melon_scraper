from django.shortcuts import render
from  scraper.ted_scraper import *
# Create your views here.

def index(request):
	talks = latest_talks()
	context = { "talks" : talks}
	return render(request,'scraper/index.html',context)
