# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    while arrA and arrB:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    merged_arr.extend(arrA)
    merged_arr.extend(arrB)
    return merged_arr

print(merge([1, 2, 16, 72, 100], [1, 4, 9, 23, 90]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        arr = merge(left, right)
    return arr

print(merge_sort([7, 3, 9, 4, 2, 10, 6, 0, 2, 1]))


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
