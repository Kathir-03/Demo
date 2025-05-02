# Problem 5: Calculate factorial of the code from Program 4
from keylength import keylen
def factorial(n):
    if n == 0:
        return 1  # Bug: factorial of 0 is 1
    else:
        return n * factorial(n-1)

print("Final Answer: " + str(factorial(keylen(1,1))))
print("Final Answer: " + str(factorial(keylen(2,1))))
