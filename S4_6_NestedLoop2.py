"""
Try this exercise:

Using pseudocode, write an algorithm to find the positive integer solutions of the equation
43x + 17y + 7z = 200

Here is a python code:
"""
for x in range(1,4):
    for y in range(1,11):
        for z in range(1,28):
            if (43*x + 17*y + 7*z==200):
                print("(" + str(x) + ", " + str(y) + ", " + str(z) + ")")