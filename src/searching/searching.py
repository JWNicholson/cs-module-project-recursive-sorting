# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    found = -1

    if start <= end:
        # find the middle
        middle = (start + end) // 2
        #if element is present at the middle
        if arr[middle] == target:
            found = middle

        elif arr[middle] < target:
            # if middle is smaller than target, the element has to be on right
            return binary_search(arr, target, middle + 1, end)
        else:
            # target has to be on the left
            return binary_search(arr, target, start, middle - 1)
    return found
   
        

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here
    
