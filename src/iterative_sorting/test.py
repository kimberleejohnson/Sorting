## Bubble Sort is good for smaller sorts 
## Making things almost sorted to sorted 

def bubble_sort(arr): 
    has_swapped = True
    # When no swaps have occurred, return 
    while has_swapped: 
        has_swapped = False 
        # Walk through each element in the array 
        for i in range (0, len(arr) - 1): 
            # If the element is out of order from the neighbor...
            if arr[i] > arr[i+1]: 
                # Swap 
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                has_swapped = True
    return arr 

## Selection sort 
## You have the sorted half, and the unsorted half 
## But instead of taking first item, you're going to select smallest item from unsorted half 

smallest_index = 6
smallest_value = 5
l = [1, 2, 3, 4, 5, 6, 8]

l = [1, 2, 3, 4, 5]

def selection_sort(arr): 
    # Divide teh array into sorted and unsorted 
    # loop through each element
    for i in range(len(arr) - 1): 

        # Starting with assumption start is smallest, before we start 
        current_index = i 
        smallest_index = current_index 

    # find the smallest element in the unsorted 
    for j in range(current_index, len(arr)): 
        if arr[j] < arr[smallest_index]: 
            smallest_index = j
    # Put the smallest element at the end of the sorted 
        # Swap the first element of unsorted with the smallest element 
        arr[smallest_index], arr[current_index] = arr[current_index], arr[smallest_index]
        
    return arr 

