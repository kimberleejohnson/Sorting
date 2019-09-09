# Selection_sort() function 
def selection_sort( arr ):
    # Loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Find next smallest element, with another loop starting at the index one after i 
        for j in range(i + 1, len(arr)):
            # If the value at i is greater than the value at j, j is the new smallest
            if arr[i] > arr[j]:
                # Swap the new smallest index with the first 
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# Bubble Sort function below
def bubble_sort( arr ):
    complete = False 
    while not complete: 
        swapped = False 
        for i in range(1, len(arr)): 
            if arr[i - 1] > arr[i]:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp
                swapped = True 
        if not swapped: 
            complete = True 
    return arr 


# STRETCH: implement the Count Sort function below
#def count_sort( arr, maximum=-1 ):

    #return arr