"""
Try this exercise too!
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

Write an algorithm that determines the number of digits in the decimal representation of a
given natural number. Show a desk check for the number 7564.

Now, in Python:
"""
def quotient(number, divisor):
    count = 0
    remainder = number
    while remainder >= divisor:
        count = count + 1
        remainder = remainder - divisor

    return count

number = int(input("Input your number: "))
count = 0
print("number = " + str(number) + ", count =",count)
while number > 0:
    number = quotient(number, 10)
    count = count + 1
    print("number = " + str(number) + ", count =",count)