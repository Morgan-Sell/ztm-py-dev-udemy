# FUNTIONAL PROGRAMMING (FP)

# FP is all about separation of concens - each part focuses itself on the one thing that it does well.
# OOP is similar
# FP seperates data and functions, unlike OOP which combines methods and attributes.
# Data is acted upon or interacts w/ a function.
# Functions operate on well-defined data structure.

# The pillar of functional programming are pure functions.
### There's a seperation b/t the data and behavior of a program.

# PURE FUNCTION 
# TWO RULES:
# 1. A specific input shuld always return the same output
# 2. A fcn should not produce any side effects, i.e., anything that effects the outside word.
#### e.g., If a function executes "print" within, it is interacting w/ the outside world.
###

# Pure functions are easier to debug. They limit function interdepeendencies.
# Pure funtions are more of a guideline than absolute.

# pure function
def mutiply_by2(lst):
    new_list = []
    for item in lst:
        new_list.append(item*2)
    return new_list

print(mutiply_by2([1, 2, 3]))

# NOT a pure function
def mutiply_by2(lst):
    new_list = []
    for item in lst:
        new_list.append(item*2)
    print(new_list)

mutiply_by2([1, 2, 3])

# NOT a pure function
new_list = []
def mutiply_by2(lst):
    
    for item in lst:
        new_list.append(item*2)
    return new_list

print(mutiply_by2([1, 2, 3]))