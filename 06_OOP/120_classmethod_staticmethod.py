# @classmethod and @ staticmethod

# A class should be singular, e.g., character (NOT characters)
class PlayerCharacter:
	# Class Object Attribute
	# Attribute is static.
    membership = True
	# Call magic or dunder method
	# __init__ is called whenever the class is instantiated.
    def __init__(self, name, age):
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
        return cls('Teddy', num1 + num2)

    @staticmethod
    # static method works similar to a class method
    # except static methods do not have access to "cls"
    # use a static method when I do NOT care about the class state.
    def addding_things2(num1, num2):
        return num1 + num2

# I can execute a class method without instatiated the class.
# Class method are not used too often.
#print(PlayerCharacter.adding_things(2,3))

# Class methods allow me to instatiate while executing the method.
player3 = PlayerCharacter.adding_things(2,3)
print(player3.age)



