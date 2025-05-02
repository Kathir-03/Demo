# Problem 2: Fix the bug and use the passcode from Program 1.
from addnumbers import add_numbers
code = add_numbers(7,3) # enter 10
if code % 2 == 0:
    print("Keyword: evenkey")
else:
    print("Keyword: oddkey")
