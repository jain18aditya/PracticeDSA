"""
Problem: Binary Search Implementation

Given an unsorted list of integers `arr` and an integer `target`,
write a function to find the index of the target element using
Binary Search.

Since Binary Search requires a sorted array, first sort the array,
then perform the search.

Return:
- The index of the target if found
- -1 if the target does not exist in the array

Example:
Input:
    arr = [2,5,7,8,5,6,3,8,0,2,5,8,3,2,6,8,8,5,4,6]
    target = 8

Output:
    (index of any occurrence of 8 in sorted array)

Constraints:
- 1 <= len(arr) <= 10^5
- Elements may contain duplicates
- If duplicates exist, return index of any valid occurrence

Follow-up Questions:
1. How would you modify the code to return the FIRST occurrence?
2. How would you return the LAST occurrence?
3. What is the time complexity?
4. Can you implement Binary Search recursively?
5. How would you handle a very large dataset?
"""

def binary_search(arr, target):
    arr = sorted(arr)
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

arr = [2,5,7,8,5,6,3,8,0,2,5,8,3,2,6,8,8,5,4,6]
target = 8

output = binary_search(arr, target)

print(output)
