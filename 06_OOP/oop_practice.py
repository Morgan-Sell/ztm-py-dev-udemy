#OOP

# The code is only stored in the class.
class BigObject: # Class
	pass

obj1 = BigObject() # instantiate


# Lecture 116
# A class should be singular, e.g., character (NOT characters)
class PlayerCharacter:
	# Class Object Attribute
	# Attribute is static.
	membership = True
	# Call magic or dunder method
	# __init__ is called whenever the class is instantiated.
	def __init__(self, name='anonymous', age=0):
		
		# Can use the class object b/c it is a class object attribute.
		# "self.membership" would also work.
		if age > 18:
			self.name = name
			self.age = age

	def run(self):
		print('run')
	
	def shout(self):
		print(f"My name is {self.name}")
	
	@classmethod
	# Note that the method has "cls".
	# "cls" is analagous to "self".
	# "clas is used in class object method.
	def adding_things(cls, num1, num2):
		return num1 + num2

#player1 = PlayerCharacter('Tom', 10)
# player2 = PlayerCharacter()


# Printing the instance alone, show the menory location of the instance.

# print(player2.shout())




