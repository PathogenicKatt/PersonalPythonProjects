# Magic Methods

class LocalUniversity:
	def __init__(self, name, province, numb_of_grad, year):
		self.name=name
		self.province= province
		self.numb_of_grad = numb_of_grad
		self.year = year

	def __str__(self):
		return f'The {self.name} is located in {self.province} and had {self.numb_of_grad} graduates in {self.year}.'

	def __contains__(self, keyword):
		return keyword in self.name or keyword in self.province

	def __eq__(self, other):
		return self.name == other.name 

university1 = LocalUniversity("NWU", "North-West", 1000, 2024)
university2 = LocalUniversity("UJ", "Gauteng", 3000, 2024)
university3 = LocalUniversity("Wits", "Gauteng", 900, 2024)

'''
print(university1) # __str__
print("UJ" in university2) # __contains__
print(university1 == university2) # __eq__ 
'''