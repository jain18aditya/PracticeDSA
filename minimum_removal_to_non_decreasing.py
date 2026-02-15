"""
Problem: Minimum Removals to Make Array Non-Decreasing

You are given an integer array consisting only of values {1, 2, 3}.
In one operation, you can remove any element from the array.

Your task is to determine the minimum number of removals required so that
the remaining array becomes non-decreasing (i.e., all 1s come first,
followed by 2s, then 3s).

Return the minimum number of deletions needed.

Example:
Input:  [2, 1, 3, 2, 1]
Output: 2

Explanation:
By removing two elements, the array can be rearranged into a valid
non-decreasing sequence such as [1, 1, 2, 3] or [1, 2, 2, 3].

Approach:
Use dynamic counting:
- c1 → longest valid sequence ending with only 1s
- c2 → longest valid sequence ending with 1s and 2s
- c3 → longest valid sequence ending with 1s, 2s, and 3s

For each element:
- If value == 1 → extend c1
- If value == 2 → extend the best of (c1,
"""

def solution(arr):
    if not arr:
        return 0

    c1 = c2 = c3 = 0

    for x in arr:
        if x == 1:
            c1 += 1
        elif x == 2:
            c2 = max(c1, c2) + 1
        elif x == 3:
            c3 = max(c2, c3) + 1

    return len(arr) - max(c1, c2, c3)


# Robust input parsing
try:
    # line = input().strip()
    line = "[2, 1, 3, 2, 1]"
    line = line.strip()[1:-1]
    if not line:
        print(0)
    else:
        arr = [int(x.strip()) for x in line.split(',') if x.strip()]
        print(arr)
        print(solution(arr))
except Exception:
    print("Exception received")
    print(0)
