def quickSort(L):
    """
    Applies quick sort algorithm to sort the elements in an array

    L (list): a list of numbers
    Returns: a sorted array
    """
    quickSort_helper(L, 0, len(L) - 1)
    return L

def quickSort_helper(my_array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while right >= left:
        if my_array[left] > my_array[pivot] > my_array[right]:
            my_array[left], my_array[right] = my_array[right], my_array[left]

        if my_array[left] > my_array[pivot]:
            left += 1

        if my_array[right] <= my_array[pivot]:
            left += 1

        if my_array[right] >= my_array[pivot]:
            right -= 1

    my_array[pivot], my_array[right] = my_array[right], my_array[pivot]

    quickSort_helper(my_array, start, right - 1)
    quickSort_helper(my_array, right + 1, end)


print(quickSort([4, 1, 3, 7, 5, 2, 6]))


#### Example 2: sorts an array of any length using a recursive approach
def quickSort2(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        
        return quickSort2(less) + [pivot] + quickSort2(greater)
    
print(quickSort2([4, 1, 3, 7, 5, 2, 6]))

