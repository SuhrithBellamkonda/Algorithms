"""
Quick Sort
- divide and conquer sorting algorithm
"""

#calls itself recursively around a pivot position provided by partition
def quickSort(arr, low, high):
    if (low+1 < high):
        j = partition(arr, low, high)
        #call quickSort on "lower" subarray
        quickSort(arr, low, j)
        #call quickSort on "upper" subarray
        quickSort(arr, j+1, high)

#helper function that gives a pivot position to call quickSort on recursively
def partition(arr, low, high):
    #take the first element value as the pivot value
    pivot = arr[low]
    i = low+1
    j = high-1
    while i <= j:
        #increment i and decrement j until you reach the pivot value
        while arr[i] <= pivot:
            i+=1
            break
        while arr[j] >= pivot:
            j-=1
            break
        #as long as i has not exceeded j, swap elements at positions i and j
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    #once i has exceeded j, we exit out of the loop
    #swap our pivot value with the intermediate value at position j
    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = [1, 4, 3, 2, 5, 6, 0, 1, 2, -1, 17, -2, 16, 19, -10]
print("initial array: ", arr)
quickSort(arr, 0, len(arr))
print("sorted array:  ", arr)