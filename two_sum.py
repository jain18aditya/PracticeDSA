"""
Problem: Two Sum — Find Pair with Given Sum

Given an integer array nums and an integer target, determine whether
there exist two distinct elements in the array whose sum equals
the target value.

Return:
- The pair (a, b) if such two numbers exist
- Otherwise return False

Requirements:
- The pair must use two different indices.
- The array may contain unsorted values.
- The solution should be efficient.

Example:
Input:
nums = [1, 2, 3, 4, 5, 6, 8, 7]
target = 15

Output:
(7, 8)

Explanation:
7 + 8 = 15

Approach:
- Sort the array.
- Use two pointers:
    low → start of array
    high → end of array
- If sum is too small → move low forward.
- If sum is too large → move high backward.
- Continue until pair is found or pointers cross.

Time Complexity: O(n log n) (due to sorting)
Space Complexity: O(1)
"""


def two_sum(num, target):
    low = 0
    high = len(num)-1
    num.sort()
    while low < high:
        result = num[low] + num[high]
        if result == target:
            return num[low], num[high]
        if result<target:
            low+=1
        else:
            high-=1
    return False


def optimized_two_sum_index(nums, target):
    seen = {}
    result = set()
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            result.add((nums[seen[complement]], nums[i]))
        seen[num] = i
    return result

def optimized_two_sum(nums, target):
    seen = []
    result = []
    for num in nums:
        compliment = target - num
        if compliment in seen:
            result.append((compliment, num))
        seen.append(num)
    return result
arr = [1,2,3,4,5,6,8,7]


print(two_sum(arr, 15))
print(optimized_two_sum(arr, 15))
print(optimized_two_sum_index(arr, 15))
