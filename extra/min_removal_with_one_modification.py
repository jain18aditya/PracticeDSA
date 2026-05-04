# =========================
# PROBLEM 1
# =========================
# Minimum Removals with One Modification
#
# Given an array of integers arr:
# - You can remove any number of elements
# - You can modify at most one element to any value
#
# The array is valid if:
#     max(arr) <= 2 * min(arr)
#
# Return the minimum number of removals required.
# Input [7, 4, 2, 3, 12, 9]
# Output 2


def min_removals_with_one_edit(arr):
    arr.sort()
    n = len(arr)

    j = 0
    max_keep = 0

    for i in range(n):
        while j < n and arr[j] <= 2 * arr[i]:
            j += 1

        length = j - i

        # case 1: no modification
        max_keep = max(max_keep, length)

        # case 2: allow one modification
        if j < n:
            max_keep = max(max_keep, length + 1)

    return n - max_keep




# =========================
# EXAMPLES
# =========================
if __name__ == "__main__":
    print(min_removals_with_one_edit([7, 4, 2, 3, 12, 9]))  # 2
    print(min_removals_with_one_edit([4, 6, 2, 9, 8, 7, 3]))  # 2
