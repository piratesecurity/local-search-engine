import urllib
import lxml.html
queue=[]

def find_urls(link):
	connection = urllib.urlopen(link)
	dom =  lxml.html.fromstring(connection.read())
	for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
	    queue.append(link)	
	return queue
