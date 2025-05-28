# Python arrays are dynamic by default, but this is an example of resizing.
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2

    # Insert n in the last position of the array
    def push_back(self, n):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1


    def resize(self):
        self.capacity = 2 * self.capacity
        newArray = [0] * self.capacity

        # Copy elements to newArr
        for i in range(self.length):
            newArray[i] = self.arr[i]
        self.arr = newArray


    def pop_back(self):
        if self.length > 0:
            self.arr[self.length - 1] = 0
            self.length -= 1

    # Get value at i-th index
    def get(self, i):
        if i < self.length:
            return self.arr[i]
        else:
            return "index out of range"

    def show_arr(self):
        for i in range(self.length):
            print(self.arr[i])
