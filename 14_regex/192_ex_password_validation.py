# Exercise: Password Validation

import re

"""
EXERCISE:
--------
- The password must be >= 8 characters.
- Can contain the following speciali chracters: $%#@
- The ‹^› and ‹$› anchors ensure that the regex matches the entire subject string;
- Must use fullmatch()

"""

pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
password = "morgan1984"

check = pattern.fullmatch(password)


print(check)