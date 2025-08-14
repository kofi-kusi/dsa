def insertionSort(L):
    for i in range(1, len(L)):
        key = L[i]
        last = i - 1

        while last >= 0 and key < L[last]:
            L[last + 1] = L[last]
            last = last - 1

        L[last + 1] = key

L = [1, 5, 3, 4, 2, 0]
insertionSort(L)
print(L)

