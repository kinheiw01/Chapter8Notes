"""
We must learn to define a function! Including defining what are the inputs.

Here is one of the structure for quotient:

define quotient(number, divisor):
    count <- 0
    remainder <- number
    while remainder >= divisor
        count <- count + 1
        remainder <- remainder - divisor
    end while
    return count

Notice that it has return in thsi function, hence that means we will be returning it to the main codespace
If you are not using it, just don't return anything because it is just waste of energy for the computer...
The time span between including extra code and no extra code space may be small
However, it is easier for us to follow without extra non-useful code.

Try this exercise:
You are given two defined functions

define quotient(number, divisor):
    count <- 0
    remainder <- number
    while remainder >= divisor
        count <- count + 1
        remainder <- remainder - divisor
    end while
    return count

&

define remainder(number, divisor):
    count <- 0
    remainder <- number
    while remainder >= divisor
        count <- count + 1
        remainder <- remainder - divisor
    end while
    return remainder

Write an algorithm that computes the sum of all the integers from 1 to 1000 that are
divisible by 2 or 3.

Here is the code in Python:
"""

def remainder(number, divisor):
    count = 0
    remainder = number
    while remainder>=divisor:
        count = count + 1
        remainder = remainder - divisor
    
    return remainder

sum = 0
for i in range(1000):
    if ((remainder(i,2)==0) or (remainder(i,3))):
        sum = sum + i
        print(str(sum))

print(str(sum))