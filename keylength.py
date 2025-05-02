# Problem 4: Multiply the length of the reversed key with 5
from reverse import reverse_
def keylen(a,b):
    key = reverse_(a,b)
    length = len(key)
    result = length * 5  # Bug: string multiplication instead of int
    return result


