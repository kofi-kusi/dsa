def mergeSort(L):
    if len(L) == 1:
        return L

    mid = len(L)//2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])


    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(mergeSort([3, 6, 1, 8, 0, 5]))

