# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 0024 14:09
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: abstract_base_class.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import abc


class MediaLoader(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def play(self):
		pass

	@abc.abstractmethod
	def ext(self):
		pass

	@classmethod
	def __subclasshook__(cls, C):
		if cls is MediaLoader:
			attrs = set(dir(C))
			print(attrs)
			if set(cls.__abstractmethods__) <= attrs:
				return True
		return False


class Ogg():
	ext = ".ogg"

	def play(self):
		pass


if __name__ == '__main__':
	o = Ogg()
