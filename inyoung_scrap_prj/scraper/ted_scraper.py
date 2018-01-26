import requests
import re

from scrapy.selector import Selector



def fetch_page(url):
	r = requests.get(url)
	return r.text


def latest_talks(page=1):
	ted_url = 'http://www.ted.com/talks?page={0}'.format(page)
	titles, talker_names, video_urls, video_images = talk_from_page(ted_url)
	length = len(titles)
	talks = []
	for i in range(length):
		temp_dict = { 'title':titles[i], 'talker_name':talker_names[i], 'video_url':video_urls[i],'video_image' :video_images[i]}
		#print([titles[i],talker_names[i], video_urls[i], video_images[i]])
		talks.append(temp_dict) 

	return talks


def talk_from_page(ted_url):
	html = fetch_page(ted_url)
	sel= Selector(text=html)
	titles = sel.css('.talk-link .media__message a::text').extract()
	talker_names = sel.css('.talk-link .media__message .h12::text').extract()
	video_urls = sel.css('.talk-link .media__message a::attr(href)').extract()
	video_images=sel.css('.talk-link .media__image img::attr(src)').extract()
	return titles, talker_names, video_urls, video_images