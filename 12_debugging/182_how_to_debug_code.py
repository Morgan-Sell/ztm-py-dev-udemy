# Debugging

import pdb
"""
pdb:
-----
- pdb.set_trace() returns an interactive python debugger where I can test commands.
- step - moves to the next line of code.
- Must move pass the variables using "step" to reference them in interactive debugger.
- "continue" moves through the code until the function returns a value/object/variable.
- "a" returns all of the arguments within the function.
- "w" shows the context of the current line.
"""
def add (num1, num2):

    pdb.set_trace()
    return num1 + num2

add(4, 5)
