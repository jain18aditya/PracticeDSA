"""
Problem: Merge Sorted Arrays (In-place)

You are given two sorted integer arrays, nums1 and nums2, and two integers
m and n representing the number of valid elements in nums1 and nums2 respectively.

- nums1 has a size of m + n, where the last n elements are empty (0) and
  should be filled by merging elements from nums2.
- Merge nums2 into nums1 so that nums1 becomes one sorted array.
- The merge must be done in-place without using extra space.

Example:
Input:
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3

Output:
[1, 2, 2, 3, 5, 6]

Approach:
Use three pointers starting from the end:
- i → last valid element in nums1 (m-1)
- j → last element in nums2 (n-1)
- k → last index of nums1 (m+n-1)

Compare nums1[i] and nums2[j] and place the larger element at nums1[k].
Move pointers accordingly until all elements of nums2 are merged.
"""

def merge(nums1, m, nums2, n):

    i = m - 1          # last valid element in nums1
    j = n - 1          # last element in nums2
    k = m + n - 1      # last position in nums1

    while i >= 0 and j >= 0:

        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    # remaining nums2 elements
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))
