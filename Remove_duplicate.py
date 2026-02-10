

def remove_duplicates_using_pop(nums):
    i =0
    while i < len(nums)-1:
        if nums[i] == nums[i + 1]:
            nums.pop(i+1)
        else:
            i+=1
    return nums

def remove_duplicates_using_pointer(nums):
    start = 0
    for i in range(len(nums)-1):
        start += 1
        while nums[i] == nums[i+1]:
            nums[i]=nums[i+1]
            i+=1
    return nums[:start+1]


nums = [0,0,0,1,1,2,2,2,3,4]
print(remove_duplicates_using_pop(nums))
print("remove_duplicates_using_pointer")
print(remove_duplicates_using_pointer(nums))
