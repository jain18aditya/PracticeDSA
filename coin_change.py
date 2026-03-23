"""
LeetCode 322 - Coin Change

Problem:

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.

If that amount of money cannot be made up by any combination of the coins,
return -1.

---

Input:
- coins: List[int]
- amount: int

---

Output:
- int (minimum number of coins)
- Return -1 if not possible

---

Example 1:

Input:
coins = [1,2,5]
amount = 11

Output:
3

Explanation:
11 = 5 + 5 + 1 → 3 coins

---

Example 2:

Input:
coins = [2]
amount = 3

Output:
-1

Explanation:
Cannot make 3 using coin 2

---

Example 3:

Input:
coins = [1]
amount = 0

Output:
0

---

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

---

Key Idea:

This is a Dynamic Programming problem.

Define:
dp[i] = minimum coins needed to make amount i

Transition:
dp[i] = min(dp[i], dp[i - coin] + 1)

Initialize:
- dp[0] = 0
- dp[i] = infinity for all other i

---

Goal:
Find minimum number of coins to make the target amount.
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                diff = i - coin
                if diff >= 0:
                    dp[i] = min(dp[i], dp[diff]+1)

        if dp[amount] < float("inf"):
            return dp[amount]
        else:
            return -1

coins = [1,2,5]
amount = 11

solution = Solution()
answer = solution.coinChange(coins, amount)
print(answer)