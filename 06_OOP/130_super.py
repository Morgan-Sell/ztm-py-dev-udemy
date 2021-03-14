# super()

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        # super() refers to super or parent class
        # Refers to User
        # removes "self" requisite
        super().__init__(email)
        self.name = name
        self.power = power

    # overrides original attack
    def attack(self):
        User.attack(self)
        print(f"Attacking with power of {self.power}")

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
