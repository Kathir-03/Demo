# Problem 3: Reverse the keyword from the last program
from Evenorodd import evenorodd
def reverse_(a,b):
    word = evenorodd(a,b)
    rev= ""
    for i in word:
        rev = i + rev  # Bug: rev not initialized
    return rev

