"""
Frequency Counter

This program counts the frequency of elements in a list.

Demonstrates:
- Dictionary usage
- Control flow
- Real-world data processing logic
"""

def count_frequency(items):
    freq = {}

    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return freq


def main():
    user_input = input("Enter elements separated by space: ")
    items = user_input.split()

    frequency = count_frequency(items)

    print("\nElement Frequencies:")
    for key, value in frequency.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
