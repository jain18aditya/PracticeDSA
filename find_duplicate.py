"""
Problem: Find All Duplicates in an Array

You are given an integer array `nums` of size n where
1 ≤ nums[i] ≤ n (numbers are within the array index range).

Some elements appear twice and others appear once.

Write a function to return all elements that appear more than once
(i.e., duplicate numbers).

Example:
Input:  nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Explanation:
- Number 2 appears twice
- Number 3 appears twice

Requirements:
- Return a list of duplicate numbers
- Order does not matter
- Avoid adding the same duplicate multiple times

Constraints:
- 1 ≤ n ≤ 10^5
- 1 ≤ nums[i] ≤ n

Follow-up Questions:

1. Can you solve this using O(n) time?
2. Can you solve this using O(1) extra space (without HashMap)?
3. What happens if numbers can appear more than twice?
4. How would you count frequency of each number?
5. How would you return duplicates sorted?
6. How would you handle very large input efficiently?

Goal:
Practice hash map counting, frequency detection, and optimized array techniques.
"""

nums = [4,3,2,7,8,2,3,1]

def findDuplicate(nums):
    dict = {}
    output = []
    for i in range(len(nums)):
        dict[nums[i]]= dict.get(nums[i], 0)+1
        if dict[nums[i]]>1:
            output.append(nums[i])

    print(output)
    return output

findDuplicate(nums)


def findDuplicate2(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            result.append(num)
    return result

def findDuplicate3(nums):
    dup_dict = {}
    output = set()
    for num in nums:
        dup_dict[num]= dup_dict.get(num, 0)+1
        if dup_dict[num]>1:
            output.add(num)
    return list(output)

print(findDuplicate2(nums))
print(findDuplicate3(nums))
