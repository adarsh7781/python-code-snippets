"""
Robust Palindrome Checker

Checks whether a given string is a palindrome:
- Ignores case
- Ignores spaces and non-alphanumeric characters

"""

import re

def is_palindrome(text):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()

    # Check palindrome
    return cleaned == cleaned[::-1]


def main():
    text = input("Enter a string: ")

    if is_palindrome(text):
        print("It is a Palindrome")
    else:
        print("It is NOT a Palindrome")


if __name__ == "__main__":
    main()
