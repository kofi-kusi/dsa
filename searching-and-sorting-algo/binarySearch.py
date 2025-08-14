def binarySearch(L, e):
    """
    Check if an element is in a list

    L (integer[]): a list of items
    e (integer): item to be checked

    Returns: True if e in L, False otherwise
    """
    low = 0
    high = len(L) - 1

    while low <= high:
        mid = (low + high)//2

        if L[mid] == e:
            return True
        elif L[mid] > e:
            high = mid - 1
        else:
            low = mid + 1

    return False

# Recursive implementation
def binarySearchRecur(L, e):
    """
    Check if an element is in a list

    L (integer[]): a list of items
    e (integer): item to be checked

    Returns: True if e in L, False otherwise
    """
    low = 0
    high = len(L) - 1
    result = search_helper(L, e, low, high)

    return result

def search_helper(L, e, low, high):
    if len(L) == 0:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            high = mid - 1
            return search_helper(L, e, low, high)
        else:
            low = mid + 1
            return search_helper(L, e, low, high)


L = [1, 2, 3, 4, 5]
print(binarySearch(L, 2))
# print(binarySearchRecur(L, 2))
