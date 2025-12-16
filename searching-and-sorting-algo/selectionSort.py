# Example 1
def selectionSort(L):
    for i in range(len(L)):
        minItem = i
        for j in range(i+1, len(L)):
            if L[minItem] > L[j]:
                minItem = j
        L[minItem], L[i] = L[i], L[minItem]

    return L

# L = [1, 5, 3, 4, 2, 0]
# print(selectionSort(L))


# Example 2: sorting an array of numbers by selecting and poping the smallest
#            into a new array

# Helper function to find the smallest number
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


# sorting algo
def selectionSort2(arr):
    newArr = []
    copiedArr = arr[:]

    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

# print(selectionSort2([5, 3, 6, 2, 10]))
