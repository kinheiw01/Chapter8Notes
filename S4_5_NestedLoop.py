"""
What is a nested loop?
A nested loop is when you have one or multiple loop outer and inner

Look at this example:
c <- 0
for a from 1 to 2
    for b from 1 to 4
        c <- c + 1
    end for
end for

Here is the code that generates the table!
"""
print("|   a   |   b   |   c   |")
print("|-------|-------|-------|")
c = 0
for a in range(1, 3):
    for b in range(1, 5):
        c += 1
        print(f"|   {a}   |   {b}   |   {c}   |")
