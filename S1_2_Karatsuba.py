"""
To find the product of a pair of two-digit numbers:
m = 10a + b
n = 10c + d

Karatsuba's multiplication algorithm is actually one of the most efficient way
1) Calculate ac. Call the result F
2) Calculate bd. Call the result G
3) Calculate (a + b)(c + d). Call the result H
4) Calculate H - F - G. Call the result K
5) Calculate 100F + 10K + G

In this method, we only require three individual multiplication!

Here is the prove of why Karatsuba's method work.
100F + 10K + G  = 100ac + 10(H - F - G) + bd
                = 100ac + 10(ac + ad + bc + bd - ac - bd) + bd
                = 100ac + 10(ad + bc) + bd
                = (10a + b)(10c + d)
                = mn

Try to run the code below. You will required to input some value.
"""

import sys

m = input("Please input a value for the first number to multiply (It must be two digit): ")
n = input("Please input a value for the second number to multiply (It must be two digit): ")
if (len(m)>2 or len(n)>2 or (int(n[0])==0) or (int(m[0])==0)):
    print("\nERROR, REPORT ERROR. LENGTH OF THE VALUE IS TOO HIGHT. TERMINATING")
    raise SystemExit

a = int(m[0])
b = int(m[1])
c = int(n[0])
d = int(n[1])

F = a * b
G = c * d
H = (a + b)*(c + d)
K = H - F - G
result = 100*F + 10*K + G
print("a = ",a)
print("b = " + str(b))
print("c = ",c)
print("d = ",d)
print("F = a * b = " + str(F))
print("G = b * d = ",G)
print("H = (a + b)*(c + d) = ",H)
print("K = H - F - G = ",K)
print("Result = ",result)
####################
# Here shows the checker of Karatsuba's method
if (result == (int(m) * int(n))):
    print("YAYYYYYY, IT WORKED")
else:
    print("Hold up, wait a min..., you found the bug of this algorithm in textbook... This is not the perfect algorithm!")