# Problem 1: Fix the bug to get the correct result.
def add_numbers(a, b):
    return a + b

result = add_numbers(7, "3")  # Bug: adding int + string
print("Passcode: " + result)
