#!/usr/bin/python3
"""
0-pascal_triangle
Generates Pascal's triangle up to n rows.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.

    Args:
        n (int): Number of rows of the triangle.

    Returns:
        list: A list of lists of integers representing Pascal’s triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle

