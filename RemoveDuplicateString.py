"""
Problem: Remove Duplicates from a List While Preserving Order

You are given a list of strings that may contain duplicate values.
Your task is to remove duplicate elements so that each string appears
only once, while keeping the original order of first occurrence.

Return a list containing only the unique elements.

Requirements:
- Do NOT change the order of elements.
- Do NOT sort the list.
- The first occurrence of each element should be kept.
- Subsequent duplicates should be removed.
- The solution should be efficient (avoid unnecessary nested loops).

Example:
Input:
["aditya", "aditya", "test", "best", "fly", "best", "fly"]

Output:
["aditya", "test", "best", "fly"]

Approach 1:
Use dict.fromkeys() — Python dictionaries preserve insertion order,
so converting the list to a dictionary and back removes duplicates
while keeping the original order.

Approach 2:
Use a set to track seen elements and build a new list containing
only elements that appear for the first time.
"""

s=["aditya", "aditya", "test", "best", "fly", "best", "fly"]


output = list(dict.fromkeys(s))
print(output)

unique = []
seen = set()

for word in s:
    if word not in seen:
        seen.add(word)
        unique.append(word)

print(unique)
