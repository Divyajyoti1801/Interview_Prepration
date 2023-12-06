"""
FIND MINIMUM IN ROTATED SORTED ARRAY 

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time


Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""


def minimum_in_rotated_sorted_array(nums):
    res = nums[0]
    l = 0
    r = len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        m = l + ((r-l)//2)
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res


print("Find minimum in rotated sorted array: ",
      minimum_in_rotated_sorted_array([3, 4, 5, 1, 2]))
