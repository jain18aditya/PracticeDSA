"""
LeetCode 198 – House Robber (Problem Statement)

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.

The only constraint is that adjacent houses cannot be robbed on the same night, because
they have connected security systems and will alert the police if both are broken into.

Task

Given an integer array nums, where nums[i] represents the amount of money in the i-th house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (1) and house 3 (3) → total = 4
Example 2
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (2), house 3 (9), house 5 (1) → total = 12
Constraints

1 <= nums.length <= 100

0 <= nums[i] <= 400
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]


nums = [2,7,9,3,1]
sol = Solution()
print(sol.rob(nums))

nums = [2,7,3,1,4,2,1,8]
print(sol.rob(nums))

