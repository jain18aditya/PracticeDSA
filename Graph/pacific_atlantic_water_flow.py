"""
LeetCode 417 - Pacific Atlantic Water Flow

Problem:

You are given an m x n matrix heights representing the height of each cell.

There are two oceans:
- Pacific Ocean touches the left and top edges
- Atlantic Ocean touches the right and bottom edges

Water can flow from a cell to another cell if the next cell has height
less than or equal to the current cell (downhill or same level).

Return a list of grid coordinates where water can flow to BOTH the Pacific
and Atlantic oceans.

---

Input:
- heights: List[List[int]]

---

Output:
- List[List[int]] where each element is [row, col]

---

Example:

Input:
heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]

Output:
[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

---

Constraints:
- m == heights.length
- n == heights[i].length
- 1 <= m, n <= 200
- 0 <= heights[i][j] <= 10^5

---

Key Idea:

Instead of flowing from each cell to oceans (expensive),
reverse the thinking:

- Start from Pacific borders → DFS/BFS inward (only go to higher/equal height)
- Start from Atlantic borders → DFS/BFS inward

Find cells reachable from BOTH traversals.

---

Goal:
Return all cells that can reach both oceans.
"""
