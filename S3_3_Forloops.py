"""
In for loops, it will keep repeating the instructions until the condition is no longer met.
It will iterate until n iterations, where n is natural number.

The structure in algorithm is:

for i from 1 to n
    follow these instructions
end for

Try the following exericse:
Consider the sequence, 1^2, 2^2, 3^2,..., n^2.
Using pseudocode, write an algorithm to calculate:
1) the sum of the terms in this sequence
2) the product of thes terms in this sequence

with 4 iterations, but after, you can define your own number of iterations.

The following code is how Python's code execute.
"""
def sum_iter(n):
    total_sum = 0
    for i in (range(n+1)):
        if i == 0:
            continue
        total_sum = total_sum + i**2
        print("i = " + str(i) + ", sum =",total_sum)

def mul_iter(n):
    total_mul = 1
    for i in (range(n+1)):
        if i == 0:
            continue
        total_mul = total_mul * i**2
        print("i = " + str(i) + ", product =",total_mul)

n = int(input("Insert your number of times you want to iterate: "))
sum_iter(n)
print("###############################################################")
mul_iter(n)