nums = [0,1,0,3,12]

write = 0

for i in nums:
    if i !=0:
        nums[write] = i
        write += 1
for i in range(write, len(nums)):
    nums[i] = 0

print(nums)