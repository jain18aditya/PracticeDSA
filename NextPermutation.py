#nums = [1, 2, 4, 6, 5, 3]

def next_permutation(nums):
    n=len(nums)
    i=n-1
    #Find the first decreasing element from the end
    while i>0 and nums[i]<nums[i-1]:
        i=i-1

    if i==0:
        nums.reverse()
        return nums

    #Find the smallest number greater than nums[i-1] to the right
    j=n-1
    while nums[j]<=nums[i-1]:
        j=j-1

    #swap i-1 and j
    nums[i-1],nums[j] = nums[j],nums[i-1]

    #reverse from i
    nums[i:] = reversed(nums[i:])

    return nums

nums = [1, 2, 4, 6, 5, 3]
print(next_permutation(nums))