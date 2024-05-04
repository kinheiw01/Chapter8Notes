"""
Try this exercise:
Write an algorithm that assigns a letter grade based on a mark out of 100.

The following code shows how Python is written
"""
mark = int(input("Insert your mark: "))

if mark>100:
    print("Bruh, the total is 100 only. You cheated...")
elif mark>=90:
    print("A")
elif mark >=75:
    print("B")
elif mark >=60:
    print("C")
elif mark >= 50:
    print("D")
else:
    print("E")