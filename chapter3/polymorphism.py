# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 0024 13:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: polymorphism.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
from collections import Container


class AudioFile:
	def __init__(self, filename):
		if not filename.endswith(self.ext):
			raise Exception("Invalid file format")
		self.filename = filename


class MP3File(AudioFile):
	ext = "mp3"

	def play(self):
		print("playing {} as map3".format(self.filename))


class WavFile(AudioFile):
	ext = "wav"

	def play(self):
		print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
	ext = "ogg"

	def play(self):
		print("playing {} as ogg".format(self.filename))


class OddContainer:
	def __contains__(self, item):
		if not isinstance(item, int) or not item % 2:
			return False
		return True


if __name__ == '__main__':
	# ogg = OggFile("myfile.ogg")
	# ogg.play()
	# mp3 = MP3File("myfile.mp3")
	# mp3.play()
	# not_an_mp3 = MP3File("myfile.ogg")
	odd_container = OddContainer()
	print(isinstance(odd_container, Container))
	print(1 in odd_container)
	print(2 in odd_container)
	print("hello" in odd_container)
