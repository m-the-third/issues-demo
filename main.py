import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number>")
        sys.exit(1)

    try:
        number = float(sys.argv[1])
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid number")
        sys.exit(1)

    print(f"{number} squared is {number ** 2}")


if __name__ == "__main__":
    main()
