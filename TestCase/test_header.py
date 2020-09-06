#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File:test_header.py
@E-mail:364942727@qq.com
@Time:2020/9/3 11:28 下午
@Author:Nobita
@Version:1.0
@Desciption:/headers接口的测试用例及断言
"""

import json
import unittest
import paramunittest
from Common import readExcel, geturlParams
from Common.Assert import Assertions
from Common.Request import RunMain

url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('learning-API-test_Case.xlsx', 'header')


@paramunittest.parametrized(*login_xls)
class test_learning_API(unittest.TestCase):

    def setParameters(self, case_name, path, headers, data, method):
        """
        set params
        :param case_name:
        :param path
        :param headers
        :param data
        :param method
        :return:
        """
        self.case_name = case_name
        self.path = path
        self.headers = headers
        self.data = data
        self.method = method

    def description(self):
        """
        test report description
        :return:
        """
        print(self.case_name)

    def setUp(self):
        """

        :return:
        """
        print("测试开始，测试用例名称：{}".format(self.case_name))

    def test_header(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test Log
        :return:
        """
        request_url = url + self.path
        headers = self.headers
        new_headers = json.loads(headers)
        info = RunMain().run_main(method=self.method, url=request_url, headers=new_headers
                                  )  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        print('接口响应报文：{}'.format(info))  # 在report中打印响应报文
        # 对响应结果进行断言
        if self.case_name == 'header_pass':
            Assertions().assert_code(info['code'], 10200)
            Assertions().assert_in_text(info['message'], 'ok')


if __name__ == "__main__":
    # unittest.main()
    pass
