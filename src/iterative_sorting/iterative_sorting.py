# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range (i+1, len(arr)):
            if arr[j]<arr[smallest_index]:
                smallest_index=j 
        # TO-DO: swap
        arr[i], arr[smallest_index]=arr[smallest_index], arr[i]
    print("Sorted arr", arr)
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1):
            if arr[j+1]<arr[j]:
                print(f"{arr[j+1]}<{arr[j+1]}")
                arr[j+1], arr[j]=arr[j], arr[j+1]
            else:
                print(f"{arr[i+1]}!<{arr[i+1]}")
    print("sorted array", arr)            
    return arr

bubble_sort(arr1)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr