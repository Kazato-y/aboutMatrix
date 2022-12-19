from sympy import *
print("input cubic square matrix")
A = Matrix([input().split() for element in range(3)])
print(A.jordan_form())
