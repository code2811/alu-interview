#!/usr/bin/python3
"""Minimum operations module"""


def minOperations(n):
    """Return the minimum number of operations to get n H characters"""
    if n < 2:
        return 0

    ops = 0
    i = 2
    while n > 1:
        while n % i == 0:
            ops += i
            n //= i
        i += 1
    return ops

