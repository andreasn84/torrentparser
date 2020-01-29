import requests
from bs4 import BeautifulSoup
import urllib


URL = 'https://ubuntu.com/download/alternative-downloads'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.findAll("a", {"class": "download-torrent"}, href=True)
for a in results:
    url = a['href']
    filename = str(a['href']).split("/")
    filename = (filename[len(filename) - 1])
    urllib.request.urlretrieve(url, "/mnt/data/torrents/" + filename)



