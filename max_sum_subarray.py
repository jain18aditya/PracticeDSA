"""
Problem: Maximum Sum Subarray

Given an integer array (which may contain positive, negative, or zero values),
find the contiguous subarray with the maximum possible sum.

Return:
1. The maximum sum
2. The starting index of the subarray
3. The ending index of the subarray

Notes:
- The array can contain all negative numbers.
- In that case, the maximum sum is the largest (least negative) element.
- The subarray must be contiguous.

Example 1:
Input:  [-2, -3, 4, -1, -2, 1, 5, -3]
Output:
Max Sum = 7
Start Index = 2
End Index = 6
Subarray = [4, -1, -2, 1, 5]

Example 2:
Input:  [-5, -2, -8]
Output:
Max Sum = -2
Start Index = 1
End Index = 1
Subarray = [-2]

Approach:
Use Kadane’s Algorithm to efficiently compute the maximum sum subarray
in O(n) time and O(1) space.
"""


def max_subarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    start = end = s = 0

    for i, num in enumerate(arr):
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

        if current_sum < 0:
            current_sum = 0
            s = i + 1

    return max_sum, start, end

def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

# Example
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
arr1 = [-5, -2, -8]
max_sum, start, end = max_subarray(arr)
print("Max Sum:", max_sum)
print("Start index:", start)
print("End index:", end)

max_sum, start, end = max_subarray(arr1)
print("Max Sum:", max_sum)
print("Start index:", start)
print("End index:", end)

print(maxSubArray(arr))
