# Selection_sort() function 
# Selection sort repeatedly finds the smallest element 

def selection_sort( arr ):
    # Loop through n-1 elements
    for i in range(0, len(arr) - 1):
        
        # Find next smallest element, with another loop starting at the index one after i 
        for j in range(i + 1, len(arr)):
            
            # If the value at i is greater than the value at j, j is the new smallest
            if arr[i] > arr[j]:
                
                # Swap values 
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr


# Bubble Sort function
# Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order 
def bubble_sort( arr ):

    # Set Boolean value for while loop  
    complete = False 

    # While Boolean complete is NOT true 
    while not complete: 

        # Another Boolean for whether values need to be swapped 
        swapped = False 

        # For i in range of first value, and length of array 
        for i in range(1, len(arr)): 

            # If the value before arr[i] is greater than arr[i]
            if arr[i - 1] > arr[i]:

                # Swap the values 
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp
                swapped = True 
        
        # If you don't need to swap the values 
        if not swapped: 
            complete = True 
    return arr 


# STRETCH: implement the Count Sort function below
#def count_sort( arr, maximum=-1 ):

    #return arr