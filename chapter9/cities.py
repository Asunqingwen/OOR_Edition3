# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 0008 10:40
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: cities.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import time
from threading import Thread
from urllib.request import urlopen
from xml.etree import ElementTree

CITIES = {
	"Charlottetown": ("PE", "s0000583"),
	"Edmonton": ("AB", "s0000045"),
	"Fredericton": ("NB", "s0000250"),
	"Halifax": ("NS", "s0000318"),
	"Iqaluit": ("NU", "s0000394"),
	"Québec City": ("QC", "s0000620"),
	"Regina": ("SK", "s0000788"),
	"St. John's": ("NL", "s0000280"),
	"Toronto": ("ON", "s0000458"),
	"Victoria": ("BC", "s0000775"),
	"Whitehorse": ("YT", "s0000825"),
	"Winnipeg": ("MB", "s0000193"),
	"Yellowknife": ("NT", "s0000366"),
}


class TempGetter(Thread):
	def __init__(self, city):
		super().__init__()
		self.city = city
		self.province, self.code = CITIES[self.city]

	def run(self) -> None:
		url = (
			"http://dd.weatheroffice.ec.gc.ca/citypage_weather/xml/"
			f"{self.province}/{self.code}_e.xml"
		)
		with urlopen(url) as stream:
			xml = ElementTree.parse(stream)
			self.temperature = xml.find(""
			                            "currentConditions/temperature").text


threads = [TempGetter(c) for c in CITIES]
start = time.time()
for thread in threads:
	thread.run()
	# thread.start() #开并发

# for thread in threads:
# 	thread.join()

for thread in threads:
	print(f"it is {thread.temperature}°C in {thread.city}")

print("Got {} temps in {} seconds".format(len(threads), time.time() - start))
