#longest increasing subsequence
from typing import List


class Solution:
    def longest_subsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

sol = Solution()
print(sol.longest_subsequence([1,2,3,4,5]))
print(sol.longest_subsequence([1,2,6,4,5]))
print(sol.longest_subsequence([1,2,6,7,5]))
print(sol.longest_subsequence([9,7,5]))
print(sol.longest_subsequence([9]))
print(sol.longest_subsequence([]))
