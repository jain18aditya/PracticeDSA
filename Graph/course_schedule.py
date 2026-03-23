"""
LeetCode 207 - Course Schedule

Problem:

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that
you must take course b first if you want to take course a.

Return true if you can finish all courses.
Otherwise, return false.

---

Input:
- numCourses: int
- prerequisites: List[List[int]]

Each pair [a, b] means:
b → a (edge from b to a)

---

Output:
- Return True if it is possible to complete all courses
- Return False if there is a cycle (i.e., impossible to finish)

---

Example 1:

Input:
numCourses = 2
prerequisites = [[1,0]]

Output:
True

Explanation:
Take course 0 first, then course 1.

---

Example 2:

Input:
numCourses = 2
prerequisites = [[1,0],[0,1]]

Output:
False

Explanation:
There is a cycle → impossible to complete courses.

---

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2

---

Key Idea:
- This is a cycle detection problem in a directed graph
- If graph has a cycle → cannot complete all courses
- Use:
  - DFS (cycle detection with visited states)
  OR
  - BFS (Topological Sort using Kahn’s Algorithm)

---

Goal:
Determine if the directed graph formed by prerequisites has a cycle.
"""
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]
            print(states)
            if state == visited: return True
            elif state == visiting: return False

            states[node] = visiting

            for neighbor in g[node]:
                if not dfs(neighbor):
                    return False
            states[node] = visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


numCourses = 2
prerequisites = [[1,0],[0,1]]
print(Solution().canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0]]
print(Solution().canFinish(numCourses, prerequisites))
