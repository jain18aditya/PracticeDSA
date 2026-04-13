"""
Leetcode 139
Problem: Given string s and list wordDict, return True if s can be segmented into space-separated words from the dictionary.
Example: s = "leetcode", wordDict = ["leet","code"] → True

"""
from typing import List

def word_break(s: str, words: List[str]):
    word_set = set(words)
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True

    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]

s = "leetcode"
wordDict = ["leet", "code"]
print(word_break(s, wordDict))