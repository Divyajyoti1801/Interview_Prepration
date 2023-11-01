"""
Problem - 8 : MERGE TWO SORTED ARRAYS

Problem Statement : 
    - You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    - Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    - The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]  
    
"""

def merge_two_sorted_array(nums1,m,nums2,n):
    temp  = [-1]*(m+n)
        
    curr,i,j = 0,0,0
    while i<m and j<n:
        if nums1[i]<=nums2[j]:
            temp[curr] = nums1[i]
            i+=1
        else:
            temp[curr]= nums2[j]
            j+=1
        curr +=1

    while i<m:
        temp[curr] = nums1[i]
        i+=1
        curr +=1
    while j<n:
        temp[curr] = nums2[j]
        j+=1
        curr += 1
    
    for i in range(len(temp)):
            nums1[i] = temp[i]
    return nums1
nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]
n = 3
print(merge_two_sorted_array(nums1,m,nums2,n))

