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