# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 0024 9:30
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: notebook.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import datetime

# store the next available id for all new notes
last_id = 0


class Note:
	"""
	represent a note in the notebook.match against a
	string in searches and store tags for each note.
	"""

	def __init__(self, memo, tags=""):
		"""initialize a note with memo and optional
		space-separated tags.automatically set the note's
		creation date and a unique id."""
		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id

	def match(self, filter):
		"""Determine if this note matches the filter
		text.Return True if it matches,False otherwise.
		Search is case sensitive and matches both text and
		tags."""
		return filter in self.memo or filter in self.tags


class Notebook:
	"""Represent a collection of notes that can be tagged,
	modified,and searched"""

	def __init__(self):
		"""initialize a notebook with an empty list."""
		self.notes = []

	def new_note(self, memo, tags=""):
		"""create a new note and add it to the list."""
		self.notes.append(Note(memo, tags))

	def _find_note(self, note_id):
		"""Locate the note with the given id."""
		for note in self.notes:
			if str(note.id) == str(note_id):
				return note
		return None

	def modify_memo(self, note_id, memo):
		"""Find the note with the given id and change its
		memo to the given value."""
		note = self._find_note(note_id)
		if note:
			note.memo = memo
			return True
		return False

	def modify_tags(self, note_id, tags):
		"""Find the note with the given id and change its
		tags to the given value."""
		note = self._find_note(note_id)
		if note:
			note.tags = tags
			return True
		return False

	def search(self, filter):
		"""Find all notes that match the given filter
		string."""
		return [note for note in self.notes if note.match(filter)]


if __name__ == '__main__':
	n = Notebook()
	n.new_note('hello world')
	n.new_note('hello again')
	print(n.notes)
	print(n.notes[0].id)
	print(n.notes[1].id)
	print(n.notes[0].memo)
	print(n.search("hello"))
	print(n.search("world"))
	n.modify_memo(1, 'hi world')
	print(n.notes[0].memo)
