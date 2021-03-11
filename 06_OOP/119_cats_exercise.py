# Cat object exercise

# Given the below class:
class Cat():
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instaniate the Cat object w/  3 cats.
cat1 = Cat('Robin Hood', 101)
cat2 = Cat('Raphael', 493)
cat3 = Cat('Autumn Cloud', 9)

# Create a function that finds the oldest cat
def find_oldest_cat(*cats):
    max_age = 0
    oldest_cat = None

    for cat in cats:
        if cat.age > max_age:
            oldest_cat = cat.name
            max_age = cat.age
    return max_age

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

max_age = find_oldest_cat(cat1, cat2, cat3)
print (f"The oldest cat is {max_age} years old.")