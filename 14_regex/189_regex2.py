# Regular Expressions 2

import re

"""
NOTES:
-----

- sets - uses brackets. Returns a match for any integer character.
  ** e.g., [0-5][0-9] returns a martch for any 2-digit number(s) from 0 to 59.
  ** e.g., [a-zA-Z] returns a match for any alphabetical character between "a" and "z", lower OR upper case.

- r = raw string

"""

pattern = re.compile(r"([a-zA-Z]).([a])")
string = "search inside of this text please!"

a = pattern.search(string)
# returns "sea" b/c it searches for a letter folowed by anything followed by "a".
print(a.group())