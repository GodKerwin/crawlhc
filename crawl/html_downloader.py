import random

import requests


class HtmlDownloader(object):
    def __init__(self):
        self.UA_list = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; GWX:MANAGED)',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; GWX:MANAGED)'
        ]
        self.proxies_list = [{'proxy': 'http:\\10.220.70.254:808'}, {'proxy': 'http:\\10.221.70.254:808'},
                             {'proxy': 'http:\\10.222.70.254:808'}, {'proxy': 'http:\\10.223.70.254:808'}]
        self.headers = {'User-Agent': random.choice(self.UA_list), 'Referer': 'https://www.hc360.com/'}

    def download(self, url):
        if url is None:
            return None
        response = requests.get(url, headers=self.headers, proxies=random.choice(self.proxies_list), timeout=60)
        if response.status_code != 200:
            return None
        return response.text

    def downloadContent(self, url):
        if url is None:
            return None
        response = requests.get(url, headers=self.headers, proxies=random.choice(self.proxies_list), timeout=60)
        if response.status_code != 200:
            return None
        return response.content