"""
Optimized Prime Number Checker

This program checks whether a number is prime using an efficient approach:
- Instead of checking all numbers from 2 to n-1
- We only check up to √n (square root of n)

This is an optimized program.
This reduces time complexity significantly.
"""

import math

def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # Check only odd numbers up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def main():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if is_prime(num):
        print(f"{num} is a Prime number")
    else:
        print(f"{num} is NOT a Prime number")


if __name__ == "__main__":
    main()
