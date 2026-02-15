"""
Question:
Given a string, find the longest substring without repeating characters.
Return the substring itself (not just the length).

Example:
Input:  "adityaditykmaditaypc"
Output: "tykmad"
(Actual result may vary depending on string)

Approach:
Use Sliding Window + HashSet to track characters in current window.
If duplicate found, shrink window from left until duplicate is removed.
"""

def longest_distinct_substring(s):
    seen = set()
    start = 0
    left = 0
    max_len = 0
    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[i])

        if i-left+1 > max_len:
            max_len = i-left+1
            start = left
    return s[start:start+max_len]


print(longest_distinct_substring("adityaditykmaditaypc"))
