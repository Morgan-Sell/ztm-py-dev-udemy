# MRO - Method Resolution Order
# MRO is a rule used by Python to determine which method to run.
# MRO uses depth-first search

"""
Inheritance Diagram
      A
    /   \
  /      \
B         C
  \       /
    \   /
      D
"""

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

#print(D.num)

# dispalys the order of the class
#print(D.mro())

class X: pass
class Y: pass
class Z: pass
class A(X, Y): pass
class B(X, Z): pass
class M(B, A, Z): pass

print(M.mro())
