"""
BINARY SEARCH STANDARD ALGORITHM

"""


def binary_search(nums, s):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + ((right-left)//2)
        if nums[mid] == s:
            return mid
        elif nums[mid] < s:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print("Binary Search : ", binary_search([-1, 0, 3, 5, 9, 12], 9))
