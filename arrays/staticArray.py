# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).

# insert end
def insert_end(arr, length, capacity, n):
    if length < capacity:
        arr[length] = n

# remove end
def remove_end(arr, length):
    if length > 0:
        arr[length] = 0

# insert middle
# Assuming i is a valid index and arr is not full.
def insert_middle(arr, i, n, length):
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
        arr[i] = n

# remove middle
def remove_middle(arr, i, length):
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]

# show arr
def print_arr(arr, capacity):
    for i in range(capacity):
        print(arr[i])

