from utility import multiply, divide
from shopping.more_shopping import shopping_cart

"""
NOTES:
------
- A package is a folder that contains modules.
- caching records the compilation step
- By importing the modules, instead of the function, can prevent name collisions.
- Best to explicit. Avoid using "from module_name import *".
- All Python packages require an __init__ file. The file can contain nothing.
- Steps of importing a module:
    1) Finds the module
    2) Runs the module's code
    3) Saves the code to memory
    
- print(__name__) returns "__main__" no matter the name of the file.
    + "__main__" is the assigned name to the file that is executed.
"""

# returns module object including file path.
#print(utility)
if __name__ == "__main__":
    print(divide(2, 3))
    print(multiply(5, 2))
    print(shopping_cart.buy('apple'))

# Ensures that the module is ran only if it is the "__main__" module.
