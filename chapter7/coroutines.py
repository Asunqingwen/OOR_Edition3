# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 0007 10:41
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: coroutines.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
def tally():
	score = 0
	while True:
		increment = yield score
		score += increment


if __name__ == '__main__':
	white_box = tally()
	blue_jays = tally()
	print(next(white_box))
	print(next(blue_jays))
	white_box.send(3)
	blue_jays.send(2)
	white_box.send(2)
	blue_jays.send(4)
