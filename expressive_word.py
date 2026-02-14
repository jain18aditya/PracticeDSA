"""
Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.



Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3


Constraints:

1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase letters.
"""

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

def is_stretchy(s, w):
    i = j = 0

    while i < len(s) and j < len(w):

        # Characters must match
        if s[i] != w[j]:
            return False

        # Start positions
        i_start = i
        j_start = j

        # Count group in s
        while i < len(s) and s[i] == s[i_start]:
            i += 1

        # Count group in w
        while j < len(w) and w[j] == w[j_start]:
            j += 1

        s_count = i - i_start
        w_count = j - j_start

        # Rule 1: if s group < 3 → must match exactly
        if s_count < 3 and s_count != w_count:
            return False

        # Rule 2: if s group >= 3 → w cannot exceed s
        if s_count >= 3 and w_count > s_count:
            return False

    # Both must finish together
    return i == len(s) and j == len(w)

def count_stretchy(s, words):
    count = 0
    for w in words:
        if is_stretchy(s, w):
            count += 1
    return count


s = "heeellooo"
words = ["hello", "hi", "helo"]

print(count_stretchy(s, words))


print(find_stretchy())