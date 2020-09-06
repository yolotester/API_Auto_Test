#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File:readConfig.py
@E-mail:364942727@qq.com
@Time:2020/9/3 13:58 上午
@Author:Nobita
@Version:1.0
@Desciption:封装读取配置ini文件
"""

import os
import configparser
import getpathInfo


class ReadConfig():
    def __init__(self):
        self.path = getpathInfo.get_Path()  # 调用实例化
        self.config_path = os.path.join(self.path, 'Config', 'Config.ini')  # 这句话是在path路径下再加一级
        self.config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
        self.config.read(self.config_path, encoding='utf-8')

    def get_http(self, name):
        value = self.config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = self.config.get('EMAIL', name)
        return value

    def get_mysql(self, name):  # 写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
        value = self.config.get('DATABASE', name)
        return value


if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))
