# Problem 5: Calculate factorial of the code from Program 4
def factorial(n):
    if n == 0:
        return 0  # Bug: factorial of 0 is 1
    else:
        return n * factorial(n-1)

print("Final Answer: " + str(factorial(35)))
