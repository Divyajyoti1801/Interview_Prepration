"""
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
"""


def contains_duplicate(nums):
    return len(nums) != len(set(nums))


print("Contains duplicate : ", contains_duplicate([1, 2, 3, 1]))
