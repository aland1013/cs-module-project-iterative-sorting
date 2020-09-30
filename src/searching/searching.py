def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i 

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        else:
            if target < arr[middle]:
                end = middle - 1
            else:
                start = middle + 1

    return -1  # not found
