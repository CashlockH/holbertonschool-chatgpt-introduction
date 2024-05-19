#!/usr/bin/python3
import sys

# Function Description:
# Calculates the factorial of a given integer using recursion.

def factorial(n):
    # Parameters:
    # n (int): The integer whose factorial is to be calculated.

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))

# Returns:
# int: The factorial of the input integer.
print(f)
