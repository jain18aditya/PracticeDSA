"""
Problem: Search in Rotated Sorted Array

You are given a sorted array of distinct integers that has been rotated
at an unknown pivot. Your task is to find the index of a given target value.

If the target exists in the array, return its index. Otherwise, return -1.

The algorithm must run in O(log n) time.

Example:
Input:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

Output:
4

Explanation:
The array was originally sorted, then rotated. Using modified binary search,
we determine which half is sorted and narrow down the search space.

Approach:
Use Binary Search with modification:
- At each step, determine whether the left half or right half is sorted.
- Check if the target lies within the sorted half.
- Narrow the search space accordingly until the target is found or the search ends.
"""

def modified_binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(modified_binary_search(nums, target))