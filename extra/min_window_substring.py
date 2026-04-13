"""
76. Minimum Window Substring
You are given two strings:
- s → source string
- t → target string

Goal:
Find the smallest substring of s such that it contains all characters of t,
including duplicates (i.e., frequency of characters matters).

Rules:
- Order of characters does NOT matter.
- The substring must contain all characters from t with correct frequency.
- If no such substring exists, return an empty string "".

Example 1:
Input:
s = "ADOBECODEBANC"
t = "ABC"

Output:
"BANC"

Explanation:
"BANC" is the smallest substring that contains A, B, and C.

Example 2:
Input:
s = "AAABBC"
t = "AABC"

Output:
"AABBC"

Explanation:
We need 2 A's, 1 B, and 1 C. "AABBC" is the smallest valid substring.

Constraints:
- 1 <= len(s), len(t) <= 100000
- Strings consist of ASCII characters
- Case-sensitive

Key Points:
- Must match character frequency (not just presence)
- Return minimum length valid substring
- If no valid substring exists → return
"""

from collections import Counter
def min_window_substring(s, t):
    need = Counter(t)
    have, need_count = 0, len(need)

    window = {}

    result = [-1, -1]
    res_len = float("inf")
    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1
        if char in need and window[char] == need[char]:
            have += 1

        while have == need_count:
            if right - left + 1 < res_len:
                res_len = right - left + 1
                result = [left, right]

            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1
    l, r = result
    return s[l:r + 1] if res_len != float("inf") else ""