"""
We used if-then block to determine how the algorithm goes, but there are multiple structure in if-then blocks:
1) Basic

if condition then
    follow these instructions
end if

2) Failing the first part of if

if condition then
    follow these instructions
else
    follow these instructions
end if

3) Adding another option
if first condition then
    follow these instructions
else if second condition then
    follow these instructions
else
    follow these instructions
end if

These are the structures of how if conditions are structured

Use pseudocode, write an algorithm to find the maximum of two numbers a and b.

The following code is to show how it performs in Python.
"""

a = int(input("Input your first value: "))
b = int(input("Input your second value: "))

if a>=b:
    print("a won! Its value is",a)
else:
    print("b won! Its value is",b)
