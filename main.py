import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Raise a number to a power (default: 2)")
    parser.add_argument("number", type=float, help="The number to raise")
    parser.add_argument("--power", type=float, default=2.0, help="The power to raise the number to (default: 2)")

    args = parser.parse_args()

    result = args.number ** args.power
    print(f"{args.number} raised to the power of {args.power} is {result}")


if __name__ == "__main__":
    main()
