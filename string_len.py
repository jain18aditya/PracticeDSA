"""
Problem: Sort Strings by Length

Given a list of strings, sort them in ascending order by their length.
You need to implement multiple sorting approaches.

Implement TWO approaches:

1. Using sorted() with key parameter
   - Python's built-in sorted function
   - Clean and Pythonic
   - Time: O(n log n)

2. Using nested loops (Bubble Sort)
   - Manual comparison and swapping
   - Educational approach
   - Time: O(n²)

Return:
    List of strings sorted by length in ascending order

Example:

Input:
    strings = ["aditya", "kanishk", "games", "fly", "play"]

Output:
    ['fly', 'play', 'games', 'aditya', 'kanishk']

Constraints:
- Handle empty lists
- Handle strings of same length
- Case sensitivity doesn't matter
- All inputs are non-empty strings

Follow-up Questions:

1. What is the time complexity of each approach?
2. What is the space complexity?
3. How would you sort in descending order?
4. How would you sort by length then alphabetically?
5. Can you optimize bubble sort?
6. What if you need stable sort?
7. How would you handle unicode strings?

Goal:
Practice sorting algorithms, Python built-ins, and different implementation approaches.
"""

s=["aditya", "kanishk", "games", "fly", "play"]

# Approach 1: Using sorted() with key
s_sorted1 = sorted(s, key=len)
print("Using sorted():", s_sorted1)

# Approach 2: Using bubble sort (nested loops)
s_sorted2 = s.copy()
for i in range(len(s_sorted2)):
    for j in range(i+1, len(s_sorted2)):
        if len(s_sorted2[i]) > len(s_sorted2[j]):
            s_sorted2[i], s_sorted2[j] = s_sorted2[j], s_sorted2[i]

print("Using bubble sort:", s_sorted2)