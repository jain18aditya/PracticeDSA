from itertools import groupby

output = []

def find_group(word):
    groups = []
    for ch, g in groupby(word):
        count = len(list(g))
        groups.append((ch,count))
    # Output: [('h', 1), ('e', 3), ('l', 2), ('o', 3)]
    return groups

def find_stretchy():
    s = "heeellooo"
    words = ["hello", "hi", "helo"]
    s_t = find_group(s)

    for w in words:
        words_t = find_group(w)
        stretchy = True

        if len(s_t) != len(words_t):
            stretchy = False
        else:
            for (s_ch, s_count), (w_ch, w_count) in zip(s_t, words_t):
                if s_ch!=w_ch:
                    stretchy = False
                    break
                if s_count<3 and s_count!=w_count:
                    stretchy = False
                    break
                if s_count>=3 and s_count<w_count:
                    stretchy = False
                    break
        output.append((w, stretchy))
    return output


print(find_stretchy())