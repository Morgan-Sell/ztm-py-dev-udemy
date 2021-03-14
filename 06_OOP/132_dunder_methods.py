# Dunder Methods
# dir returns all the methods that apply to the Class object referenced.
# e.g., dir(class_instance)
# In general "del" deletes a variable from a program. Andrei does not recommend using it.

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'yo-yo',
            'has_pets': False
        }
    # change/overwrite dunder method when applied to Toy class
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5
    
    def __del__(self):
        print('deleted!')
    
    def __call__(self):
        return 'yesss??'
    
    # Allows me to use bracket notation.
    def __getitem__(self, idx):
        return self.my_dict[idx]

action_figure = Toy('red', 0)

print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])