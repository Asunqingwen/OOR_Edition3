# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 0007 15:18
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: observe.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
class Inventory:
	def __init__(self):
		self.observers = []
		self._product = None
		self._quantity = 0

	def attach(self, observer):
		self.observers.append(observer)

	@property
	def product(self):
		return self._product

	@product.setter
	def product(self, value):
		self._product = value
		self._update_observers()

	@property
	def quantity(self):
		return self._quantity

	@quantity.setter
	def quantity(self, value):
		self._quantity = value
		self._update_observers()

	def _update_observers(self):
		for observer in self.observers:
			observer()


class ConsoleObserver:
	def __init__(self, inventory):
		self.inventory = inventory

	def __call__(self):
		print(self.inventory.product)
		print(self.inventory.quantity)


if __name__ == '__main__':
	i = Inventory()
	c1 = ConsoleObserver(i)
	c2 = ConsoleObserver(i)
	i.attach(c1)
	i.attach(c2)
	i.product = "Widget"
	i.quantity = 5
