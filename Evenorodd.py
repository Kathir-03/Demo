# Problem 2: Fix the bug and use the passcode from Program 1.

def evenorodd(a,b):
    from addnumbers import add_numbers
    code = add_numbers(a,b) # enter 10
    if code % 2 == 0:
        return "evenkey"
    else:
        return "oddkey"
