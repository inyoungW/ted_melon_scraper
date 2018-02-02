import requests
import re
import os.path
import datetime
from scrapy.selector import Selector

ted_file_path=""

def fetch_page(url):
	r = requests.get(url)
	return r.text


def checkExistFile():
	now = datetime.datetime.now()
	date = now.strftime('%Y%m%d')
	title = 'ted_'+date+'.html'
	ted_file_path = os.getcwd()+"/scraper/ted_date_file/"+title
	if os.path.isfile(ted_file_path):
		return True
	else: 
		return False


# def saveTedHtml(html):
# 	now = datetime.datetime.now()
# 	date = now.strftime('%Y%m%d')
# 	title = 'ted_'+date+'.html'
# 	ted_file_path = os.getcwd()+"/scraper/ted_date_file/"+title
# 	if os.path.isfile(ted_file_path):
# 		return False
# 	else:
		

def latest_talks(page=1):
	ted_url = 'http://www.ted.com/talks?page={0}'.format(page)
	titles, talker_names, video_urls, video_images, video_date = talk_from_page(ted_url)
	length = len(titles)
	talks = []
	for i in range(length):
		temp_dict = { 'title':titles[i], 'talker_name':talker_names[i], 
		'video_url':video_urls[i],'video_image' :video_images[i], 'video_date':video_date[i] }
		#print([titles[i],talker_names[i], video_urls[i], video_images[i]])
		talks.append(temp_dict) 

	return talks


def talk_from_page(ted_url):

	html = fetch_page(ted_url)
	#ted_file_path = saveTedHtml(html)
	# with open(ted_file_path, 'wb') as f:
	# 		f.write(html.encode('utf-8'))

	sel= Selector(text=html)
	
	titles = sel.css('.talk-link .media__message a::text').extract()
	talker_names = sel.css('.talk-link .media__message .h12::text').extract()
	video_urls = sel.css('.talk-link .media__message a::attr(href)').extract()
	video_images=sel.css('.talk-link .media__image img::attr(src)').extract()
	video_date = sel.css('.talk-link .media__message .meta .meta__item .meta__val::text').extract()
	return titles, talker_names, video_urls, video_images,video_date
