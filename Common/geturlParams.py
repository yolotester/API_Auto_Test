#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File:geturlParams.py
@E-mail:364942727@qq.com
@Time:2020/9/3 9:28 下午
@Author:Nobita
@Version:1.0
@Desciption:获取配置文件中拼接后的URL
"""

from Config import readConfig as readConfig


class geturlParams():  # 定义一个方法，将从配置文件中读取的进行拼接
    def __init__(self):
        self.readconfig = readConfig.ReadConfig()

    def get_Url(self):
        new_url = self.readconfig.get_http('scheme') + '://' + self.readconfig.get_http(
            'baseurl') + ':' + self.readconfig.get_http(
            'port')
        # logger.info('new_url'+new_url)
        return new_url


if __name__ == '__main__':  # 验证拼接后的正确性
    print(geturlParams().get_Url())
    # pass
