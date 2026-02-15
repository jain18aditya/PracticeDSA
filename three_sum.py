"""
Problem: Three Sum — Find Triplet with Given Sum

Given an integer array nums and an integer target, determine whether
there exist three distinct elements in the array whose sum equals
the target value.

Return:
- The triplet (a, b, c) if such three numbers exist
- Otherwise return -1

Requirements:
- The triplet must consist of three different indices.
- The array may contain positive, negative, or zero values.
- The solution should be efficient (better than O(n^3)).

Example:
Input:
nums = [1, 4, 45, 6, 10, 8]
target = 6

Output:
(1, 4, 1) → (example depends on array)
Or any valid triplet whose sum = 6
If no such triplet exists → -1

Approach:
- Sort the array.
- Fix one element and use two-pointer technique (left and right)
  to search for remaining two numbers.
- If sum is too small → move left pointer right.
- If sum is too large → move right pointer left.
- Time complexity: O(n^2)
- Space complexity: O(1) (excluding sort).
"""

def three_sum(nums, target):
    nums.sort()
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        while left < right:
            total_sum = nums[i] + nums[left] + nums[right]
            if total_sum == target:
                return nums[i], nums[left], nums[right]
            if total_sum < target:
                left += 1
            if total_sum > target:
                right -= 1
    return -1

nums = [1, 4, 45, 6, 10, 8]
print(three_sum(nums, 6))