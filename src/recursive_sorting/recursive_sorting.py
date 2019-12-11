# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    #print(f"MERGE arrA: {arrA}, arrB: {arrB}")
    elements = len( arrA ) + len( arrB )
   # merged_arr = [0] * elements
    merged_arr=[]
    indexA, indexB=0,0
    # TO-DO
    while elements>0:
        elements-=1
        if arrA[indexA]<=arrB[indexB]:
            #print(f"{arrA[indexA]}<={arrB[indexB]}")
            merged_arr.append(arrA[indexA])
            if indexA ==len(arrA)-1:
                merged_arr.extend(arrB[indexB:])
                break
            else:
                #print(f"indexA: {indexA} +1")    
                indexA+=1
        elif arrB[indexB]<=arrA[indexA]:
            print(f"{arrB[indexB]}<={arrA[indexA]}")
            merged_arr.append(arrB[indexB])
            if indexB==len(arrB)-1:
                merged_arr.extend(arrA[indexA:])
                break
            else:
                #print(f"indexB: {indexB} +1")      
                indexB+=1

    #print(f"Merged array: {merged_arr}")
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr)<=1:
        #print(f"merge_sort return")
        return arr
    split=round(len(arr)/2)
    #print(f"split: {split}")
    arr1=arr[:split]
    arr2=arr[split:]
    #print(f"MERGE SORT arr1: {arr1}, arr2:{arr2}")
    sorted1=merge_sort(arr1)
    sorted2=merge_sort(arr2)
    arr= merge(sorted1, sorted2)
    return arr


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
