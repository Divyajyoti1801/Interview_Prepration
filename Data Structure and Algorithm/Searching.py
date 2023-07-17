"""
SEARCHING PART-1
"""

"""
Searching Algorithm: BINARY SEARCH

I/P: l = [10,20,30,40,50,60] x = 20 
O/P: 1

Prerequisite: The Array must be sorted.

Time Complexity: O(log(n))
"""
def binary_search(l,x):
    low=0
    high=len(l)
    
    while(low<=high):
        mid= (low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            low=mid+1
        else:
            high=mid-1
    
    return -1

print(binary_search([10,20,30,40,50,60],20))

"""
RECURSIVE BINARY SEARCH

height of binary tree: log(n)
"""
def recursive_bs(l,x,low,high):
    if low>high:
        return -1
    
    mid = (low+high)//2

    if l[mid] == x:
        return mid
    elif l[mid]>x:
        return recursive_bs(l,x,low,mid-1)
    else:
        return recursive_bs(l,x,mid+1,high)
print(recursive_bs([10,20,30,40,50],20,0,len([10,20,30,40,50])))

"""
Problem Statement: Given a shorted array find the index of shorted array.

I/P: arr[] = {1,10,10,10,20,20,40} x = 20
O/P: 4
"""
def first_occurrence(l,x,low,high):
    if low>high:
        return -1
    mid = (low+high)//2

    if x > l[mid]:
        return first_occurrence(l,x,mid+1,high)
    elif  x < l[mid]:
        return first_occurrence(l,x,low,mid-1)
    else:
        if mid==0 or l[mid-1]!=l[mid]:
            return mid
        else:
            return first_occurrence(l,x,low,mid-1)

print(first_occurrence([10,20,20,20,30,30],20,0,len([10,20,20,20,30,30])))
"""
Problem Statement: Given a shorted array find the last occurrence

I/P: l = [10,15,20,20,40,40] x = 20
O/P: 3
"""
def last_occurrence(l,x):
    low=0
    high= len(l)
    if low>high:
        return -1
    
    while low<=high:
        mid=(low+high)//2

        if l[mid]<x:
            low=mid+1
        elif l[mid] >x:
            high=mid-1
        else:
            if mid==len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                low=mid+1
    return -1
print(last_occurrence([10,15,20,20,40,40],20))

"""
Problem Statement: Given a sorted array count all the occurrence

I/P: l=[10,20,20,20,30,30] x=20
O/P: 3
"""
def count_occurrences(l,x,low,high):
    first=first_occurrence(l,x,low,high)
    if first==-1:
        return 0
    else:
        return last_occurrence(l,x)- first +1
print(count_occurrences([10,20,20,20,30,30],20,0,len([10,20,20,20,30,30])))

"""
Problem Statement: Count 1's in a sorted binary list.

I/P: l = [0,0,0,1,1,1,1]
O/P: 4
"""
def count_ones(l):
    low=0
    high= len(l)
    while(low<=high):
        mid = (low + high)//2
        if l[mid]< 1:
            high=mid-1
        elif l[mid] > 1:
            low = mid + 1
        else:
            if mid == len(l)-1 or l[mid+1] != 1:
                return mid + 1
            else:
                low=mid+1
    return 0
print(count_ones([1,1,1,1,0,0,0]))

"""
Problem Statement: Square root of a number

I/P: x =4
O/P: 2
"""
def square_root(x):
    i =1
    while i*i<=x:
        i+=1
    return i-1
print("Square Root: ",square_root(4))

def square_root_2(x):
    low = 1
    high = x
    ans = -1
    while low <= high:
        mid = (low + high)//2
        msq = mid * mid
        if msq == x:
            return mid
        elif msq > x:
            high = mid -1 
        else:
            low = mid + 1
            ans = mid
    return ans
print(square_root_2(9))