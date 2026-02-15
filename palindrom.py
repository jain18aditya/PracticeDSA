"""
Problem: Check if a String is a Palindrome

Given a string, determine whether it is a palindrome.

A palindrome is a string that reads the same forward and backward.

Return:
- True if the string is a palindrome
- False otherwise

Requirements:
- Implement a function using the two-pointer technique.
- Implement another function using Python slicing.
- The comparison should be character by character.
- Assume case-sensitive comparison unless specified otherwise.

Example:
Input:  "adida"
Output: True

Input:  "aditya"
Output: False

Approach 1 (Two-Pointer):
- Start one pointer at the beginning and one at the end.
- Compare characters while moving inward.
- If any mismatch occurs → not a palindrome.

Approach 2 (Slicing):
- Reverse the string using slicing.
- Compare original string with reversed string.
"""

s="aditya"

def palindrom(s):
    start = 0
    end = len(s)-1

    while start < end:
        if (s[start] != s[end]):
            return False
        start += 1
        end -= 1
    return True

print(palindrom(s))
print(palindrom("adida"))
print(palindrom("adittida"))

def palindrom_list(s):
    return s[0:] == s[::-1]

print(palindrom_list("aditya"))
print(palindrom_list("adida"))

