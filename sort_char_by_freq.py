"""
Sort Characters by Frequency

Given a string, sort the characters in decreasing order based on their frequency
of occurrence. Characters with higher frequency should appear first.

Requirements:
- Count frequency of each character.
- Construct a new string where characters appear repeated by their frequency.
- Sort by frequency in descending order.

Example:
Input:  "tree"
Output: "eetr" or "eert"

Explanation:
- 'e' appears twice → highest frequency
- 't' and 'r' appear once
- Result string groups characters by frequency.
"""

from collections import Counter

def sort_char_by_frequency(s):
    arr = Counter(s)
    sorted_freq = sorted(arr.keys(), key=lambda x: arr[x], reverse=True)
    print(sorted_freq)
    sorted_freq = "".join([ch*arr[ch] for ch in sorted_freq])
    return sorted_freq

print(sort_char_by_frequency("tree"))

