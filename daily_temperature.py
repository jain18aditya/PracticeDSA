"""
LeetCode 739 - Daily Temperatures

Problem:

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that:

answer[i] is the number of days you have to wait after the i-th day to get
a warmer temperature.

If there is no future day for which this is possible, keep answer[i] == 0.

---

Input:
- temperatures: List[int]

---

Output:
- List[int]

---

Example 1:

Input:
temperatures = [73,74,75,71,69,72,76,73]

Output:
[1,1,4,2,1,1,0,0]

Explanation:
- For 73 → next warmer is 74 → 1 day
- For 75 → next warmer is 76 → 4 days
- For 76 → no warmer → 0

---

Example 2:

Input:
temperatures = [30,40,50,60]

Output:
[1,1,1,0]

---

Example 3:

Input:
temperatures = [30,60,90]

Output:
[1,1,0]

---

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

---

Key Idea:

Use a Monotonic Stack (decreasing stack):

- Store indices of temperatures
- When current temperature is higher than stack top:
  → pop and calculate days difference
- Continue until stack is valid again

---

Goal:
For each day, find how many days until a warmer temperature.
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        answer = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                answer[stack_index] = i - stack_index
            stack.append((temp, i))
        return answer

def sol(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    return result


print(f"Output from sol {sol([73,74,75,71,69,76,72,73])}")

temperatures = [73,74,75,71,69,76,72,73]
solution = Solution()
print(f"Output from dailyTemperatures {solution.dailyTemperatures(temperatures)}")

