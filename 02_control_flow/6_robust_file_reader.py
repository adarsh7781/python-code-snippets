"""
Robust File Reader

This program safely reads a file and handles common errors:
- File not found
- Permission issues
- Unexpected errors

Demonstrates exception handling with control flow.
"""

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)

    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print(f"Unexpected error: {e}")

    else:
        print("\nFile read successfully.")

    finally:
        print("Execution completed.")


def main():
    filename = input("Enter filename to read: ")
    read_file(filename)


if __name__ == "__main__":
    main()
