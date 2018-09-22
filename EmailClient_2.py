# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 14:57:56 2018

@author: SQ
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = '592350960@qq.com'
receiver = '813515323@qq.com'
subject = '学生有问题请教'
smtpserver = 'smtp.qq.com'
username = 'shelljo'
password = 'araurzkpquccbbga'
 
msg = MIMEText('老师您好，我是您的学生，今天想要请教你一些问题，请问你有时间吗','plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = '592350960@qq.com'  
msg['To'] = "813515323@qq.com"
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
print("邮件发送成功，请查看……")
