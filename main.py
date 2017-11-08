#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 加载读取模块
from ConnectMySQL import ConnectMySQL;
from excel import ExcelWriter;

# 数据库连接配置
testConfig = {
    'host': "localhost",
    'user': "root",
    'password': "123456",
    'db': "job",
    'charset': 'utf8mb4'
}

tableName = 'account'

SQL = "SELECT * from %s" % tableName
data = ConnectMySQL(testConfig).loadDataBaseFromMyServer(SQL=SQL)


def writeIntoExcel(ws):
    for row, rowData in enumerate(data):
        for col, value in enumerate(rowData):
            # 因为下标从0开始，所以要加1
            ws.cell(row=row + 1, column=col + 1, value='%s' % value)


ExcelWriter().write(writeIntoExcel, sheetsName="first", filename='123.xlsx')
print('写入完成')
