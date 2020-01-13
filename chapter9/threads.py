# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 0008 10:32
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: threads.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
from threading import Thread


class InputReader(Thread):
	def run(self) -> None:
		self.line_of_text = input()


print("Enter some text and press enter:")
thread = InputReader()
thread.start()

count = result = 1
while thread.is_alive():
	result = count * count
	count += 1

print("calculated squares up to {0} * {0} = {1}".format(count, result))
print("while you typed '{}'".format(thread.line_of_text))
