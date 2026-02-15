"""
Problem: Sort Strings by Length

Given a list of strings, sort the list in ascending order based on
the length of each string.

Requirements:
- Sort strings by their length (shorter → longer).
- Preserve the original string values.
- If two strings have the same length, their relative order may remain
  unchanged (stable sort preferred but not required).
- Implement two approaches:
    1. Using built-in sorted() with key=len
    2. Manual sorting using comparison (e.g., bubble/selection style)

Example:
Input:
["aditya", "kanishk", "games", "fly", "play"]

Output:
["fly", "play", "games", "aditya", "kanishk"]

Explanation:
- "fly" → length 3
- "play" → length 4
- "games" → length 5
- "aditya" → length 6
- "kanishk" → length 7

Approach 1:
Use sorted(list, key=len) to sort based on string length.

Approach 2:
Compare lengths manually and swap elements when needed.
"""

s=["aditya", "kanishk", "games", "fly", "play"]

s = sorted(s, key=len)
print(s)

for i in range(len(s)):
    for j in range(i+1, len(s)):
        if len(s[i])>len(s[j]):
            s[i], s[j] = s[j], s[i]

print(s)

