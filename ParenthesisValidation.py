"""
Problem: Valid Parentheses

Given a string consisting of only bracket characters:
'(', ')', '{', '}', '[', ']', '<', '>'

Determine whether the input string is valid.

A string is considered valid if:
1. Every opening bracket has a corresponding closing bracket of the same type.
2. Brackets are closed in the correct order (LIFO — Last In, First Out).
3. No closing bracket appears without a matching opening bracket.

Return:
- True if the parentheses string is valid
- False otherwise

Examples:
Input:  "[()]"
Output: True

Input:  "(()]"
Output: False

Approach:
Use a stack:
- Push opening brackets onto the stack.
- When a closing bracket
"""

def validate_parentheses(par):
    par_dict = {"}":"{", ")":"(", "]":"[", ">":"<"}
    stack = []
    for ch in par:
        if ch in par_dict.values():
            stack.append(ch)
        if ch in par_dict.keys():
            if stack[-1] != par_dict[ch]:
                return False
            stack.pop()
    return True

print(validate_parentheses('(()]'))
print(validate_parentheses('[()]'))