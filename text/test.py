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

res = requests.get('https://m.hc360.com/info/')
html_cont = res.text
soup = BeautifulSoup(html_cont, 'lxml')
urls = soup.select('section.navBox > article.IndexNav > ul > li > a')
print(urls)
list_url = urljoin('https://m.hc360.com/info-machine/', urls.pop(-1).get('href'))
res = requests.get(list_url)
html_cont = res.text
if html_cont is None:
    print('[parse_first_floor] skip because of 404! link[%s]' % list_url)
soup = BeautifulSoup(html_cont, 'lxml')
urls = soup.select('section > div.ListBox2 > dl > dd > a')
result = [[url.text.replace('行业资讯', ''), urljoin('https://m.hc360.com/info-machine/', url.get('href'))] for url in urls]
print(result)
