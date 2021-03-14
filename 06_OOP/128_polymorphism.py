# POLYMORPHISM

# Object classes can share the same method name...
# ... BUT the method can act differently depending on which method calls it.
# Can customize classes to their needs.
# Ability to redefine methods

class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    # overrides original attack
    def attack(self):
        User.attack(self)
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left: {self.num_arrows}")

wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

# attack() returns a different result depending on the class
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

# for char in [wizard1, archer1]:
#     char.attack()