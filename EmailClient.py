# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 12:48:07 2018

@author: SQ
"""

import smtplib
#from email import encoders
from email.header import Header
from email.mime.text import MIMEText
#from email.utils import parseaddr, formataddr

def send_email(from_addr,to_addr,subject,password):
    msg=MIMEText("大家好啊",'plain','utf-8')
    msg['From']=from_addr
    msg['To']=to_addr
    msg['Subject']=Header(subject,'utf-8')
    
    smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtp.set_debuglevel(1)
    smtp.ehlo("smtp.qq.com")
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, to_addr, msg.as_string())


if __name__ == "__main__":
    # 这里的密码是开启smtp服务时输入的客户端登录授权码，并不是邮箱密码
    # 现在很多邮箱都需要先开启smtp才能这样发送邮件
    send_email(u"592350960@qq.com",u"wywushaoqiang@163.com",u"放假通知",u"araurzkpquccbbga")
    print("发送成功....")