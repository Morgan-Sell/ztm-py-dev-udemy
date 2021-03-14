# Inheritance
# Child classes AKA subclasses and derived classes

class User:
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left -{self.num_arrows}")

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
print(wizard1.attack())
print(archer1.attack())

# Check if something is a class instance.
print(isinstance(wizard1, Wizard))