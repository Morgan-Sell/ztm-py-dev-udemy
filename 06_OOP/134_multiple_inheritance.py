# Multiple inheritance

# Multiple inheritance can be tricky.
# Must be aware of how the classes were implemented
# Be careful that I'm not overwriting anything
# Some languages do NOT allow multiple inheritance.


class User(object):
    def __init__(self, email):
        self.email = email
        print('init complete')

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    
    def check_arrows(self):
        print(f'{self.arrows} remaining')
    
    def run(self):
        print('ran really fast')

# Can inherit from multiple classes
class HybridBord(Wizard, Archer):
    # Can use this approach to better organize code.
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBord('borgie', 50, 100)
print(hb1.check_arrows())
print(hb1.attack())