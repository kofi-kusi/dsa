# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.


def getConcatenation(self, nums):
    ans = [0] * (2 * len(nums))
    for i in range(len(nums)):
        ans[i] = nums[i]
        ans[i + len(nums)] = nums[i]
    return ans
