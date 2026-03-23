"""
Jump Game II
📄 Problem Statement (copy-friendly)

Given an integer array nums, you are initially positioned at the first index.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Return the minimum number of jumps required to reach the last index.

🔹 Example 1
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: Jump from index 0 → 1, then 1 → last index.
🔹 Example 2
Input: nums = [2,3,0,1,4]
Output: 2
🔹 Constraints
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
"""

class Solution:
    def jump(self, nums):
        l = r = 0
        farthest = 0
        res = 0
        while r < len(nums)-1:
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res


nums = [2,3,1,1,4]
solution = Solution()
print(solution.jump(nums))

nums = [2,3,0,1,4]
print(solution.jump(nums))
