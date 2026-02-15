"""
Problem: Reverse a String

Given a string, reverse the order of its characters and return the reversed string.

Implement two approaches:

1. Reverse using a Stack (LIFO — Last In, First Out)
2. Reverse using Python slicing

Requirements:
- Return a new reversed string.
- Do not modify the original string.
- Handle empty string and single-character string.
- Maintain character integrity (case-sensitive, no trimming).

Example:
Input:  "aditya"
Output: "aytida"

Approach 1 (Stack):
- Push all characters onto a stack.
- Pop characters one by one and build the reversed string.

Approach 2 (Slicing):
- Use Python slicing syntax [::-1] to reverse the string directly.
"""

def reverse_stack(arr):
    stack = []
    for ch in arr:
        stack.append(ch)

    reversed_ch = stack.pop()
    while stack:
        reversed_ch = reversed_ch + stack.pop()

    return reversed_ch

def reverse_list(arr):
    return arr[::-1]

s = "aditya"
print(reverse_list(s))
print(reverse_stack(s))
