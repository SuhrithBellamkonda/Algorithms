"""
Binary Search
- a search algorithm that finds the position of a target value within a sorted array
- recursive implementation
"""
def binarySearch(lst, value, low, high, iterations=0):
    mid = (low+high) // 2
    print("Mid is ", mid, " with value ", lst[mid])
    if high>=low:
        if value == lst[mid]:
            print("I found ", value, " at position ", mid, "! -- Recursive calls: ", iterations)
            return mid
        elif value > lst[mid]:
            print("-> ", value, "is higher than ", lst[mid], " so I'll search the sublist ", lst[mid:])
            return binarySearch(lst, value, mid+1, high, iterations+1)
        else:
            print("-> ", value, "is lower than ", lst[mid], " so I'll search the sublist ", lst[low:mid])
            return binarySearch(lst, value, low, mid-1, iterations+1)
    else:
        print("I could not find the value :( -- Recursive calls: ", iterations)
        return None
    
lst = [1, 2, 3, 4, 6, 7, 8, 9, 10, 14, 15, 18, 21, 24, 29, 30, 32, 37]
binarySearch(lst, 30, 0, len(lst)-1)
    