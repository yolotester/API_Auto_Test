#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File:Request.py
@E-mail:364942727@qq.com
@Time:2020/9/5 8:29 下午
@Author:Nobita
@Version:1.0
@Desciption:Request请求封装模块
"""

import requests
from Common.Log import logger


class RunMain():
    def __init__(self):
        self.logger = logger

    def send_post(self, url, headers, data):  # 定义一个方法，传入需要的参数url、headers和data
        # 参数必须按照url、headers、data顺序传入
        headers = headers
        result_data = requests.post(url=url, headers=headers, data=data).json()  # 因为这里要封装post方法，所以这里的url和data值不能写死
        result_json = requests.post(url=url, headers=headers, json=data).json()  # 接口需要json参数提交数据，用这种请求方法
        # res = json.dumps(Log, ensure_ascii=False, sort_keys=True, indent=2)  # 格式化输出
        res = result_data
        return res

    def send_get(self, url, headers, data):
        headers = headers
        result_data = requests.get(url=url, headers=headers, data=data).json()
        result_json = requests.post(url=url, headers=headers, json=data).json()  # 接口需要json参数提交数据，用这种请求方法
        # res = json.dumps(Log, ensure_ascii=False, sort_keys=True, indent=2)  # 格式化输出
        res = result_data
        return res

    def run_main(self, method, url=None, headers=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, headers, data)
            self.logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, headers, data)
            self.logger.info(str(result))
        else:
            print("method值错误！！！")
            self.logger.info("method值错误！！！")
        return result


if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    pass
    # method_post = 'post'
    # url_post = 'http://127.0.0.1:5000/login'
    # data_post = {
    #     "username": "admin",
    #     "password": "a123456"
    # }
    # result_post = RunMain().run_main(method=method_post, url=url_post, data=data_post)
    # print(result_post)
