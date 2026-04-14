"""
Number Classifier

This program classifies a number based on multiple conditions:
- Positive / Negative / Zero
- Even / Odd
- Divisible by 3 and 5
"""

def classify_number(num):
    result = {}

    # Positive / Negative / Zero
    if num > 0:
        result["sign"] = "Positive"
    elif num < 0:
        result["sign"] = "Negative"
    else:
        result["sign"] = "Zero"

    # Even / Odd
    if num % 2 == 0:
        result["parity"] = "Even"
    else:
        result["parity"] = "Odd"

    # Divisibility check
    if num % 3 == 0 and num % 5 == 0:
        result["divisibility"] = "Divisible by both 3 and 5"
    elif num % 3 == 0:
        result["divisibility"] = "Divisible by 3"
    elif num % 5 == 0:
        result["divisibility"] = "Divisible by 5"
    else:
        result["divisibility"] = "Not divisible by 3 or 5"

    return result


# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    classification = classify_number(number)

    print("\n--- Classification Result ---")
    for key, value in classification.items():
        print(f"{key.capitalize()}: {value}")
