from collections import deque

def max_sliding_window(nums, k):
    result = []
    for i in range(len(nums)-k+1):
        result.append(max(nums[i:i+k]))
    return result

def max_deque(nums, k):
    result = []
    queue = deque()
    i=0
    for i in range(k):
        queue.append(nums[i])
    i+=1
    while i<len(nums):
        result.append(max(queue))
        queue.popleft()
        queue.append(nums[i])
        i+=1
    result.append(max(queue))
    return result

nums = [1,3,-1,-3,5,3,6,7]
print(max_sliding_window(nums, 4))
print(max_deque(nums, 4))