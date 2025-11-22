class Stack:
	def __init__(self, name="Stack"):
		self.items = []
		self.name = name
	
	def push(self, item):
		self.items.append(item)
		print(f"Pushed {item}")
		self.display()

	def pop(self):
		if not self.is_empty():
			item = self.items.pop()
			print(f"Popped {item}")
			self.display()
			return item
		print("Stack is empty")
		return None
	
	def peak(self):
		if not self.is_empty():
			return self.items[-1]

	def is_empty(self):
		return len(self.items) == 0
	
	def size(self):
		return len(self.items)

	def display(self):
		""" Display stack as a visual diagram"""
		print(f"\n{self.name}:")
		print("┌─────────┐")

		if self.is_empty():
			print("│  EMPTY  │")
		else:
			# Display from top to bottom
			for i in range(len(self.items)):
				item = self.items[i]
				maker = " <--	TOP" if i == len(self.items) - 1 else ""
				print(f"| {str(item):^7}|{maker}")
				if i > 0:
					print("├─────────┤")
	
		print("└─────────┘")
		print(f"Size: {self.size()}\n")
