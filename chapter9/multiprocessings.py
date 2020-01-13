# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 0008 14:25
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: multiprocessings.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import os
import time
from multiprocessing import Process, cpu_count
from threading import Thread


class MuchCPU(Process):
# class MuchCPU(Thread):
	def run(self) -> None:
		print(os.getpid())
		for i in range(200000000):
			pass


if __name__ == '__main__':
	procs = [MuchCPU() for _ in range(cpu_count())]
	t = time.time()
	for p in procs:
		p.start()
	for p in procs:
		p.join()
	print("work took {} seconds".format(time.time() - t))
