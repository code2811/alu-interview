#!/usr/bin/python3
"""
0-rain module
Calculates the total amount of rainwater retained between walls.
"""

def rain(walls):
    """
    Calculates how many square units of water will be retained after it rains.

    Args:
        walls (list): A list of non-negative integers representing wall heights.

    Returns:
        int: Total amount of rainwater retained.
    """
    if not walls or len(walls) < 3:
        return 0

    total_water = 0
    left = 0
    right = len(walls) - 1
    left_max = walls[left]
    right_max = walls[right]

    while left < right:
        if walls[left] < walls[right]:
            left += 1
            left_max = max(left_max, walls[left])
            total_water += max(0, left_max - walls[left])
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            total_water += max(0, right_max - walls[right])

    return total_water

