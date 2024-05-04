"""
Now try this exercise:
Consider the sequence defined by the rule
x_{n+1} = 5x_n + 4
x_1 = 3

Write an  algorithm that will determine the smallest value of n for which x_n > 10 000.
Show a desk check to test the operation of the algorithm.

This is how the code in Python would be written:
"""

n = 1
x = 3
print("n = " + str(n) + ", x =", str(x))
while x<=10000:
    n = n + 1
    x = 5*x + 4
    print("n = " + str(n) + ", x =", str(x))