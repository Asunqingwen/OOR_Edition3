# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 0023 11:08
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: first_class.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import math


class MyFirstClass():
	pass


class Point:
	def __init__(self, x, y):
		self.move(x, y)

	def move(self, x, y):
		self.x = x
		self.y = y

	def reset(self):
		self.move(0, 0)

	def calculate_distance(self, other_point):
		return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


if __name__ == '__main__':
	# a = MyFirstClass()
	# b = MyFirstClass()
	# print(a)
	# print(b)
	point1 = Point()
	point2 = Point()

	point1.reset()
	point2.move(5, 0)
	print(point2.calculate_distance(point1))
	assert point2.calculate_distance(point1) == point1.calculate_distance(point2)
	point1.move(3, 4)
	print(point1.calculate_distance(point2))
	print(point1.calculate_distance(point1))
