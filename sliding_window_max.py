"""
Problem: Sliding Window Maximum

Given an integer array nums and an integer k, return a list of the
maximum values for each contiguous subarray (window) of size k.

The window slides from left to right by one position at a time.

Requirements:
- For every window of size k, find the maximum element.
- Return a list of window maximums.
- Handle edge cases such as empty array or k = 1.

Example:
Input:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 4

Output:
[3, 5, 5, 6, 7]

Explanation:
Windows of size 4:
[1, 3, -1, -3] → max = 3
[3, -1, -3, 5] → max = 5
[-1, -3, 5, 3] → max = 5
[-3, 5, 3, 6] → max = 6
[5, 3, 6, 7] → max = 7

Approach 1 (Brute Force):
- For each window, compute max(nums[i:i+k]).
- Time complexity: O(n * k)

Approach 2 (Optimized using Deque):
- Use a deque to store useful elements of the window.
- Maintain elements in decreasing order.
- Remove elements out of window and smaller elements.
- Time complexity: O(n)
"""

from collections import deque

def max_sliding_window(nums, k):
    result = []
    for i in range(len(nums)-k+1):
        result.append(max(nums[i:i+k]))
    return result

def max_deque(nums, k):
    result = []
    queue = deque()
    i=0
    for i in range(k):
        queue.append(nums[i])
    i+=1
    while i<len(nums):
        result.append(max(queue))
        queue.popleft()
        queue.append(nums[i])
        i+=1
    result.append(max(queue))
    return result

nums = [1,3,-1,-3,5,3,6,7]
print(max_sliding_window(nums, 4))
print(max_deque(nums, 4))