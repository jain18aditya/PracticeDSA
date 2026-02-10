

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