# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # Loop through the merged array
    # If the arrays are bigger than zero, find out which element is bigger
    # pop the smaller element into the merged_arr
    for i in range(len(merged_arr)):
        if len(arrA) > 0 and len(arrB) > 0:
            #if arrA at the 0 index is bigger than arrB at 0 index, pop out the element in arrB's 0 index
            if arrA[0] > arrB[0]:
                merged_arr[i] = arrB.pop(0)

            else:
                # pop the element in arrA 0 index
                merged_arr[i] = arrA.pop(0)

        else:
            #if arrA is empty, add the remainder of arrB to merged_array
            if len(arrA) == 0:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    ### 1st version - a bit looonnggg
    # if len(arr) > 1:
    #     # find the middle
    #     middle = len(arr) // 2
    #     left = arr[:middle]
    #     right = arr[middle:]

    #     merge_sort(left)
    #     merge_sort(right)
    #     # initialize index variables to 0
    #     i = j = k = 0
    #     while i < len(left) and j < len(right):
    #         if left[i] < right[j]:
    #             arr[k] = left[i]
    #             i += 1

    #         else:
    #             arr[k] = right[j]
    #             j += 1
    #         k += 1

    #     while i < len(left):
    #         arr[k] = left[i]
    #         i += 1
    #         k += 1

    #     while j < len(right):
    #         arr[k] = right[j]
    #         j += 1
    #         k += 1

## version 2
    # check if array is longer than 1
    if len(arr) > 1:
        # find the middle of left and right
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        # use merge() to merge arrays
        arr = merge(left,right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

