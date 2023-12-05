"""
FIND K CLOSEST ELEMENTS 

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
"""


def find_k_closest_element_BS(arr, k, x):
    l, r = 0, len(arr)-k
    while l < r:
        m = l + ((r-l)//2)
        if x-arr[m] > arr[m+k] - x:
            l = m + 1
        else:
            r = m
    return arr[l:l+k]


print("Find K Closest Element : ",
      find_k_closest_element_BS([1, 2, 3, 4, 5], 4, 3))
