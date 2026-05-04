"""
Two Sum Problem

Find indices of two numbers such that they add up to a target.

"""

def two_sum(nums, target):
    lookup = {}  # value → index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i

    return None


def main():
    try:
        nums = list(map(int, input("Enter numbers: ").split()))
        target = int(input("Enter target: "))
    except ValueError:
        print("Invalid input.")
        return

    result = two_sum(nums, target)

    if result:
        print(f"Indices: {result}")
    else:
        print("No valid pair found.")


if __name__ == "__main__":
    main()
