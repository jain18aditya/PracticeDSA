"""
📘 LeetCode 1143 — Longest Common Subsequence
🧾 Problem Statement

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

📌 Definition

A common subsequence of two strings is a subsequence that is common to both strings.

🧠 Goal

Find the maximum length of such a common subsequence.

🧪 Examples
Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace"
Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The entire string is the LCS
Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: No common subsequence
⚙️ Constraints
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

solution = Solution()

text1="aa"
text2="aabb"
print(solution.longestCommonSubsequence(text1, text2))

text1="abc"
text2="acbebc"
print(solution.longestCommonSubsequence(text1, text2))
