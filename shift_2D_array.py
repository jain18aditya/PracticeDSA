"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.



Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:

Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]


0,0 -> 2,2
0,1 -> 0,0
0,2 -> 0,1
1,0 -> 0,2


0,0,2-> 0, 2
0,1,2 ->

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100

Algorithm:
1. If k is greater than size of grid: k = k % size of grid
2. Initialize result with 0
3. Traverse all rows:
    Travers all columns:
        shift current element with index i, j to new row and column
        new row = (i + (j + k)/len(grid[0]) % len(grid)
        new column = (j + k) % len(grid[0])
"""

def shiftGrid(grid, k):
    m, n = len(grid), len(grid[0])
    total = m * n
    k %= total  # avoid extra rotations

    # Step 1: flatten
    flat = []
    for row in grid:
        flat.extend(row)

    # Step 2: rotate right by k
    flat = flat[-k:] + flat[:-k]
    # Step 3: reshape
    result = []
    idx = 0
    for i in range(m):
        result.append(flat[idx:idx+n])
        idx += n

    return result

arr = [[1,2,3],[4,5,6],[7,8,9]]
output = shiftGrid(arr, 3)
print(output)
