#!/usr/bin/python3
"""
Module for calculating minimum operations to get n H's
"""


def minOperations(n):
    """
    Calculate fewest number of operations needed to result in exactly n H characters
    
    Args:
        n (int): Target number of H characters
        
    Returns:
        int: Minimum number of operations, or 0 if impossible
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    # Find all prime factors and sum them
    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    # If n is still greater than 1, then it's a prime factor
    if n > 1:
        operations += n
    
    return operations
