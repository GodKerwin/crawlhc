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
data1 = soup.select('section.newsBox > ul > li.NewsListImg > h3 > a')
data2 = soup.select('section.newsBox > ul > li.NewsList > div.nListRight > h3 > a')
data1.extend(data2)
print(data1)
data3 = soup.select('section.newsBox > article.pageBox > span')[0]
data4 = soup.select('section.newsBox > article.pageBox > a:nth-of-type(3)')[0]
# print(data3.text.split('/')[0], data3.text.split('/')[1])
# print(urljoin('https://m.hc360.com/info/', data4.get('href')))
for item in data1:
    print('link', urljoin('https://m.hc360.com/info/', item.text))
    print('link', urljoin('https://m.hc360.com/info/', item.get('href')))
