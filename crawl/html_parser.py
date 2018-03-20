from urllib.parse import urljoin

from bs4 import BeautifulSoup


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
        title = soup.select('section.dBox > div.dTopBox > h1')[0].text.strip()
        text = soup.select('section.dBox > div.dCon')
