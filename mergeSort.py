"""
Merge Sort
- divide and conquer sorting algorithm
"""

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half until len(arr) == 1
        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              arr[k] = left[i]
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1

arr = [1, 4, 3, 2, 5, 6, 0, 1, 2, -1, 17, -2, 16, 19, -10]
print("initial array: ", arr)
mergeSort(arr)
print("sorted array:  ", arr)