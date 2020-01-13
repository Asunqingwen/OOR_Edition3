# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 0002 10:08
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: zip_replace2.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import shutil
import sys
import zipfile
from pathlib import Path

from PIL import Image


class ZipProcessor:
	def __init__(self, zipname):
		self.zipname = zipname
		self.temp_directory = Path(f"unzipped-{zipname[:-4]}")

	def process_zip(self):
		self.unzip_files()
		self.process_files()
		self.zip_files()

	def unzip_files(self):
		self.temp_directory.mkdir()
		with zipfile.ZipFile(self.zipname) as zip:
			zip.extractall(self.temp_directory)

	def zip_files(self):
		with zipfile.ZipFile(self.zipname, 'w') as file:
			for filename in self.temp_directory.iterdir():
				file.write(filename, filename.name)
		shutil.rmtree(self.temp_directory)


class ZipReplace(ZipProcessor):
	def __init__(self, filename, search_string, replace_string):
		super(ZipReplace, self).__init__(filename)
		self.search_string = search_string
		self.replace_string = replace_string

	def process_files(self):
		"""perform a search and replace on all files in the temporary directory"""
		for filename in self.temp_directory.iterdir():
			with filename.open() as file:
				contents = file.read()
			contents = contents.replace(self.search_string, self.replace_string)
			with filename.open('w') as file:
				file.write(contents)


class ScaleZip(ZipProcessor):
	def process_files(self):
		"""Scale each image in the directory to 640x480"""
		for filename in self.temp_directory.iterdir():
			im = Image.open(str(filename))
			scaled = im.resize((640, 480))
			scaled.save(filename)


if __name__ == '__main__':
	ScaleZip(*sys.argv[1:4]).process_zip()