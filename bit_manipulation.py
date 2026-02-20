def subsets(nums):
    """
    Generate all subsets (power set) using bitmask.

    Idea:
    For n elements -> total subsets = 2^n
    Each subset represented by binary mask.

    Example:
    nums = [1,2,3]
    mask 101 -> include index 0 and 2 -> [1,3]
    """
    n = len(nums)
    result = []

    # Loop through all bitmasks from 0 to 2^n - 1
    for mask in range(1 << n):
        subset = []

        for i in range(n):
            # Check if i-th bit is set
            if mask & (1 << i):
                subset.append(nums[i])

        result.append(subset)

    return result


# Example
print("Subsets:", subsets([1, 2, 3]))

def missing_number(nums):
    """
    Given n distinct numbers from range [0..n], exactly one is missing.

    Idea:
    XOR all indices and numbers.
    All matching values cancel -> missing remains.

    Example:
    nums = [3,0,1]
    XOR(0..3) ^ XOR(nums) -> 2
    """
    xor = len(nums)   # start with n

    for i, num in enumerate(nums):
        xor ^= i ^ num   # XOR index and value

    return xor


# Example
print("Missing Number:", missing_number([3, 0, 1]))  # 2

def count_bits(n):
    """
    Count number of set bits (1s) in binary representation.

    Brian Kernighan's Algorithm:
    n & (n - 1) removes the lowest set bit each time.
    So count how many times we can remove a set bit.
    """
    count = 0

    while n:
        n = n & (n - 1)   # remove lowest set bit
        count += 1

    return count


# Example
print("Count Bits (13):", count_bits(13))  # 3 (binary 1101)

def is_power_of_two(n):
    """
    A power of 2 has exactly ONE set bit in binary.
    Example:
        8  -> 1000
        16 -> 10000

    Trick:
    n & (n - 1) removes the lowest set bit.
    For power of 2 -> result becomes 0.
    """
    return n > 0 and (n & (n - 1)) == 0


# Example
print("Power of 2 (8):", is_power_of_two(8))   # True
print("Power of 2 (6):", is_power_of_two(6))   # False

def single_number(nums):
    """
    Given an array where every element appears twice except one,
    find the element that appears only once.

    Idea:
    XOR cancels duplicate numbers: a ^ a = 0
    So XOR of all numbers leaves the unique number.
    """
    result = 0

    for n in nums:
        result ^= n   # XOR each number

    return result


# Example
print("Single Number:", single_number([2, 1, 4, 5, 2, 4, 1]))  # 5
