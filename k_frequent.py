"""
You’re given a list of numbers.
You need to return the k numbers that appear most often.
nums = [1,1,1,2,2,3], k = 2
Output = [1,2]
"""
import heapq
from collections import Counter

def k_frequent(nums, k):
    frequency = Counter(nums)
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    print(frequency)
    return [num[0] for num in frequency[:k]]

def topKFrequent_heap(nums, k):
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)

nums = [1,1,1,2,2,3]
k = 2

print(k_frequent(nums, k))
print(topKFrequent_heap(nums, k))