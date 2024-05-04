"""
What is a list?
A list is a finite sequence in programming. It is always using square brackets

E.g.
A <- [2,3,5,7,11]

In algorithm, we want to find the first number of whatever list, then we just say A[1] in algorithm
So, for nth position, A[n]

We can also add a number to the end of the list by:

append 9 to A

which results to A = [2,3,5,7,11,9]

Now, try this exercise:
Write down the step-by-step performance for the pseudocode.

A <- [5,7]
for i from 1 to 3
    append 2i to A
end for

Compare the answer in the output from Python:
"""
A = [5,7]
for i in range(len(A) + 2):
    if (i==0):
        continue
    A.append(2*i)
    print("i = " + str(i) + ", A =", str(A))