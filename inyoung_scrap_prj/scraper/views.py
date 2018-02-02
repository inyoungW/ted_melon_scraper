from django.shortcuts import render
from  scraper.ted_scraper import *
from .models import TedFile
from django.core.paginator import Paginator
# Create your views here.

def index(request):
	tedFiles = TedFile.objects.all().order_by('-id')
	# ted_list = []
	# ted_dict= dict()
	# for tedfile in tedFiles:
	# 	ted_dict[tedfile.title]=tedfile
	# 	ted_list.append(tedfile)
	
	# # file didn't check 
	# if not checkExistFile():
	# 	talks = latest_talks()
	# 	for talk in talks :
	# 		if talk['title'] in ted_dict:
	# 			break
	# 		# save at db
	# 		new_talk = TedFile(title = talk['title'], talker_name = talk['talker_name'], video_url=talk['video_url'],
	# 			video_image= talk['video_image'], video_date = talk['video_date'])
	# 		new_talk.save()
	# 		ted_list.append(new_talk)

	# paging
	page = request.GET.get('page',1)
	paginator = Paginator(tedFiles,5)
	try:
		ted_list_page = paginator.page(page)
	except PageNotAnInteger:
		ted_list_page = paginator.page(1)
	except EmptyPage:
		ted_list_page = paginator.page(paginator.num_page)

	context = { "talks" : ted_list_page }
	return render(request,'scraper/index.html',context)



def graph(request):
	return render(request,'scraper/combo_chart.html')
