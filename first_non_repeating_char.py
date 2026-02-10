from typing import OrderedDict

def find_non_rep_char(s):
    freq = OrderedDict()
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for c, count in freq.items():
        if count == 1:
            return c
    return None


s= "aabbccddeefg"
print(find_non_rep_char(s))