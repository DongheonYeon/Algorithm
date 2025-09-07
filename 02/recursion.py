def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]:
            return False
    return True

def is_palindrome_recursive(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True

    return is_palindrome_recursive(string[1:-1])

input = "우영우"
print(is_palindrome_recursive(input))