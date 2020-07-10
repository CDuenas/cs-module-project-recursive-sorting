# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # Count system needed for when all elements in one array have been merged
    a = 0
    b = 0

    # begin merging from both lists from 0 to elements because elements is the length
    # of both lists
    for i in range(0, elements):
        # If all elements in arrA have been merged
        # add the next element in arrB to the end of the merged list
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        # If all elements in arrB have been merged
        # add the next element in arrA to the end of the merged list
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # If element in arrA is smaller than element in arrB
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        # Only case left element in arrB is smaller than element in arrA
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:

        midpoint = len(arr) // 2
        left = arr[:midpoint]
        right = arr[midpoint:]
        return merge(merge_sort(left), merge_sort(right))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
