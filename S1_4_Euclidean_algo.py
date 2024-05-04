"""
Euclidean's algorithm is one of the quickest way to find the highest common factor (HCF).

Let a and b be integers with b>0, there are unique integers q and r such that:
a = qb + r, where 0 <= r < b

q = quotient
r = remainder of a/b

If a = qb + r, where q and r are intergers, then HCF(a, b) = HCF(b, r).
In Euclidean algorithm, follow the steps below:
1) Define the two values to test on HCF as a and b.
2) Let r be the remainder when a is divided by b
3) If r = 0, go to Step 7
4) Let a have the value of b
5) Let b have the value of r
6) Repeat from Step 2
7) The HCF value is b.

Try executing the following code:
"""
def euclidean_algorithm(a, b):
    steps = []  # List to store steps for the table
    while b:
        steps.append([a, b, a // b, a % b])  # Append current step to the list
        a, b = b, a % b  # Update a and b for the next iteration
    return a, steps  # Return the HCF and steps list

def print_table(steps):
    # Print the table headers
    print("+------+------+----------+----------+")
    print(f"| Step |  a   |    b     |  r       |  q       |")
    print("+------+------+----------+----------+")
    
    # Print each step in the table
    for i, step in enumerate(steps):
        print(f"|  {i+1:<3} | {step[0]:<4} | {step[1]:<8} | {step[2]:<8} | {step[3]:<8} |")
    
    # Print the table footer
    print("+------+------+----------+----------+")

def find_hcf(a, b):
    hcf, steps = euclidean_algorithm(a, b)
    print("Steps of Euclidean Algorithm:")
    print_table(steps)
    print(f"\nHCF of {a} and {b} is: {hcf}")

# Example usage:
num1 = int(input("First value: "))
num2 = int(input("Second value: "))
print(f"Numbers: {num1}, {num2}")
find_hcf(num1, num2)
