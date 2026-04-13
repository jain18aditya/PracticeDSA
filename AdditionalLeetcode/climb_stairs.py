"""
LeetCode 70 – Climbing Stairs (Problem Statement)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either:

Climb 1 step, or

Climb 2 steps

Task

Return the number of distinct ways to reach the top.

Example 1
Input: n = 2
Output: 2
Explanation:
1 + 1
2
Example 2
Input: n = 3
Output: 3
Explanation:
1 + 1 + 1
1 + 2
2 + 1
Constraints

1 <= n <= 45
"""

class Solution:
    def climb_stairs(self, n: int) -> int:
        if not n:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 1
        curr = 2
        for i in range(2, n):
            prev, curr = curr, prev + curr
        return curr


solution = Solution()
print(solution.climb_stairs(1))
print(solution.climb_stairs(2))
print(solution.climb_stairs(3))
print(solution.climb_stairs(10))