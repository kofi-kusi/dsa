# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].


def shuffle(self, nums, n):
    x = 0
    y = n
    arr = []
    for i in range(n):
        arr.append(nums[x])
        arr.append(nums[y])
        x += 1
        y += 1
    return arr
