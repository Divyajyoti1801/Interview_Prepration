"""
Problem Statement: 
    - Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
I/P : arr[] = {7,10,4,20,15} k = 4
O/P : 15
"""

def K_Smallest(l,k):
    l.sort()
    return l[k-1]

print("Kth Smallest Element: ",K_Smallest([7,10,4,20,15],4))      