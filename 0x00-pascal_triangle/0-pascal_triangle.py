#!/usr/bin/python3
"""Pascal's Triangulation."""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers representing
    the Pascal’s triangle of n

    Arguments:
        n (int) -- the nth pascal triangle.

    Return:
        result (list) -- a list of lists of integers representing.
    """
    if not isinstance(n, (int, float)):
        raise TypeError('n must be an integer.')
    n = int(n)
    result = []
    if n <= 0:
        return result
    for i in range(1, n+1):
        if i == 1:
            result.append([1])
        elif i == 2:
            result.append([1, 1])
        else:
            a = []
            for j in range(1, i + 1):
                if j == 1:
                    a.append(1)
                elif j == i:
                    a.append(1)
                else:
                    a.append(result[i - 2][j - 2] + result[i - 2][j - 1])
            result.append(a)
    return result
