import urllib
from bs4 import BeautifulSoup
from collections import Counter
from collections import OrderedDict

#get the url for the page that has a list of all diablo 3 builds
def get_buildlist_url():
	url = "https://www.icy-veins.com/d3/builds"
	return url

#read the page text into python
def get_page_text(url):
	req = urllib.request.Request(url)
	with urllib.request.urlopen(req) as response:
		return response.read()

#for each build on the page, get the url to their associated webpage
def get_build_url(page_text):
	soup = BeautifulSoup(page_text, 'html.parser')
	buildlist_raw = soup.find_all('span', 'd3_build_presentation_title_name')
	build_url_list = []
	for build in buildlist_raw:
		href_tag = build.find('a', href=True)
		build_url = "https:" + href_tag['href']
		build_url_list.append(build_url)
	return build_url_list

#for each item on the specific build's webpage, add them to a list
def get_itemlist(page_text):
	soup = BeautifulSoup(page_text, 'html.parser')
	itemlist_raw = soup.find_all('img', 'd3_icon d3_item')
	itemlist = []
	for item in itemlist_raw:
		item_name = item['alt']
		itemlist.append(item_name)
	return itemlist

#sort the dictionary of all items and their counts in descending order
def sort_dict(dict):
	sorted_dict = OrderedDict(sorted(dict.items(), key=lambda x: x[1], reverse=True))
	return sorted_dict

#main function
def main():
	url = get_buildlist_url()
	page_text = get_page_text(url)
	build_url_list = get_build_url(page_text)
	itemlist_master = []
	#create a master list of all items from each build's webpage
	for build_url in build_url_list:
		try:
			build_page_text = get_page_text(build_url)
			itemlist = get_itemlist(build_page_text)
			for item in itemlist:
				itemlist_master.append(item)
		except:
			print(build_url, 'was not found.')
			pass
	#turn the master list into a dictionary with their respective counts in descending order
	item_counter = dict(Counter(itemlist_master))
	sorted_item_counter = sort_dict(item_counter)
	for item in sorted_item_counter:
		print(item, ':', sorted_item_counter[item])

#run main function
main()
