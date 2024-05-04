"""
In this part, we will be learning to change between decimal system and binary system.
A decimal system contains numbers 0,1,2,3,4,5,6,7,8,9
A binary system contains numbers 0,1 only
Do we have a system that is higher than decimal system? Yes we do! We have octal and Hexadecimal.

E.g. we have 352 in decimal number system. We call this base 10. We can put the position:
352 = (3 × 10^2) + (5 × 10^1) + (2 × 10^0)

However, in binary system, we represent things in 0, 1, and we call this base 2. We can put the following
number in this position:
110101 = (1 × 2^5) + (1 × 2^4) + (0 × 2^3) + (1 × 2^2) + (0 × 2^1) + (1 × 2^0)
The RHS of the equation shows the value in base 10, hence, we now know how to convert from binary to decimal!
#######################################################
Now we do conversion between decimal to binary
For example, we know 53's binary is 110101, but how does it work?
Print the following code to show the table how it works!
PS: This is generated from ChatGPT cuz I am too lazy :). BUT I KNOW HOW TO WRITE THE CODE
"""
def decimal_to_binary(decimal_num):
    binary_digits = []  # List to store binary digits

    # Initialize the table
    print("+----------------------+")
    print("| Division | Quotient | Remainder |")
    print("+----------+----------+-----------+")

    # Convert decimal to binary iteratively
    while decimal_num > 0:
        quotient = decimal_num // 2  # Get the quotient
        remainder = decimal_num % 2  # Get the remainder when divided by 2
        binary_digits.insert(0, remainder)  # Insert the remainder at the beginning of the list
        
        # Print the division, quotient, and remainder in the table format
        print(f"| {decimal_num:>8} | {quotient:>8} | {remainder:>9} |")
        
        decimal_num = quotient  # Update the decimal number for the next iteration

    # Close the table
    print("+----------+----------+-----------+")

    # Print the binary representation
    binary_str = ''.join(map(str, binary_digits))
    print(f"The binary representation is: {binary_str}")

# Example usage:
decimal_number = int(input("Insert the value you want to convert from decimal to binary: "))
print(f"Decimal number: {decimal_number}")
decimal_to_binary(decimal_number)
