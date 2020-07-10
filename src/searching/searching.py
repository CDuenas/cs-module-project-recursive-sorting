# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # base case
    if start > end:
        return -1

    midpoint = (start + end) // 2

    # If target is the middle
    if arr[midpoint] == target:
        return midpoint

    # If the target is smaller then go left
    elif arr[midpoint] > target:
        return binary_search(arr, target, start, midpoint - 1)

    # If target is larger go right
    else:
        return binary_search(arr, target, midpoint + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here
