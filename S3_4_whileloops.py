"""
While loop is different from for loop. We need to change the number in the condition to terminate the loop.
The structure is:

while condition
    follow these instructions
end while

Try this exercise:
Write an algorithm that divides 72 by 14 and returns the quotient and remainder. Show a
desk check to test the operation of the algorithm.

The following code shows how the structure is in Python:
"""

count = 0 # Extra: Why do you think we need this?
remainder = 72
print("count = " + str(count) + ", remainder =", str(remainder))
while remainder >=14:
    count = count + 1
    remainder = remainder - 14
    print("count = " + str(count) + ", remainder =", str(remainder))
