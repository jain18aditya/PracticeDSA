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