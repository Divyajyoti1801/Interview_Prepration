"""
FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""


def binary_search(nums, target, leftBias):
    l, r = 0, len(nums)-1
    i = -1

    while l <= r:
        m = l + ((r-l)//2)
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            i = m
            if leftBias:
                r = m - 1
            else:
                l = m + 1
    return i


def first_and_last_position_of_element(nums, target):
    left = binary_search(nums, target, True)
    right = binary_search(nums, target, False)
    return [left, right]


print("Find first and last position of element in sorted array: ",
      first_and_last_position_of_element([5, 7, 7, 8, 8, 10], 8))
