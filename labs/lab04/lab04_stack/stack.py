class Stack():
	def __init__(self):
		self.items = []

	def push(self, node):
		self.items.append(node)

	def pop(self):
		self.items.pop()