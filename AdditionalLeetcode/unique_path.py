"""
LeetCode 62 – Unique Paths (Problem Statement)

A robot is located at the top-left corner of an m x n grid.

The robot can only move:

Down, or

Right

The robot is trying to reach the bottom-right corner of the grid.

Task

Return the total number of unique paths the robot can take to reach the bottom-right corner.

Example 1
Input: m = 3, n = 7
Output: 28
Example 2
Input: m = 3, n = 2
Output: 3
Explanation:
Right → Down → Down
Down → Down → Right
Down → Right → Down
Constraints

1 <= m, n <= 100
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[]
        for _ in range(m):
            dp.append([0]*n)
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

solution = Solution()
print(solution.uniquePaths(3, 3))
print(solution.uniquePaths(3, 7))
print(solution.uniquePaths(3, 2))
