
def two_sum(num, target):
    low = 0
    high = len(num)-1
    num.sort()
    while low < high:
        result = num[low] + num[high]
        if result == target:
            return num[low], num[high]
        if result<target:
            low+=1
        else:
            high-=1
    return False

arr = [1,2,3,4,5,6,8,7]
print(two_sum(arr, 15))

