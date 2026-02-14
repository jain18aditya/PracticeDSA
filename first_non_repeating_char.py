"""
Problem: Find First Non-Repeating Character in a String

Given a string, find and return the first character that appears exactly once.
If no such character exists, return None.

Implement the solution using:
    - OrderedDict to maintain insertion order
    - Frequency counting
    - Single pass lookup

Return:
    First non-repeating character or None if none exists

Example:

Input:
    s = "aabbccddeefg"

Output:
    'f'

Explanation:
    Character frequencies:
    - 'a': 2 times
    - 'b': 2 times
    - 'c': 2 times
    - 'd': 2 times
    - 'e': 2 times
    - 'f': 1 time (FIRST NON-REPEATING)
    - 'g': 1 time

Constraints:
- String may be empty
- String may contain only repeating characters
- Case sensitive (treat 'A' and 'a' differently)
- Handle unicode characters

Follow-up Questions:

1. What is the time complexity and space complexity?
2. Why use OrderedDict instead of regular dict?
3. In Python 3.7+, regular dict maintains insertion order - which is better?
4. How would you find ALL non-repeating characters?
5. How would you optimize for very long strings?
6. How to make it case-insensitive?
7. What if you want the most frequently repeating character instead?

Goal:
Practice hash maps, frequency counting, and string manipulation.
"""