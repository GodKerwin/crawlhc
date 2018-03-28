import datetime
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
import sys
import os

sys.path.append(os.getcwd())
from crawl import html_downloader, html_parser, db_manager


class Main(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.db = db_manager.DbManager()

    def collect_category(self, root_url):
        try:
            print('[collect_category] begin!!!')
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
            print('[collect_category] failed')
        finally:
            print('[collect_category] end!!!')

    def crawl_all(self):
        print('[crawl_all] begin!!!')
        for pid in range(1, self.db.count_pids() + 1):
            self.crawl_by_pid(pid)
        print('[crawl_all] end!!!')

    def crawl_by_pid(self, pid):
        print('%s [crawl_by_pid] begin!!!' % threading.current_thread().name)
        types = self.db.select_category_by_pid(pid)
        # pool = ThreadPoolExecutor(10)
        for type in types:
            self.collect_and_crawl(pid, type[1], type[3])
            # pool.submit(self.collect_and_crawl, pid, type[1], type[3])
        # pool.shutdown(wait=True)

        print('%s [crawl_by_pid] end!!!' % threading.current_thread().name)

    def crawl_by_cid(self, pid, cid):
        print('[crawl_by_cid] begin!!!')
        type = self.db.select_category_by_cid(pid, cid)
        self.collect_and_crawl(pid, cid, type[3])
        print('[crawl_by_cid] end!!!')

    def collect_and_crawl(self, pid, cid, link):
        # print('thread[%s] pid[%d] cid[%d] link[%s]' % (threading.current_thread().name, pid, cid, link))
        try:
            print('%s [collect_url] begin!!!' % threading.current_thread().name)
            next_url = link.decode('utf-8')
            has_next = True
            while has_next:
                print('%s [collect_url] crawl' % threading.current_thread().name, pid, '-', cid, next_url)
                html_cont = self.downloader.download(next_url)
                if html_cont is None:
                    print('[collect_url] stop because of 404!')
                    break
                urls, next_url, has_next = self.parser.parse_third_floor(html_cont, next_url)
                self.db.save_url(pid, cid, urls)
            self.crawl_news(pid, cid)
        except:
            traceback.print_exc()
            print('%s [collect_url] failed' % threading.current_thread().name)
        finally:
            print('%s [collect_url] end!!!' % threading.current_thread().name)

    def crawl_news(self, pid, cid):
        # print('thread[%s] pid[%d] cid[%d]' % (threading.current_thread().name, pid, cid))
        try:
            print('%s [crawl_news] start!!!' % threading.current_thread().name)
            offset = 0
            page_size = 20
            total = self.db.count_news_by_cid(pid, cid)
            while offset < total:
                insert_values = []
                update_values = []
                url_map = self.db.page_news_by_cid(pid, cid, 0, page_size)
                print('%s [crawl_news] crawl article pid(%d) cid(%d) page(%d - %d) total(%d)' % (
                    threading.current_thread().name, pid, cid, offset + 1, offset + page_size, total))
                for id in url_map:
                    html_cont = self.downloader.download(url_map[id])
                    if html_cont is None:
                        print('%s [crawl_news] skip because of 404!' % threading.current_thread().name)
                        continue
                    title, content = self.parser.parse_article(html_cont, url_map[id], pid, cid)
                    update_values.append([int(time.time()), id])
                    insert_values.append([url_map[id], title, content])
                self.db.update_news(update_values)
                self.db.save_news_content(insert_values)
                offset += page_size
        except:
            traceback.print_exc()
            print('%s [crawl_news] failed' % threading.current_thread().name)
        finally:
            print('%s [crawl_news] end!!!' % threading.current_thread().name)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    print('[main] start!!! %s' % start_time)
    main = Main()
    try:
        root_url = 'https://m.hc360.com/info/'
        if len(sys.argv) == 1:
            print('全爬取模式')
            main.collect_category(root_url)
            main.crawl_all()
        elif len(sys.argv) == 2:
            print('pid[%s]爬取模式' % sys.argv[1])
            main.crawl_by_pid(int(sys.argv[1]))
        elif len(sys.argv) == 3:
            print('pid[%s],cid[%s]爬取模式' % (sys.argv[1], sys.argv[2]))
            main.crawl_by_cid(int(sys.argv[1]), int(sys.argv[2]))
    finally:
        end_time = datetime.datetime.now()
        main.db.dispose()
        print('[main] end!!! %s' % end_time)
        print('共运行%d秒' % (end_time - start_time).seconds)
