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
        # divide list in half
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        else:
            # target is in first half of list
            if target < arr[middle]:
                # cut second half of list
                end = middle - 1
            #target is in second half of list
            else:
                # cut first half of list
                start = middle + 1
        # repeat

    return -1  # not found
