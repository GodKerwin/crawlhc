import random
import time

from crawl import url_manager, html_downloader, html_parser, html_outputer


class Main(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def collect_url(self, root_url):
        try:
            html_cont = self.downloader.download(root_url)
            first_floor = self.parser.parse_first_floor(html_cont, root_url)
            if first_floor is not None:
                for first in first_floor:
                    html_cont = self.downloader.download(first[1])
                    if html_cont is None:
                        print('skip because of 404!')
                        continue
                    second_floor = self.parser.parse_second_floor(html_cont, first[1])
                    if second_floor is not None:
                        for second in second_floor:
                            next_url = second[1]
                            has_next = True
                            while has_next:
                                print('crawl', first[0], '-', second[0], next_url)
                                html_cont = self.downloader.download(next_url)
                                if html_cont is None:
                                    print('break because of 404!')
                                    break
                                urls, next_url, has_next = self.parser.parse_third_floor(html_cont, next_url)
                                self.urls.add_new_urls(urls)
        except:
            print('collect failed')

        self.urls.print_urls()

        # def crawl(self):
        #     count = 1
        #     while self.urls.has_new_url():
        #         try:
        #             new_url = self.urls.get_new_url()
        #             print("crawl", count, ":", new_url)
        #             html_cont = self.downloader.download(new_url)
        #             if html_cont is None:
        #                 print('skip because of 404!')
        #                 count += 1
        #                 continue
        #             new_data = self.parser.parse1(html_cont)
        #             if new_data is None:
        #                 new_url += 'shop/company.html'
        #                 print("crawl", count, ":", new_url)
        #                 html_cont = self.downloader.download(new_url)
        #                 if html_cont is None:
        #                     print('skip because of 404!')
        #                     count += 1
        #                     continue
        #                 new_data = self.parser.parse2(html_cont)
        #             self.outputer.collect_data(new_data)
        #             time.sleep(random.randint(1, 5))
        #             count += 1
        #         except:
        #             count += 1
        #             print('crawl failed')
        #
        #     self.outputer.output_html()


if __name__ == '__main__':
    main = Main()
    root_url = 'https://m.hc360.com/info/'
    main.collect_url(root_url)
    # main.crawl()
