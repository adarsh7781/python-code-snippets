"""
Robust Anagram Checker

An anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Checks whether two strings are anagrams:
- Ignores case
- Ignores spaces and non-alphanumeric characters

Examples:
"listen" & "silent" → Anagram
"Debit Card" & "Bad Credit" → Anagram
"""

import re

def normalize(text):
    # Remove non-alphanumeric characters and convert to lowercase
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()


def are_anagrams(str1, str2):
    str1 = normalize(str1)
    str2 = normalize(str2)

    # If lengths differ, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    freq = {}

    # Count characters in first string
    for char in str1:
        freq[char] = freq.get(char, 0) + 1

    # Decrease count using second string
    for char in str2:
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1

    return True


def main():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    if are_anagrams(s1, s2):
        print("Strings are Anagrams")
    else:
        print("Strings are NOT Anagrams")


if __name__ == "__main__":
    main()
