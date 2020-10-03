def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] is target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if arr[middle] == target:
            return middle
        if arr[middle] > target:
            right = middle - 1
        if arr[middle] < target:
            left = middle + 1

    return -1  # not found
