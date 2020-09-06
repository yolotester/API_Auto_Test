#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File:SendEmail.py
@E-mail:364942727@qq.com
@Time:2020/9/5 7:58 下午
@Author:Nobita
@Version:1.0
@Desciption:封装SMTP邮件功能模块
"""

import os
from Config import readConfig
import getpathInfo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from Common.Log import logger


class SendEmail(object):
    def __init__(self):
        # 读取邮件配置信息，初始化参数
        read_conf = readConfig.ReadConfig()
        self.email_service = read_conf.get_email('EMAIL_SERVICE')  # 从配置文件中读取，邮件服务器类型
        self.email_port = read_conf.get_email('EMAIL_PORT')  # 从配置文件中读取，邮件服务器端口
        self.sender_address = read_conf.get_email('SENDER_ADDRESS')  # 从配置文件中读取，发件人邮箱地址
        self.sender_password = read_conf.get_email('SENDER_PASSWORD')  # 从配置文件中读取，发件人邮箱授权码
        self.receiver_address = read_conf.get_email('RECEIVER_ADDRESS')  # 从配置文件中读取，收件人邮箱地址
        self.file_path = os.path.join(getpathInfo.get_Path(), 'Report', 'report.html')  # 获取测试报告路径
        # 日志输出
        self.logger = logger

    def send_email(self):
        # 第三方 SMTP 服务
        message = MIMEMultipart()
        # 创建附件的实例
        message['From'] = Header("测试组", 'utf-8')
        message['To'] = Header(''.join(self.receiver_address), 'utf-8')
        subject = '接口测试邮件'
        message['Subject'] = Header(subject, 'utf-8')
        # 邮件正文内容
        part = MIMEText('Dear all:\n       附件为接口自动化测试报告，此为自动发送邮件，请勿回复，谢谢！', 'plain', 'utf-8')
        message.attach(part)
        # 发送附件
        att1 = MIMEText(open(file=self.file_path, mode='r').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', '接口测试报告.html'))
        message.attach(att1)

        try:

            service = smtplib.SMTP_SSL(self.email_service)
            # service.set_debuglevel(True)  # debug开启或关闭
            service.connect(self.email_service, self.email_port)
            service.login(self.sender_address, self.sender_password)
            service.sendmail(self.sender_address, self.receiver_address, message.as_string())
            print('邮件发送成功')
            service.close()
            self.logger.info("{'邮件发送成功'}")

        except smtplib.SMTPException:
            print("报错，邮件发送失败")
            self.logger.info("{'报错，邮件发送失败'}")


if __name__ == '__main__':
    # SendEmail().send_email()  # 测试邮件功能模块
    pass
