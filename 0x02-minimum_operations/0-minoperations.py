#!/usr/bin/python3
"""
Function to calculate the minimum number of operations
needed to obtain exactly n 'H' characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed
    to result in n 'H' characters.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
