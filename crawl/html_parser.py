from urllib.parse import urljoin

import os

import time
from bs4 import BeautifulSoup

from crawl import html_downloader


class HtmlParser(object):
    def parse_first_floor(self, html_cont, root_url):
        soup = BeautifulSoup(html_cont, 'lxml')
        urls = soup.select('section.navBox > article.IndexNav > ul > li > a')
        result = [[url.text, urljoin(root_url, url.get('href'))] for url in urls]
        result.pop(-1)
        return result

    def parse_second_floor(self, html_cont, root_url):
        soup = BeautifulSoup(html_cont, 'lxml')
        urls = soup.select('section.navBox > article.hyIndexNav > ul > li > a')
        result = [[url.text, urljoin(root_url, url.get('href'))] for url in urls]
        result.pop(-1)
        return result

    def parse_third_floor(self, html_cont, root_url):
        soup = BeautifulSoup(html_cont, 'lxml')
        urls = soup.select('section.newsBox > ul > li.NewsListImg > a')
        urls2 = soup.select('section.newsBox > ul > li.NewsList > div.nListRight > a')
        urls.extend(urls2)
        pages = soup.select('section.newsBox > article.pageBox > span')[0].text
        has_next = (pages.split('/')[0] != pages.split('/')[1])
        next_url = urljoin(root_url, soup.select('section.newsBox > article.pageBox > a:nth-of-type(3)')[0].get('href'))
        return [urljoin(root_url, url.get('href')) for url in urls], next_url, has_next

    def parse_article(self, html_cont):
        soup = BeautifulSoup(html_cont, 'lxml')
        content = ''
        title = soup.select('section.dBox > div.dTopBox > h1')[0].text.strip()
        contents = soup.select('section.dBox > div.dCon > p')
        for p in contents:
            if p.text == '':
                img = p.find('img')
                if img:
                    img_src = img.get('src').strip()
                    img_suffix = os.path.splitext(img_src)[1]
                    img_name = os.path.basename(os.path.splitext(img_src)[0]) + '_' + str(int(time.time())) + img_suffix
                    html_cont = html_downloader.HtmlDownloader().downloadContent(img_src)
                    with open(img_name, 'wb') as f:
                        f.write(html_cont)
                        f.close()
                    print('<p><img src=\'%s\'></p>' % img_name)
            else:
                print('<p>%s</p>' % p.text.strip())
        return title, content
