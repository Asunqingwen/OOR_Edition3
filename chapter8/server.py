# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 0007 14:15
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: server.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import gzip
import socket
from io import BytesIO


class LogSocket:
	def __init__(self, socket):
		self.socket = socket

	def send(self, data):
		print(
			"Sending {0} to {1}".format(
				data, self.socket.getpeername()[0]
			)
		)
		self.socket.send(data)

	def close(self):
		self.socket.close()


class GzipSocket:
	def __init__(self, socket):
		self.socket = socket

	def send(self, data):
		buf = BytesIO()
		zipfile = gzip.GzipFile(fileobj=buf, mode="w")
		zipfile.write(data)
		zipfile.close()
		self.socket.send(buf.getvalue())

	def close(self):
		self.socket.close()


def respond(client):
	response = input("Enter a value: ")
	client.send(bytes(response, "utf8"))
	client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 2401))
server.listen(1)
try:
	while True:
		client, addr = server.accept()
		respond(LogSocket(client))
finally:
	server.close()
