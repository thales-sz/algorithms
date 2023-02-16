def is_palindrome_iterative(word):
    reverse = ""
    for letter in word:
        reverse = letter + reverse

    if reverse == word and word != "":
        return True
    return False
