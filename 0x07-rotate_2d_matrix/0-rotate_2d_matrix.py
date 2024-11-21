#!/usr/bin/python3
"""Matrix Rotate Module"""


def rotate_2d_matrix(matrix):
    """
    A function to rotate a 2D matrix by 90 degree in place

    :param matrix: the 2D matrix to be rotated
    """
    for i, row in enumerate([[matrix[i][j]
                              for i in range(len(matrix) - 1, -1, -1)]
                            for j in range(len(matrix))]):
        matrix[i] = row
