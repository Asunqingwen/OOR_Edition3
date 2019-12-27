# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 0025 10:11
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: define_exception.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
class InvalidWithdrawal(Exception):
	def __init__(self, balance, amount):
		super().__init__(f"account doesn't have ${amount}")
		self.amount = amount
		self.balance = balance

	def overage(self):
		return self.amount - self.balance


try:
	raise InvalidWithdrawal(50, 26)
except InvalidWithdrawal as e:
	print("I'm sorry,but your withdrawal is more than your balance by "
	      f"${e.overage()}")
