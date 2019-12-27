# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 0025 9:39
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: handle_except.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me

import random

some_exceptions = [ValueError, TypeError, IndexError, None]

try:
	choice = random.choice(some_exceptions)
	print("raising {}".format(choice))
	if choice:
		raise choice("An error")
except ValueError:
	print("Caught a ValueError")
except TypeError:
	print("Caught a TypeError")
except Exception as e:
	print("Caught some other error:%s" % e.args)
else:
	print("This code called if there is no exception")
finally:
	print("This cleanup code is always called")
