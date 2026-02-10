
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

