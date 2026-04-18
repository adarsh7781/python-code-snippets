"""
List Processing: Filtering and Transformation

This program:
- Filters even numbers from a list
- Squares them
- Returns the processed result

Demonstrates control flow with real data manipulation.
"""

def process_numbers(numbers):
    processed = []

    for num in numbers:
        if num % 2 == 0:          # Filter condition
            processed.append(num ** 2)  # Transformation

    return processed


def main():
    try:
        user_input = input("Enter numbers separated by space: ")
        numbers = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    result = process_numbers(numbers)

    print("\nProcessed Output:")
    print(result)


if __name__ == "__main__":
    main()
