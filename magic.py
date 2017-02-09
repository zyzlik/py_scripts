import re

class Everything(object):
	"""docstring for Everything"""
	def __init__(self):
		pass

	def __eq__(self, other):
		return True

	def __ne__(self, other):
		return True

	def __lt__(self, other):
		return True

	def __gt__(self, other):
		return True

	def __ge__(self, other):
		return True

	def __le__(self, other):
		return True					

def cmp(arg):
	object = Everything()
	return object

print cmp(re) >= re
		