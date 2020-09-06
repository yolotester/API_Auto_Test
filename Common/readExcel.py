#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File:readExcel.py
@E-mail:364942727@qq.com
@Time:2020/9/3 16:58 上午
@Author:Nobita
@Version:1.0
@Desciption:
"""

import os
import getpathInfo
from xlrd import open_workbook  # 调用读Excel的第三方库xlrd


class readExcel():
    def __init__(self):
        self.path = getpathInfo.get_Path()  # 拿到该项目所在的绝对路径

    def get_xls(self, xls_name, sheet_name):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(self.path, "TestFile", 'case', xls_name)
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        for i in range(nrows):  # 根据行数做循环
            if sheet.row_values(i)[0] != u'case_name':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':  # 我们执行该文件测试一下是否可以正确获取Excel中的值
    print(readExcel().get_xls('learning-API-test_Case.xlsx', 'login'))  # 遍历每一行数据
    print(readExcel().get_xls('learning-API-test_Case.xlsx', 'login')[0][1])  # 登录接口url
    print(readExcel().get_xls('learning-API-test_Case.xlsx', 'login')[1][4])  # 请求method
    # pass
