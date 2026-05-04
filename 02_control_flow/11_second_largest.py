"""
Second Largest Element Finder

Finds the second largest unique number in a list.

Handles:
- Duplicate values
- Edge cases (small lists)

Example:
Input: [10, 20, 4, 45, 99]
Output: 45
"""

def find_second_largest(nums):
    unique_nums = list(set(nums))  # Remove duplicates

    if len(unique_nums) < 2:
        return None

    largest = second = float('-inf')

    for num in unique_nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num

    return second


def main():
    try:
        user_input = input("Enter numbers separated by space: ")
        nums = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    result = find_second_largest(nums)

    if result is None:
        print("No second largest element found.")
    else:
        print(f"Second Largest Element: {result}")


if __name__ == "__main__":
    main()
