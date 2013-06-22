from sys import argv

script, filename = argv

class node:
	def __init__(self,val):
		self.val = val
		self.n = None
		self.e = None
		self.s = None
		self.w = None
		self.ne = None
		self.nw = None
		self.se = None
		self.sw = None


def buildTree(filename):
	last_read = None
	above = None

	f = open(filename)
	line = f.readline()

	for line in f:
		number_list = line.split()
		#process the first line
		if above == None:

			for num in number_list:
				#process first in a line
				if last_read == None:

				#process rest of columns in line
				else:
				int(num)
		#process the rest of the lines
		else:
			for num in number_list:
				int(num)
