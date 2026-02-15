"""
Problem: Remove Character from a String

Given a string and a character, remove occurrences of the character
from the string.

Implement the following variations:

1. Remove ALL occurrences of the character from the string.
2. Remove ONLY the FIRST occurrence of the character using built-in methods.
3. Remove ONLY the FIRST occurrence without using replace() (manual approach).

Requirements:
- Return a new string (strings are immutable).
- If the character does not exist, return the original string unchanged.
- Maintain the order of remaining characters.

Examples:
Input:  s = "aditya", ch = "a"
Output (remove all):   "dity"
Output (remove first): "ditya"

Approach 1:
- Use list comprehension / generator to filter out all occurrences.

Approach 2:
- Use string replace() with count = 1 to remove first occurrence.

Approach 3:
- Find index of first occurrence and rebuild string using slicing.
"""

def remove_character(s, ch):
    return "".join(c for c in s if c!=ch)

print(remove_character("aditya", "a"))

def remove_first_character(s, ch):
    return s.replace(ch, "", 1)

print(remove_first_character("aditya", "a"))

def remove_first_character(s, ch):
    idx = s.find(ch)
    if idx == -1:
        return s
    return s[:idx] + s[idx+1:]

print(remove_first_character("aditya", "a"))

