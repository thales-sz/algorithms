def is_palindrome_iterative(word):
    if not word:
        return False

    reverse = ""
    for letter in word:
        reverse = letter + reverse

    if reverse == word:
        return True
    return False
