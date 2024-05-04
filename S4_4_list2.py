"""
Try this exercise now:
You have the following function:

define remainder(number, divisor):
    count <- 0
    remainder <- number
    while remainder >= divisor
        count <- count + 1
        remainder <- remainder - divisor
    end while
    return remainder

Write a function that returns a list of all the factors of a given natural number.

Let's see how it's structure in Python.
"""
def remainder(number, divisor):
    count = 0
    remainder = number
    while remainder>=divisor:
        count = count + 1
        remainder = remainder - divisor
    return remainder

def factors(N):
    A = []
    for i in range(1, N+1):
        if (remainder(N,i)==0):
            A.append(i)
    return A

N = int(input("Input your factor: "))
result = factors(N)
print(str(N))