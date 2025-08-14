def selectionSort(L):
    for i in range(len(L)):
        minItem = i
        for j in range(i+1, len(L)):
            if L[minItem] > L[j]:
                minItem = j
        L[minItem], L[i] = L[i], L[minItem]

    return L

L = [1, 5, 3, 4, 2, 0]
print(selectionSort(L))
