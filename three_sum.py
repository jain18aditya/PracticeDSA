
def three_sum(nums, target):
    nums.sort()
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        while left < right:
            total_sum = nums[i] + nums[left] + nums[right]
            if total_sum == target:
                return nums[i], nums[left], nums[right]
            if total_sum < target:
                left += 1
            if total_sum > target:
                right -= 1
    return -1

nums = [1, 4, 45, 6, 10, 8]
print(three_sum(nums, 6))