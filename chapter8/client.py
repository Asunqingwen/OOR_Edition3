# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 0007 14:17
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: client.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",2401))
print("Received: {0}".format(client.recv(1024)))
client.close()
