# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 0008 15:24
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: pools.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import random
from multiprocessing.pool import Pool

def prime_factor(value):
	factors = []
	for divisor in range(2, value - 1):
		quotient, remainder = divmod(value, divisor)
		if not remainder:
			factors.extend(prime_factor(divisor))
			factors.extend(prime_factor(quotient))
			break
		else:
			factors = [value]
	return factors

if __name__ == '__main__':
	pool = Pool()

	to_factor = [random.randint(100000, 50000000) for _ in range(20)]
	results = pool.map(prime_factor, to_factor)
	for value, factors in zip(to_factor, results):
		print("The factors of {} are {}".format(value, factors))
