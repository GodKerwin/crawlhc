import threading

import pymysql
from DBUtils.PooledDB import PooledDB

from config import config


class DbManager(object):
    __pool = None
    lock = threading.RLock()

    def __init__(self):
        try:
            self._conn = DbManager.__get_conn()
            self._cursor = self._conn.cursor()
        except Exception as e:
            print('Connect failed! ERROR (%s): %s' % (e.args[0], e.args[1]))

    @staticmethod
    def __get_conn():
        if DbManager.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20,
                              host=config.DBHOST,
                              port=config.DBPORT,
                              user=config.DBUSER,
                              passwd=config.DBPWD,
                              db=config.DBNAME,
                              use_unicode=False,
                              charset=config.DBCHAR)
        return __pool.connection()

    # crawl_category
    def save_category(self, categorys):
        sql = 'INSERT INTO crawl_category (pid,cid,`name`,link) VALUES(%s,%s,%s,%s)'
        values = tuple(categorys)
        count = self._cursor.executemany(sql, values)
        self.end()
        return count

    def select_category_by_pid(self, pid):
        sql = 'select * from crawl_category WHERE pid = %d and cid > 0' % pid
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def select_category_by_cid(self, pid, cid):
        sql = 'select * from crawl_category WHERE pid = %d and cid = %d' % (pid, cid)
        self._cursor.execute(sql)
        return self._cursor.fetchone()

    def count_pids(self):
        sql = 'SELECT count(pid) FROM crawl_category WHERE cid = 0'
        self._cursor.execute(sql)
        return self._cursor.fetchone()[0]

    # crawl_news
    def save_url(self, pid, cid, urls):
        try:
            DbManager.lock.acquire()
            sql = 'INSERT IGNORE INTO crawl_news (pid, cid, link) VALUES (%s, %s, %s)'
            values = tuple([[pid, cid, url] for url in urls])
            count = self._cursor.executemany(sql, values)
            self.end()
            return count
        except Exception as e:
            print('[save_url] fail! message[%s]' % e)
        finally:
            DbManager.lock.release()

    def page_news_by_cid(self, pid, cid, offset, size):
        try:
            DbManager.lock.acquire()
            sql = 'select id, link from crawl_news WHERE pid = %d and cid = %d and createAt = 0 order by id limit %d, %d' % (
            pid, cid, offset, size)
            self._cursor.execute(sql)
            results = self._cursor.fetchall()
            result = {}
            for row in results:
                result[row[0]] = row[1]
            return result
        finally:
            DbManager.lock.release()

    def count_news_by_cid(self, pid, cid):
        try:
            DbManager.lock.acquire()
            sql = 'SELECT count(*) FROM crawl_news WHERE pid = %d and cid = %d and createAt = 0' % (pid, cid)
            self._cursor.execute(sql)
            return self._cursor.fetchone()[0]
        finally:
            DbManager.lock.release()

    def update_news(self, values):
        try:
            DbManager.lock.acquire()
            sql = 'UPDATE crawl_news SET `title` = %s, content = %s, createAt = %s WHERE id = %s'
            values = tuple(values)
            count = self._cursor.executemany(sql, values)
            self.end()
            return count
        finally:
            DbManager.lock.release()

    # crawl_recommend
    def begin(self):
        self._conn.autocommit(0)

    def end(self, option='commit'):
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()
