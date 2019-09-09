# Selection_sort() function 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        # Find next smallest element, with another loop 
        # Compare i to all values after the one next to i 
        for j in range(i + 1, len[arr]):
            # If the smallest index is smaller than the value at j, j is the new smallest
            if arr[smallest_index] > arr[j]:
                smallest_index = j 
             
    # Swap the new smallest index with the first 
    arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr