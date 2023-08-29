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
#Using Concept of Hoare's Partition
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

"""
Problem Statement: Sort an Array with Three types
    - Sort an Array of 0's, 1's and 2's
    - Three way Partitioning
    - Partition around a range
"""
def three_way_partition_1(arr):
    n = len(arr)
    i=0
    temp = [0]*n
    for j in range(0,n):
        if arr[j]==0:
            temp[i] = arr[j]
            i+=1
    
    for j in range(0,n):
        if arr[j]==1:
            temp[i] = arr[j]
            i+=1
    
    for j in range(0,n):
        if arr[j] == 2:
            temp[i] = arr[j]
            i+=1
    
    arr[:] = temp
    return arr
print("Three way partition (Naive): ",three_way_partition_1([0,1,0,2,1,2]))
# Efficient Method: Dutch National Flag Algorithm
def dutch_national_flag(arr):
    low,mid,high = 0,0,len(arr)-1
    while mid<=high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[high],arr[mid] = arr[mid],arr[high]
            high -=1
list_2 = [0,1,2,1,1,2]
dutch_national_flag(list_2)
print("Dutch National Flag Algorithm: ",list_2)
print()

"""
Problem Statement: Merge Overlapping Intervals
I/P: [[1,3],[2,4],[5,7],[6,8]]
O/P: [[1,4],[5,8]] 
"""
def over_lapping_1(arr):
    arr.sort(key = lambda x:x[0])
    res = 0
    for i in range(1,len(arr)):
        if arr[res][1]>=arr[i][0]:
            arr[res][1] = max(arr[res][1],arr[i][1])
        else:
            res += 1
            arr[res] = arr[i]
    for i in range(res+1):
        print(arr[i],end = " ")
    print()
print("Over-Lapping Intervals (Efficient) [[1,3],[2,4],[5,7],[6,8]] : ")
over_lapping_1([[1,3],[2,4],[5,7],[6,8]])
print()

"""
Problem Statement: Meeting the maximum guests
I/P: arr[]=[900,940], dep[]  = [1000,1030]
O/P: 2
"""
def meet_maximum_guests(arr,dep):
    arr.sort()
    dep.sort()
    n = len(arr)
    i,j = 1,0
    curr,res = 1,1
    while(i<n and j<n):
        if arr[i] <= dep[j]:
            curr+=1
            i+=1
        else:
            curr-=1
            j+=1
        res = max(res,curr)
    return res
list_3 = [900,600,700]
dep = [1000,800,730]
print("Meeting the maximum guests: ",meet_maximum_guests(list_3,dep))
print()
"""
Advance Sorting Algorithm: Counting Sort
    - Time Complexity: O(n+k) if k <= linear;
    - Auxiliary Space: O(n+k)
    - Stable Algorithm
    - Used as subroutine for Radix Sort
"""
def counting_sort_naive(arr,k):
    count = [0]*k

    for x in arr:
        count[x]+=1
    idx = 0
    for i in range(k):
        for j in range(count[i]):
            arr[idx] = i
            idx+=1
# There is a problem: Would not work for an array of objects like an array of students to be sorted

def counting_sort(arr,k):
    output = [0] * len(arr)
    count = [0] * (k)
    for x in arr:
        count[x] +=1
    for i in range(1,k):
        count[i] += count[i-1]
    for x in reversed(arr):
        output[count[x]-1]=x
        count[x]-=1
    arr[:] = output
    return arr
print("Counting Sort: ",counting_sort([1,4,4,1,0,1],5))

"""
Advance Sorting Algorithm: Cycle Sort
"""