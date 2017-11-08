#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 新建一个新的
# 导入模块
from openpyxl import Workbook


class ExcelWriter(object):
    def write(self, fn, sheetsName="first sheet", filename='test.xlsx'):
        # 新建一个工作簿
        wb = Workbook()
        # 拿取第一个工作表
        ws = wb.worksheets[0]
        # 设置这个工作表的名字
        ws.title = sheetsName
        # 写值
        fn(ws)
        # 存储这个工作表
        wb.save(filename=filename)
