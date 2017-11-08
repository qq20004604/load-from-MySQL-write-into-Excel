#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入MySQL驱动:
import pymysql


class ConnectMySQL(object):
    def __init__(self, config):
        self.config = config

    def loadDataBaseFromMyServer(self, SQL):
        # 打开数据库连接
        db = pymysql.connect(**self.config)

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        data = None
        try:
            # 使用 execute()  方法执行 SQL 查询
            cursor.execute(SQL)
            # 使用 fetchall() 方法获取所有数据，获取结果是一个二维tuple
            data = cursor.fetchall()
        except BaseException as e:
            print(e)
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()
        return data


if __name__ == '__main__':
    testConfig = {
        'host': "localhost",
        'user': "root",
        'password': "123456",
        'db': "job",
        'charset': 'utf8mb4'
    }
    loadSQL = ConnectMySQL(testConfig)
    SQL = "SELECT * from account"
    print(loadSQL.loadDataBaseFromMyServer(SQL=SQL))
