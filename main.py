# downloading pdfs off UN website
import requests, pickle
from bs4 import BeautifulSoup


# pages from which the download pages can be reached
days_urls = [
	"https://gadebate.un.org/en/listbydate/2018-09-25",
	"https://gadebate.un.org/en/listbydate/2018-09-26",
	"https://gadebate.un.org/en/listbydate/2018-09-27",
	"https://gadebate.un.org/en/listbydate/2018-09-28",
	"https://gadebate.un.org/en/listbydate/2018-09-29",
	"https://gadebate.un.org/en/listbydate/2018-10-01"]


# extracting the urls of the "country pages" from each "day page"
country_urls = []
for each in days_urls:
	response = requests.get(each)
	soup = BeautifulSoup(response.text, "html.parser")

	for link in soup.find_all('a', href=True):
	    if link['href'].startswith("/en/73/"):
	    	country_urls.append("https://gadebate.un.org" + link['href'])


# for each "country page" checking whether there's a download link, if so, extract it
download_urls = []
for each in country_urls:
	response = requests.get(each)
	soup = BeautifulSoup(response.text, "html.parser")

	for link in soup.find_all('a', href=True):
		if "Read the statement in English" in link.getText():
			download_urls.append(link['href'])


"""
# Pickling - written for development purposes
# write to pickle
pickle_out = open("download_urls.pickle", "wb")
pickle.dump(download_urls, pickle_out)
pickle_out.close()

# read from pickle
pickle_in = open("download_urls.pickle", "rb")
download_urls = pickle.load(pickle_in)
"""


# get out last part of download url to use as file name later
named_download_urls = {}
for each in download_urls:
	pdf_title = each.rsplit('/', 1)[-1]
	named_download_urls[pdf_title] = each
# print(named_download_urls)


# download pdfs by writing their return value to file  
for title, url in named_download_urls.items():
	try:
		response = requests.get(url)
		with open("pdfs/" + title, "wb") as f:
			f.write(response.content)
		print("file written out")
	except:
		print("couldnt get title:" + title)
