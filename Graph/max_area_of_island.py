"""
LeetCode 695 - Max Area of Island

Problem:

You are given an m x n binary grid where:
- 1 represents land
- 0 represents water

An island is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are surrounded by water.

Return the maximum area of an island in the grid.
If there is no island, return 0.

Input:
- grid: List[List[int]]
  where:
    1 = land
    0 = water

Output:
- Return an integer representing the maximum area of any island

Example 1:

Input:
[
  [0,0,1,0,0,0,1,1],
  [0,1,1,0,1,0,1,1],
  [0,0,0,0,1,0,0,0],
  [1,1,0,1,1,1,0,0],
  [1,1,0,0,0,0,0,0]
]

Output:
5

Explanation:
The largest island has area = 6 (6 connected 1s)

Example 2:

Input:
[
  [0,0,0,0],
  [0,0,0,0]
]

Output:
0

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1

Key Idea:
- Use DFS or BFS to explore each island
- Count the size (area) of each island
- Track the maximum area

Goal:
Find the largest connected group of 1s in the grid.
"""
from typing import List

class Solution:
    def maxArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
            else:
                return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area


grid = [
    [0,0,1,0,0,0,1,1],
    [0,1,1,0,1,0,1,1],
    [0,0,0,0,1,0,0,0],
    [1,1,0,1,1,1,0,0],
    [1,1,0,0,0,0,0,0]
]
print(Solution().maxArea(grid))