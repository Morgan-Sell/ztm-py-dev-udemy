# Regular Expression 3


"""
NOTES:
-----

- plus is a quantifier, meaning as many characters as desired.
  ** e.g., ^[a-zA-Z0-9_.+-]+ <-- no limit to the number of characters after the initial value.

"""

import re



pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "b@b.com"

a = pattern.search(string)
print(a)
