# Problem 3: Reverse the keyword from the last program
def reverse(word):
    for i in word:
        rev = i + rev  # Bug: rev not initialized
    return rev

print("Reversed Key: " + reverse("evenkey"))
