from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# res = requests.get('https://m.hc360.com/info/')
# soup = BeautifulSoup(res.text, 'lxml')
# data = soup.select('section.navBox > article.IndexNav > ul > li > a')
# for item in data:
#     print(item)
#     print(urljoin('https://m.hc360.com/info/', item.get('href')))
#
#
# res = requests.get('https://m.hc360.com/info-machine/')
# soup = BeautifulSoup(res.text, 'lxml')
# data = soup.select('section.navBox > article.hyIndexNav > ul > li > a')
# for item in data:
#     print(item)
#     print(urljoin('https://m.hc360.com/info/', item.get('href')))
#

res = requests.get('https://m.hc360.com/info-machine/list/001067-001-1.html')
soup = BeautifulSoup(res.text, 'lxml')
urls = soup.select('section.newsBox > ul > li.NewsListImg > h3 > a')
urls2 = soup.select('section.newsBox > ul > li.NewsList > div.nListRight > h3 > a')
urls3 = soup.select('section.newsBox > ul > li.NewsList > div.nListRight > a')
urls4 = soup.select('section.newsBox > ul > li.NewsList > div.nListRight > a')
urls.extend(urls2)
print(urls)
