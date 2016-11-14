class Parent():
	"""docstring for Parent"""
	def __init__(self, last_name, eye_color):
		# super(Parent, self).__init__()
		print("Parent constructed")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print('Last name:'+ self.last_name)
		print('Eye color:'+ self.eye_color)


class Child(Parent):
	"""docstring for Child"""
	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child constructed")
		Parent.__init__(self, last_name, eye_color)
		# super(Child, self).__init__()
		self.number_of_toys = number_of_toys

	def show_info(self):
		print('Last name:'+ self.last_name)
		print('Eye color:'+ self.eye_color)
		print('Number of toy:'+ str(self.number_of_toys))
		

# billy_cyrus = Parent ("Cyrus", "blue")
milly_cyrus = Child ("Cyrus", "blue", 5)
# print(milly_cyrus.last_name)
# print(milly_cyrus.number_of_toys)
milly_cyrus.show_info()