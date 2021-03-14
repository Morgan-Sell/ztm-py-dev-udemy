# Four Pillars of OOP
# 1) Encapsulation - Contain the data and functions in one class object.
# 2) Abstraction - Only provide the user/machine access to the necessary information. 
# --- All other actions/information are "hidden underneath the hood".


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        return("run")
    
    def speak(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

player1 = PlayerCharacter("andrei", 100)

# An example of abstraction.
# I don't care how speak() is implemented.
print(player1.speak())