import time
import traceback

from crawl import url_manager, html_downloader, html_parser, html_outputer, db_manager


class Main(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.db = db_manager.DbManager()

    def collect_category(self, root_url):
        try:
            pid = 1
            html_cont = self.downloader.download(root_url)
            first_floor = self.parser.parse_first_floor(html_cont, root_url)
            for first in first_floor:
                categorys = []
                cid = 1
                categorys.append([pid, 0, first[0], first[1]])
                html_cont = self.downloader.download(first[1])
                if html_cont is None:
                    print('[collect_category] skip %s %s because of 404!' % (first[0], first[1]))
                    continue
                print('[collect_category] collect %s %s' % (first[0], first[1]))
                second_floor = self.parser.parse_second_floor(html_cont, first[1])
                for second in second_floor:
                    categorys.append([pid, cid, second[0], second[1]])
                    cid += 1
                pid += 1
                self.db.save_category(categorys)
        except:
            traceback.print_exc()
            print('[collect_category] collect_category failed')

    def crawl_all(self):
        for pid in range(self.db.count_pids()):
            self.crawl_by_pid(pid + 1)

    def crawl_by_pid(self, pid):
        types = self.db.select_category_by_pid(pid)
        for type in types:
            self.collect_url(pid, type[1], type[3])
            self.crawl_news(pid, type[1])

    def crawl_by_cid(self, pid, cid):
        type = self.db.select_category_by_cid(pid, cid)
        self.collect_url(pid, cid, type[3])
        self.crawl_news(pid, cid)

    def collect_url(self, pid, cid, link):
        try:
            next_url = link.decode('utf-8')
            has_next = True
            while has_next:
                print('crawl', pid, '-', cid, next_url)
                html_cont = self.downloader.download(next_url)
                if html_cont is None:
                    print('[collect_url] stop because of 404!')
                    break
                urls, next_url, has_next = self.parser.parse_third_floor(html_cont, next_url)
                self.db.save_url(pid, cid, urls)
        except:
            traceback.print_exc()
            print('[collect_url] collect_url failed')

    def crawl_news(self, pid, cid):
        try:
            offset = 0
            page_size = 20
            total = self.db.count_news_by_cid(pid, cid)
            print('[crawl_news] crawl article total %d' % total)
            while offset < total:
                values = []
                url_map = self.db.page_news_by_cid(pid, cid, 0, page_size)
                print('[crawl_news] crawl article pid(%d) cid(%d) page(%d - %d)' % (
                pid, cid, offset + 1, offset + page_size))
                for id in url_map:
                    html_cont = self.downloader.download(url_map[id])
                    if html_cont is None:
                        print('[crawl_news] skip because of 404!')
                        continue
                    title, content = self.parser.parse_article(html_cont, url_map[id], pid, cid)
                    values.append([title, content, int(time.time()), id])
                self.db.update_news(values)
                offset += page_size
        except:
            traceback.print_exc()
            print('[crawl_news] crawl_news failed')


if __name__ == '__main__':
    main = Main()
    try:
        root_url = 'https://m.hc360.com/info/'
        # main.collect_category(root_url)
        main.crawl_by_cid(10, 6)
        # main.crawl_by_pid(1)
        # main.crawl_all()
    finally:
        main.db.dispose()
