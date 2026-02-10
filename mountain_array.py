def valid_mountain_array(arr):
    if len(arr) <= 2 or arr[0] >= arr[1]:
        return False
    up = True

    for i in range(1, len(arr)):
        if up:
            if i == len(arr) - 1:
                return False
            if arr[i] == arr[i + 1]:
                return False
            if arr[i] > arr[i + 1]:
                up = False
        else:
            if arr[i - 1] <= arr[i]:
                return False
    return True

print(valid_mountain_array([6,7,8,6]))

print(valid_mountain_array([3,5,5,3]))
print(valid_mountain_array([2,1]))
print(valid_mountain_array([1,2,1]))