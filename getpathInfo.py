#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File:getpathInfo.py
@E-mail:364942727@qq.com
@Time:2020/9/3 7:58 下午
@Author:Nobita
@Version:1.0
@Desciption:获取项目的文件路径
"""

import os


def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


if __name__ == '__main__':  # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())
