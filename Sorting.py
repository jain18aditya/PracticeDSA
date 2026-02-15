"""
Implement Basic Sorting Algorithms

Given an unsorted list of integers, implement the following sorting algorithms
to sort the array in ascending order:

1. Bubble Sort
2. Selection Sort
3. Insertion Sort

Requirements:
- Sort the array in-place.
- Do not use built-in sorting functions.
- Preserve correctness for duplicate and zero values.
- Return the sorted array.

Example:
Input:  [2, 5, 7, 8, 5, 6, 3, 8, 0]
Output: [0, 2, 3, 5, 5, 6, 7, 8, 8]
"""

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
