"""
Problem: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] represents the price of a stock
on day i. Your goal is to maximize profit by choosing a single day to buy one
stock and choosing a different future day to sell that stock.

Return the maximum profit you can achieve. If no profit is possible, return 0.

Constraints:
- You may complete only ONE transaction (buy once and sell once).
- You must buy before you sell.
- If the stock price only decreases, profit is 0.

Example 1:
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

Example 2:
Input:  prices = [7, 6, 4, 3, 1]
Output: 0
Explanation:
No profitable transaction possible.

Approach:
- Track the minimum price seen so far.
- For each day, calculate potential profit = current_price - min_price.
- Update maximum profit if higher profit is found.
- Time Complexity: O(n)
- Space Complexity: O(1)
"""

def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        # update minimum price seen so far
        min_price = min(min_price, price)

        # calculate profit if sold today
        profit = price - min_price

        # update max profit
        max_profit = max(max_profit, profit)

    return max_profit


# Example
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))   # Output: 5
