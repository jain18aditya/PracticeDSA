"""
Problem:
Given an array of strings words, group all anagrams together. You may return the answer in any order.

Two strings are anagrams if they contain the same characters with the same frequency.

Example:

Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
q

Constraints:

1 ≤ words.length ≤ 10^4

0 ≤ words[i].length ≤ 100

words[i] consists of lowercase English letters
"""

from collections import defaultdict

def group_anagrams(words):
    anagrams_dict = {}
    for word in words:
        key = "".join(sorted(word))
        if key in anagrams_dict:
            anagrams_dict[key].append(word)
        else:
            anagrams_dict[key] = [word]
    return list(anagrams_dict.values())

def group_anagram_defaultdict(words):
    groups = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagram_defaultdict(arr))
print(group_anagrams(arr))