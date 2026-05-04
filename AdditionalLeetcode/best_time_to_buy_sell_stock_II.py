"""
LeetCode 122 — Best Time to Buy and Sell Stock II
🧾 Problem Statement

You are given an integer array prices where prices[i] is the price of a given stock on the i-th day.


On each day, you may decide to:

Buy the stock
Sell the stock
Or do nothing

👉 You can complete as many transactions as you like (buy one and sell one share multiple times).

⚠️ However:

You may not hold more than one stock at a time
You must sell before you buy again
🎯 Goal

Return the maximum profit you can achieve.

🧪 Examples
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation:
Buy on day 2 (price = 1), sell on day 3 (price = 5) → profit = 4
Buy on day 4 (price = 3), sell on day 5 (price = 6) → profit = 3
Total profit = 7
Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation:
Buy on day 1 and sell on day 5 → profit = 4
OR buy/sell multiple times → same total profit
Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation:
No profitable transactions possible
⚙️ Constraints
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
"""

class Solution:
    def maxProfit(self, prices):
        i = 0
        profit = 0

        while i < len(prices)-1:
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1
            low = prices[i]

            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i += 1
            high = prices[i]

            profit += high - low

        return profit

sol = Solution()
prices = [1,2,3,4,5]
print(sol.maxProfit(prices))

prices = [7,6,4,3,1]
print(sol.maxProfit(prices))

prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))