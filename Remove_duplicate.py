"""
Problem: Remove Duplicates from Sorted Array

Given a sorted integer array, remove the duplicate elements in-place
so that each unique element appears only once.

Return the array (or portion of the array) containing only unique elements.
Do not use extra space beyond O(1) (in-place modification).

Requirements:
- The input array is sorted in non-decreasing order.
- Modify the array in-place to remove duplicates.
- Preserve the original order of unique elements.
- Return the updated array containing only unique values.

Example:
Input:  [0, 0, 0, 1, 1, 2, 2, 2, 3, 4]
Output: [0, 1, 2, 3, 4]

Approach 1 (Using pop):
- Traverse the array.
- If current and next elements are equal, remove the next element using pop().
- Continue until all duplicates are removed.

Approach 2 (Two-Pointer Technique):
- Use one pointer to track position of unique elements.
- Traverse array and overwrite duplicates.
- Return the array slice containing only unique values.
"""


def remove_duplicates_using_pop(nums):
    i =0
    while i < len(nums)-1:
        if nums[i] == nums[i + 1]:
            nums.pop(i+1)
        else:
            i+=1
    return nums

def remove_duplicates_using_pointer(nums):
    start = 0
    for i in range(len(nums)-1):
        start += 1
        while nums[i] == nums[i+1]:
            nums[i]=nums[i+1]
            i+=1
    return nums[:start+1]


nums = [0,0,0,1,1,2,2,2,3,4]
print(remove_duplicates_using_pop(nums))
print("remove_duplicates_using_pointer")
print(remove_duplicates_using_pointer(nums))
