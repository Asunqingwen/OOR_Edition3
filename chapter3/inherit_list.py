# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 0024 10:45
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: inherit_list.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
class ContactList(list):
	def search(self, name):
		"""Return all contacts that contain the search value
		in theri name."""
		matching_contacts = []
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts


class Contact:
	all_contacts = ContactList()

	def __init__(self, name="", email="", **kwargs):
		super().__init__(**kwargs)
		self.name = name
		self.email = email
		Contact.all_contacts.append(self)


class AddressHolder:
	def __init__(self, street="", city="", state="", code="", **kwargs):
		super().__init__(**kwargs)
		self.street = street
		self.city = city
		self.state = state
		self.code = code


class Friend(Contact, AddressHolder):
	def __init__(self, phone="", **kwargs):
		# super(Friend, self).__init__(name, email)
		# Contact.__init__(self, name, email)
		# AddressHolder.__init__(self, street, city, state, code)
		super().__init__(**kwargs)
		self.phone = phone


class LongNameDict(dict):
	def longest_key(self):
		longest = None
		for key in self:
			if not longest or len(key) > len(longest):
				longest = key
		return longest


if __name__ == '__main__':
	# c1 = Contact("John A", "johna@example.net")
	# c2 = Contact("John B", "johnb@example.net")
	# c3 = Contact("Jenna C", "jennac@example.net")
	# print([c.name for c in Contact.all_contacts.search('John')])

	longkeys = LongNameDict()
	longkeys['hello'] = 1
	longkeys['longest yet'] = 5
	longkeys['hello2'] = 'world'
	print(longkeys.longest_key())
