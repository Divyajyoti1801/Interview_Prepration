"""
SORTING ADVANCE
    
    - Overview Of Sorting Algorithm
        = Binary Array : Partition Algorithm (Lomuto and Hoare Algorithm)
        = Array with three values: Quick sort algorithm
        = Array of size n and small ranged values : Counting Sort (Auxiliary Space: O(k), Time Complexity: O(n + k))
        = Array of size and range is of size n^3 or n^2 or closer : Radix Sort
        = Array of uniformly distributed across a range: Bucket Sort
        = When memory writes are costly: Selection Sort & Cycle Sort
        = When adjacent swaps are allowed: Bubble Sort & Cocktail Sort
        = When array size is small: Insertion Sort
        = When available extra memory is less: Shall Sort (n((log(n)^2))
    
    - General Purpose Sorting Algorithm: 
        = Merge Sort
        = Heap Sort
        = Quick Sort
    
    - Hybrid Algorithm
        = Tim Sort
        = Intro Sort
"""

"""
Tail Call Elimination of Quick Sort Algorithm
    - Generally, Quick sort is a tail recursive function
    - Well, Tail recursive function allows us for more optimization.
def Quick_Sort(arr,l,r):
    if l < r:
        p = partition(arr,l,r)
        Quick_Sort(arr,l,p)
        Quick_Sort(arr,p+1,r)
"""
# Lomuto's Partition Algorithm
def partition(arr,l,h):
    pivot = arr[h]
    i = l
    for j in range(l,h):
        if arr[j]<=pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    arr[i],arr[h] = arr[h],arr[i]
    return i

def quick_sort(arr,l,r):
    while l<r:
        p = partition(arr,l,r)
        quick_sort(arr,l,p)
        l = p + 1

"""
Problem Statement : Kth Smallest element
"""
def kth_smallest_1(arr,k):
    arr.sort()
    return arr[k-1]
print("Kth smallest Element O(nlog(n)): ", kth_smallest_1([10,4,5,8,11,6,26],5))
# Function is called "QUICK SELECT FUNCTION"
def kth_smallest_2(arr,k):
    l = 0
    r = len(arr)-1
    while l<=r:
        p = partition(arr,l,r)
        if p == k-1:
            return p
        elif p > k-1:
            r = p-1
        else:
            l = p+1
    return -1
print("Kth smallest Element efficient: ",kth_smallest_2([10,4,5,8,11,6,26],5))
print()
"""
Problem Statement: Minimum difference in the array
"""
def minimum_difference_1(arr):
    res = float("inf")
    for i in range(1,len(arr)):
        for j in range(i):
            res = min(res,abs(arr[i]-arr[j]))
    return res
print("Minimum difference in array (O(n^2)): ",minimum_difference_1([5,3,8]))
def minimum_difference_2(arr):
    res = float("inf")
    arr.sort()
    for i in range(1,len(arr)):
        res = min(res,(arr[i]-arr[i-1]))
    return res
print("Minimum difference Efficient: ",minimum_difference_2([5,3,8]))
print()

"""
Problem Statement: Chocolate Distribution Problem 
"""
def chocolate_distribution(arr,m):
    if m == 0 or len(arr) == 0:
        return 0
    if len(arr) < m:
        return -1
    arr.sort()
    
    res = arr[m-1] - arr[0]
    for i in range(1,len(arr)-m+1):
        res = min(res,arr[i+m-1]-arr[i])
    return res
print("Chocolate Distribution Problem: ",chocolate_distribution([7,3,1,8,9,12,56],3))
print()

"""
Sort an Array with Two Types:
    - Segregate positive and negative
    - Segregate Even and odd
    - Sort a Binary Array
"""
def sort_two_type_1(arr):
    n = len(arr)
    temp = [0] * n
    i = 0
    for j in range(0,n):
        if arr[j] < 0:
            temp[i] = arr[j]
            i+=1
    for j in range(0,n):
        if arr[j]>=0:
            temp[i] = arr[j]
            i+=1
    arr[:] = temp
    return arr

print("Sort an Array of two types (+/-): ",sort_two_type_1([13,-12,18,-10]))
def sort_two_type_2(arr):
    i,j = -1,len(arr)
    while True:
        i+=1
        while arr[i]<0:
            i+=1
        j-=1
        while arr[j]>=0:
            j-=1
        if i>=j:
            return
        arr[i],arr[j]=arr[j],arr[i]

list_1 = [13,-12,18,-10]
print("Sort an Array of two types (+/-) Efficient: ",sort_two_type_2(list_1))
