"""
LeetCode 210 - Course Schedule II

Problem:

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that
you must take course b first if you want to take course a.

Return the ordering of courses you should take to finish all courses.

If there are multiple valid answers, return any of them.
If it is impossible to finish all courses (due to a cycle), return an empty list.

---

Input:
- numCourses: int
- prerequisites: List[List[int]]

Each pair [a, b] means:
b → a (edge from b to a)

---

Output:
- Return a list of course order (topological order)
- Return [] if no valid ordering exists

---

Example 1:

Input:
numCourses = 2
prerequisites = [[1,0]]

Output:
[0,1]

Explanation:
Take course 0 first, then course 1.

---

Example 2:

Input:
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

Output:
[0,1,2,3]   (or [0,2,1,3])

Explanation:
- Take 0 first
- Then 1 and 2
- Then 3

---

Example 3:

Input:
numCourses = 1
prerequisites = []

Output:
[0]

---

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2

---

Key Idea:
- This is a Topological Sorting problem on a directed graph
- If a valid ordering exists → return topological order
- If cycle exists → return []

Approaches:
1. BFS (Kahn’s Algorithm using indegree)
2. DFS (with cycle detection and postorder)

---

Goal:
Return a valid order of courses or detect if it’s impossible.
"""
from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        order = []
        for a, b in prerequisites:
            g[a].append(b)

        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        def dfs(i):
            if states[i] == visiting:
                return False
            elif states[i] == visited:
                return True

            states[i] = visiting

            for neighbor in g[i]:
                if not(dfs(neighbor)):
                    return False

            states[i] = visited
            order.append(i)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []

        return order

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]    ]
print(Solution().findOrder(numCourses, prerequisites))