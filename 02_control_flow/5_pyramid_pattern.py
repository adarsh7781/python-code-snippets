"""
Simple Pyramid Pattern Printer

Prints a centered pyramid pattern using '*' characters.

Example (n = 5):

    *
   ***
  *****
 *******
*********

Demonstrates nested loops and control flow logic.
"""

def print_pyramid(n):
    for i in range(1, n + 1):
        # Print spaces
        for j in range(n - i):
            print(" ", end="")

        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")

        print()  # Move to next line


def main():
    try:
        n = int(input("Enter number of rows: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print_pyramid(n)


if __name__ == "__main__":
    main()
