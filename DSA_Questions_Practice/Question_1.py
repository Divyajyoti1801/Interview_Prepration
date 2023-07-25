"""
Problem Statement: Reverse the array

I/P: arr[] = {1,2,3}
O/P: arr[] = {3,2,1}
"""

def reverse_array(l):
    if len(l) == 0:
        return []
    return l[::-1]

print("Reverse of the array: ",reverse_array([1,2,3]))