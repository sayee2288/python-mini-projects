'''
This is a binary tree implementation with 
two child nodes per parent and does not allow duplicates
'''


class node:

	def __init__(self, data=None):
		self.data = data
		self.left, self.right = None, None

	def add(self, data):
		if self.data is None:
			self.data = data
		elif data < self.data:
			if self.left is None:
				self.left = node(data)
			else:
				self.left.add(data)
		elif data > self.data:
			if self.right is None:
				self.right = node(data)
			else:
				self.right.add(data)
		else:
			print('Illegal operation - No duplicates allowed in this binary tree')

	def printinorder(self):
		if self.left is not None:
			self.left.printinorder()
		print(self.data)
		if self.right is not None:
			self.right.printinorder()

	def contains(self, data):
		#print(self.data, 'is looking for', data)
		if self.data is None:
			print('Tree is empty')
		elif self.data == data:
			print('Exists!') 
		else:
			if data < self.data and self.left is not None:
				#print('Since {} less than {}' .format(data, self.data))
				self.left.contains(data)
			elif data > self.data and self.right is not None:
				#print('Since {} greater than {}' .format(data, self.data))
				self.right.contains(data)
			else:
				print('Does not exist!')


my_bt = node()

while True:
    x = int(input('\n Please select an \
        operation: 1. insert 2. Search 3. Print: 4. exit\n'))
    if x == 1:
        data = int(input('Please enter the data to place in the list: '))
        my_bt.add(data)
    if x == 2:
        data = int(input('Please enter the value to look for: '))
        my_bt.contains(data)
    if x == 3:
        my_bt.printinorder()
    if x == 4:
        break