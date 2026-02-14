"""
Problem:
Given two strings a and b, return True if b is an anagram of a, otherwise return False.

Two strings are anagrams if they contain the same characters with the same frequency.

Example:

Input: a = "listen", b = "silent"
Output: True

"""

from collections import Counter

def anagram_sorted(a, b):
    return sorted(a) == sorted(b)

def anagrams_loop(a, b):
    def find_group(s):
        word_count = {}
        for ch in s:
            word_count[ch] = word_count.get(ch, 0) + 1
        return word_count

    a_group = find_group(a)
    b_group = find_group(b)
    return a_group == b_group

def anagram_counter(a, b):
    return Counter(a) == Counter(b)

def anagrams_word_counter(a, b):
    if len(a) != len(b):
        return False
    count = [0]*26
    for ch in a:
        count[ord(ch) - ord('a')] += 1
    for ch in b:
        count[ord(ch) - ord('a')] -= 1

    return all(x==0 for x in count)

a = "abcdefghz"
b = "abdcegfzh"

print(anagrams_word_counter(a, b))
print(anagram_counter(a, b))
print(anagrams_loop(a, b))
print(anagram_sorted(a, b))