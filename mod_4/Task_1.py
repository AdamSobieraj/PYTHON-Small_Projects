
def is_palindrome(word):
    """
        Sprawdza, czy przetworzone słowo jest odwróconym wersją samego siebie:
    """
    word = ''.join(e for e in word if e.isalnum()).lower()
    return word == word[::-1]

if __name__ == "__main__":

    print(is_palindrome("kajak"))  # True
    print(is_palindrome("potop"))  # True
    print(is_palindrome("Python"))  # False
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True