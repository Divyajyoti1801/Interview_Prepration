"""
Problem - 6 : Remove duplicate from sorted Array

Problem Statement:
    - Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
    - Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
        = Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
        = Return k.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]   
"""

def remove_duplicate_from_sorted_arr(arr=[]):
    j = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j+=1
    return j

print("Remove duplicate from sorted array: ",remove_duplicate_from_sorted_arr([1,1,2]))