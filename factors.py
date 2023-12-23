#!/usr/bin/python3
import sys

def factorize(number):
    """
    Factorizes a given number

    Parameter:
    - number (int): The number to be facotrized.

    Returns: - tuple: A tuple containing two factors of the input number
    """

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return i, number // i
        return None, None


def main(filename):
    """
    Main function to read file contianing numbers and output
    the factorization

    Parameters:
    - filename (str): The name of the file
    """

    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            p, q = factorize(number)
            print("{}={}*{}".format(number, p, q))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: facotrs <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
