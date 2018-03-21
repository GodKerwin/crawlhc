import pymysql
from DBUtils.PooledDB import PooledDB

from crawl import config


class DbManager(object):
    __pool = None

    def __init__(self):
        try:
            self._conn = DbManager.__getConn()
            self._cursor = self._conn.cursor()
        except Exception as e:
            print('Connect failed! ERROR (%s): %s' % (e.args[0], e.args[1]))

    @staticmethod
    def __getConn():
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

    def saveUrl(self, category, subcategory, urls):
        sql = 'insert into tb_news (category,subcategory,link) values(%s,%s,%s)'
        values = tuple([[category, subcategory, url] for url in urls])
        count = self._cursor.executemany(sql, values)
        self.end()
        return count

    def selectUrl(self, offset, size):
        sql = 'select id, link from tb_news WHERE createAt = 0 limit %d, %d' % (offset, size)
        self._cursor.execute(sql)
        results = self._cursor.fetchall()
        result = {}
        for row in results:
            result[row[0]] = row[1]
        return result

    def countUrl(self):
        sql = 'select count(*) as `count` from tb_news WHERE createAt = 0'
        self._cursor.execute(sql)
        results = self._cursor.fetchone()
        return results[0]

    def updateNews(self, values):
        sql = 'update tb_news set title = %s, content = %s, createAt = %s where id = %s'
        values = tuple(values)
        count = self._cursor.executemany(sql, values)
        self.end()
        return count

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
