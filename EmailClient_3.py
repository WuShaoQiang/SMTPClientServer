# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 15:46:47 2018

@author: SQ
"""

from socket import *
msg='I Love Computer Networking'
endmsg="\r\n.\r\n"
mailServer = "smtp.qq.com"
user_BASE64="NTkyMzUwOTYwQHFxLmNvbQ=="
pass_BASE64="c2JjbGdweXh4bmZjYmViYw=="

clientSocket = socket(AF_INET,SOCK_STREAM)   #IPv4  TCP
clientSocket.connect((mailServer,25))
recv = clientSocket.recv(1024).decode('utf-8')
print(recv)
if recv[:3] != '220':
    print('220 reply not recevied from server')
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode('utf-8')
print(recv1)
if recv1[:3] != '250':
    print('250 reply not recevied from server')
login='auth login'
clientSocket.send(login.encode())
recv2 = clientSocket.recv(1024).decode('utf-8')
print(recv2)
