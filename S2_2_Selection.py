"""
In selection, we let the algorithm decide according to the condition, using "If..., then..." in algorithm
In Python, we use the command "If..., [elif...,] else"

E.g.
For n in natural number, t_n = 2n + 4 if n is even, and t_n = n + 3 if n is odd.

1) Try to write an algorithm the first N terms of this sequences.
2) Demonstrate the algorithm for N = 6 with a table of values.

The following code demonstrate how it works in Python.
"""

n = 1 # Defining n-value
stop = 6
while n <= stop:
    if (n%2==0):
        t_n = 2*n + 4
    else:
        t_n = n + 3
    print("n = " + str(n) + ", t_n = ", t_n)
    n = n + 1
    