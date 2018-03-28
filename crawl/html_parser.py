import uuid
from urllib.parse import urljoin
import os
from bs4 import BeautifulSoup
from crawl import html_downloader


class HtmlParser(object):
    def parse_first_floor(self, html_cont, root_url):
        soup = BeautifulSoup(html_cont, 'lxml')
        urls = soup.select('section.navBox > article.IndexNav > ul > li > a')
        list_url = urljoin(root_url, urls.pop(-1).get('href'))
        html_cont = html_downloader.HtmlDownloader().download(list_url)
        if html_cont is None:
            print('[parse_first_floor] skip because of 404! link[%s]' % list_url)
            return None
        soup = BeautifulSoup(html_cont, 'lxml')
        urls = soup.select('section > div.ListBox2 > dl > dd > a')
        result = [[url.text.replace('行业资讯', ''), urljoin(root_url, url.get('href'))] for url in urls]
        return result

    def parse_second_floor(self, html_cont, root_url):
        soup = BeautifulSoup(html_cont, 'lxml')
        urls = soup.select('section.navBox > article.hyIndexNav > ul > li > a')
        list_url = urljoin(root_url, urls.pop(-1).get('href'))
        html_cont = html_downloader.HtmlDownloader().download(list_url)
        if html_cont is None:
            print('[parse_second_floor] skip because of 404! link[%s]' % list_url)
            return None
        soup = BeautifulSoup(html_cont, 'lxml')
        urls = soup.select('section > div.ListBox2 > dl > dd > a')
        result = [[url.text, urljoin(root_url, url.get('href'))] for url in urls]
        return result

    def parse_third_floor(self, html_cont, root_url):
        soup = BeautifulSoup(html_cont, 'lxml')
        urls = soup.select('section.newsBox > ul > li.NewsListImg > h3 > a')
        urls2 = soup.select('section.newsBox > ul > li.NewsList > div.nListRight > h3 > a')
        urls3 = soup.select('section.newsBox > ul > li.NewsListImg > a')
        urls4 = soup.select('section.newsBox > ul > li.NewsList > div.nListRight > a')
        urls.extend(urls2)
        urls.extend(urls3)
        urls.extend(urls4)
        pages = soup.select('section.newsBox > article.pageBox > span')[0].text
        has_next = (pages.split('/')[0] != pages.split('/')[1])
        next_url = urljoin(root_url, soup.select('section.newsBox > article.pageBox > a:nth-of-type(3)')[0].get('href'))
        return [urljoin(root_url, url.get('href')) for url in urls], next_url, has_next

    def parse_article(self, html_cont, root_url, pid, cid):
        soup = BeautifulSoup(html_cont, 'lxml')
        content = ''
        title = soup.select('section.dBox > div.dTopBox > h1')[0].text.strip()
        contents = soup.select('section.dBox > div.dCon > p')
        img_no = 1
        for p in contents:
            if p.text == '':
                img = p.find('img')
                if img:
                    img_src = img.get('src').strip()
                    img_dir = './pic/p%d/c%d/' % (pid, cid)
                    img_name = '%s%s' % (uuid.uuid1(), os.path.splitext(img_src)[1])
                    img_full_path = img_dir + img_name
                    if os.path.exists(img_dir) is False:
                        os.makedirs(img_dir)
                    try:
                        html_cont = html_downloader.HtmlDownloader().download_content(img_src)
                        with open(img_full_path, 'wb') as f:
                            f.write(html_cont)
                            f.close()
                        content += '<p><img src=\'%s\'></p>\r\n' % img_full_path
                    except:
                        print('link(%s) img(%s) download fail' % (root_url, img_src))
                    img_no += 1
            else:
                content += '<p>%s</p>\r\n' % p.text.strip().replace('慧聪网', '').replace('慧聪', '')
        return title, content
