# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 0024 11:17
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: diamond_inherit.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
class BaseClass:
	num_base_calls = 0

	def call_me(self):
		print("Calling method on Base Class")
		self.num_base_calls += 1


class LeftSubClass(BaseClass):
	num_left_calls = 0

	def call_me(self):
		# BaseClass.call_me(self)
		super().call_me()
		print("Calling method on Left Subclass")
		self.num_left_calls += 1


class RightSubClass(BaseClass):
	num_right_calls = 0

	def call_me(self):
		# BaseClass.call_me(self)
		super().call_me()
		print("Calling method on Right Subclass")
		self.num_right_calls += 1


class SubClass(LeftSubClass, RightSubClass):
	num_sub_calls = 0

	def call_me(self):
		# LeftSubClass.call_me(self)
		# RightSubClass.call_me(self)
		super().call_me()
		print("Calling method on Subclass")
		self.num_sub_calls += 1


if __name__ == '__main__':
	s = SubClass()
	print(s.call_me())
	print(s.num_sub_calls, s.num_left_calls, s.num_right_calls, s.num_base_calls)
