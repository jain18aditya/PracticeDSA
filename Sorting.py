from collections import Counter


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [2,5,7,8,5,6,3,8,0,2,5,8,3,2,6,8,8,5,4,6]

print(bubble_sort(arr))
print(selection_sort(arr))
print(insertion_sort(arr))


def sort_char_by_frequency(s):
    arr = Counter(s)
    sorted_freq = sorted(arr.keys(), key=lambda x: arr[x], reverse=True)
    print(sorted_freq)
    sorted_freq = "".join([ch*arr[ch] for ch in sorted_freq])
    return sorted_freq

print(sort_char_by_frequency("tree"))

