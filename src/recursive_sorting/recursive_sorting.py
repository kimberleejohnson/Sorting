# Merge Sort function USING RECURSION
## Split list in half, using a midpoint 
## Sorts halfs as it brings them back together 

def merge_sort(l):
    # Base case for recursion, exits out if 0 or 1 value, returning original, to avoid error 
    if len(l) <= 1:
        return l 

    # Middle index for splitting list in half 
    middle_index = len(l) // 2

    # Halves, set up using slice 
    ## Also need to pass halves to merge_sort, recursively
    left_values = merge_sort(l[:middle_index])
    right_values = merge_sort(l[middle_index:])

    ## Indices that we use to keep track as we sort
    right_index = 0
    left_index = 0 

    ## Empty list for storing the sorted values as we go 
    sorted_l = [] 

    # Loop through until we've gone through all values on each side 
    while left_index < len(left_values) and right_index < len(right_values): 
        
        # Compare values, push smallest to empty sorted array, increment index of one pushed 
        if left_values[left_index] < right_values[right_index]:
            sorted_l.append(left_values[left_index])
            left_index += 1
        else: 
            sorted_l.append(right_values[right_index])
            right_index += 1
    # Copy remainders of lists over 
    sorted_l += left_values[left_index:]
    sorted_l += right_values[right_index:]

    # Return sorted 
    return sorted_l


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
