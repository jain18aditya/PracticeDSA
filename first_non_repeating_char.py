"""
Problem: First Non-Repeating Character in a String

Given a string `s`, find and return the first character
that does not repeat anywhere in the string.

If all characters repeat, return None.

Example:
Input:  s = "aabbccddeefg"
Output: "f"

Explanation:
- 'a','b','c','d','e' repeat
- 'f' appears only once → first non-repeating character

Requirements:
- Preserve original character order
- Return first non-repeating character
- If none exists → return None

Constraints:
- 1 ≤ len(s) ≤ 10^5
- String may contain lowercase/uppercase letters, digits, symbols

Follow-up Questions:

1. Can you solve this in O(n) time?
2. Why use OrderedDict instead of normal dict?
3. How would you return index instead of character?
4. How would you find all non-repeating characters?
5. How to make it case-insensitive?
6. How to handle streaming input (very large string)?

Goal:
Practice hash map counting, order preservation, and efficient scanning.
"""

from typing import OrderedDict

def find_non_rep_char(s):
    freq = OrderedDict()
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for c, count in freq.items():
        if count == 1:
            return c
    return None

def find_non_rep_char1(s):
    freq = OrderedDict()
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for c, count in freq.items():
        if count == 1:
            return c
    return None

s= "aabbccddeefg"
print(find_non_rep_char(s))
print(find_non_rep_char1(s))