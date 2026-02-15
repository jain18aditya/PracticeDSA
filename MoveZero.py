"""
283. Move Zeroes
Easy
14.7K
371
Companies
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

0,1,0,3,12

1,0,0,3,12

1,3,0,0,12


1,3,0,0,12

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""

nums = [0,1,0,3,12]

write = 0

for i in nums:
    if i !=0:
        nums[write] = i
        write += 1
for i in range(write, len(nums)):
    nums[i] = 0

print(nums)