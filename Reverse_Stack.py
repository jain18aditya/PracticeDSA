
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
