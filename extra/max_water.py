"""
==>Container With Most Water — Problem Statement

You are given an integer array height of length n.

Each element height[i] represents the height of a vertical line drawn at index i.
The lines are drawn such that:
The x-axis is the base
Each line is vertical (perpendicular to x-axis)
==>Goal

Find two lines such that together with the x-axis, they form a container that holds the maximum amount of water.
"""

def max_area(height):
    n = len(height)
    max_water = 0

    # Try every pair of lines
    for i in range(n):
        for j in range(i + 1, n):
            # Width = distance between lines
            width = j - i

            # Height = min of two lines (water limited by shorter line)
            h = min(height[i], height[j])

            # Area = width * height
            area = width * h

            # Update max
            max_water = max(max_water, area)

    return max_water


def optimized_max_area(height):
    max_area = left = 0
    right = len(height) - 1
    while left < right:
        w = right - left
        h = min(height[left], height[right])
        area = w * h
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))
print(optimized_max_area(height))