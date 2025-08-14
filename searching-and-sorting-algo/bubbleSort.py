def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j-1], L[j] = L[j], L[j-1]


# 135420
# 134520
# 134250
# 134205
#
# 132405
# 132045
#
# 123045
# 120345
#
# 102345
# 012345

def bubbleSort(L):
    for i in range(len(L)):
        for j in range(0, len(L) - 1 - i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]


L = [1, 5, 3, 4, 2, 0]
bubbleSort(L)
print(L)
