import urllib
import urllib2
import custom_config
import get_urls
import string

url_queue=[]

external_url_queue=[]

base_url=custom_config.base_url

url_queue.append(base_url)

urls=get_urls.find_urls(base_url)

file_list=open("files.txt","w")

def url_filtering(urls):
	for url in urls:
		url=string.strip(url)
		if "http" not in url:
			try:
				if url[0] !="/":
					url=base_url+"/"+url
				else:
					url=base_url+url
			except IndexError:
				leave=1
		if url not in url_queue:
			url_parts=url.split(".")
			file_extension=url_parts[-1]
			if file_extension not in custom_config.file_types:
				if base_url in url:
					if '#' not in url:
						print url		
						url_queue.append(url)
				else:
					external_url_queue.append(url)
			else:
				file_list.write(url+"\n")




url_filtering(urls)



for url in url_queue:
	try:
		urls=get_urls.find_urls(url)
		url_filtering(urls)	
			
	except IOError:
		leave=1


for url in url_queue:
	print url
