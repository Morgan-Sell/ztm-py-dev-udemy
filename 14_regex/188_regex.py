# Regular Expression

import re

"""
NOTES:
-----
- Regex is not Python specific.
- Regualar expression returns a match object.
- Match object includes location of the first instance of the specified element.
  ** e.g.,  <re.Match object; span=(17, 21), match='this'>
- If I apply a method to a character/string that does not exist in the string, the method returns an error.

"""

string = "search inside of this text please!"

# MATCH OBJECT
a = re.search("this", string)


# Useful match object methods
print("Span: ", a.span())
print("Start: ", a.start())
print("End: ", a.start())
# returns the part that is the match.
# group() is useful when perform multiply searches
print("Group: ", a.group())


# PATTERN OBJECT
pattern = re.compile("search this")

a = pattern.search(string)
b = pattern.findall(string)
# "pattern" must be exactly the same as "string"
c = pattern.fullmatch(string)
d = pattern.match(string)
print(d)