"""
FizzBuzz (Optimized & Reusable Version)

Print numbers from 1 to n with the following rules:
- Multiple of 3 → "Fizz"
- Multiple of 5 → "Buzz"
- Multiple of both → "FizzBuzz"

This version is modular and easy to extend.
"""

def fizzbuzz(n):
    for i in range(1, n + 1):
        result = ""

        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"

        print(result if result else i)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    fizzbuzz(n)
