"""
LeetCode 200 - Number of Islands

Problem:

Given an m x n 2D grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

Input:
- grid: List[List[str]]
  where '1' represents land and '0' represents water

Output:
- Return the number of islands

Example 1:

Input:
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Output:
1

Example 2:

Input:
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output:
3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'

Key Idea:
- Use DFS or BFS to traverse the grid
- Every time you find an unvisited '1', it represents a new island
- Flood-fill (mark visited) all connected land cells

Goal:
Count how many distinct islands exist in the grid.
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i-1, j)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i, j+1)
            else:
                return

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        return num_islands

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

s = Solution()
num_islands = s.numIslands(grid)
print(num_islands)

