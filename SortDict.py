"""
Problem: Sort a Dictionary by Keys

Given a dictionary containing key–value pairs, sort the dictionary
based on its keys in ascending order and return the sorted result
as a list of tuples.

Requirements:
- Sort using the dictionary keys (not values).
- Maintain key–value relationship.
- Use Python's built-in sorting functionality.
- Return the result as a list of (key, value) pairs.

Example:
Input:
{"a": 10, "c": 15, "b": 13}

Output:
[("a", 10), ("b", 13), ("c", 15)]

Approach:
- Use dict.items() to get (key, value) pairs.
- Use sorted() with a lambda function to sort by key (x[0]).
- The result is a sorted list of tuples.
"""

dict={"a":10, "c":15, "b":13}

dict = sorted(dict.items(), key= lambda x: x[1])

print(dict)
