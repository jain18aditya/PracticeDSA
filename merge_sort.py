"""
Problem: Merge Sort

Given an unsorted list of integers, sort the list in ascending order
using the Merge Sort algorithm.

Merge Sort is a Divide and Conquer algorithm that:
1. Divides the array into two halves.
2. Recursively sorts each half.
3. Merges the two sorted halves into a single sorted array.

Requirements:
- Implement merge_sort(arr) to recursively split and sort the array.
- Implement merge(left, right) to merge two sorted arrays.
- The algorithm should return a new sorted array.
- Handle edge cases such as empty list and single-element list.

Example:
Input:  [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]

Approach:
Recursively divide the array until subarrays of size 1 are obtained.
Then merge the subarrays in sorted order using a two-pointer technique.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr = [4, 1, 3, 9, 7]
out = merge_sort(arr)
print(out)