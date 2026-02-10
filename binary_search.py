

def binary_search(arr, target):
    arr = sorted(arr)
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[low] < target:
            low = mid+1
        elif arr[high] > target:
            high = mid-1
    return -1

arr = [2,5,7,8,5,6,3,8,0,2,5,8,3,2,6,8,8,5,4,6]
target = 8

output = binary_search(arr, target)

print(output)
