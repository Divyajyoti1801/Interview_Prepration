
"""
SORTING BASICS ALGORITHM AND QUESTIONS

    - sort()
        - Works only for list 
        - sorts in-place
    
    - sorted()
        - Works for any iterable
        - Does not modify the passed container 
        - Return a list of sorted items
    
    - Both use TimSort and both are stable
"""

# Sorting user defined Objects using List Sort
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __lt__(self,other):
        return self.x<other.x

object_list=[Point(1,15),Point(10,5),Point(5,8)]
object_list.sort()

print("Sorting Of User Defined Object:")
for i in object_list:
    print(i.x, i.y)
print()

# Sorting using Sorted function
print("Sorting of Set:") 
print(sorted((10,12,5,1)))
print()
print("Sorting of Tuple: ")
print(sorted({"gfg","course","python"}))
print()
print("Sorting of the string:")
print(sorted("gfg"))
print()
print("Sorting of Dictionary:")
print(sorted({10:"gfg",15:"ide",5:"course"}))
print()
print("Sorting of list of sets:")
print(sorted([(10,15),(1,8),(2,3)]))

"""
Stability In Sorting Algorithms

l = [("Anil",50),("Ayan",80),("Piyush",50),("Ramesh",80)]

Stable Sorting Algorithm:
l = [("Anil",50),("Piyush",50),("Ayan",80),("Ramesh",80)]

Unstable Sorting Algorithm:
l = [("Piyush",50),("Anil",50),("Ayan",80),("Ramesh",80)]

Examples Stable Sorts: Bubble Sort, Insertion Sort, Merge Sort.....

Examples Unstable Sorts: Selection Sort, Quick Sort, Heap Sort.....

"""

"""
Sorting Algorithm: BUBBLE SORT
    - Time Complexity: O(n^2)
    - No. of Passes: n-1
    - Stable Algorithm
"""
def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
# Time Complexity of this version: theta(n^2)
list_1= [10,8,20,5]
bubble_sort(list_1)
print("After Bubble Sort: ",list_1)

def bubble_sort_optimized(l):
    n= len(l)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped = True
        if swapped == False:
            return
list_2 = [3,5,10,20,40]
bubble_sort_optimized(list_2)
print("After Bubble Sort Optimized: ",list_2)

"""
Sorting Algorithm: SELECTION SORT
    - Time Complexity: O(n^2)
    - Does less memory writes compared to Quick Sort, Merge Sort, Insertion Sort etc, But Cycle sort is optimal in terms of memory writes
    - Basic idea for HeapSort
    - Not Stable
    - In-Place
"""

def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        min_ind=i
        for j in range(i+1,n):
            if l[j] < l[min_ind]:
                min_ind = j
        l[min_ind],l[i] = l[i],l[min_ind]

list_3 = [10,5,8,20,2,18]
selection_sort(list_3)
print("After Selection Sort: ",list_3)

"""
Sorting Algorithm: INSERTION SORT
    - Time Complexity: O(n^2)
    - In-Place and Stable
    - Used in practice for small arrays
"""
def insertion_sort(l):
    for i in range(1,len(l)):
        x = l[i]
        j = i-1
        
        while j>=0 and x<l[j]:
            l[j+1] = l[j]
            j = j-1
        l[j+1] = x

list_4 = [20,5,40,60,10,30]
insertion_sort(list_4)
print("After Insertion Sort: ",list_4)

"""
Sorting Algorithm: MERGE SORT ALGORITHM
    - Divide and Conqueror Algorithm
    - Stable Algorithm
    - O(nlog(n)) time complexity and O(n) Auxiliary Space
    - Used in External Sorting
    - Outperformed by Quicksort
"""
"""
First Step - 1:
    Merge Two Sorted Lists
    
    I/P: l1 = [10,15], l2 = [5,6,6,30,40]
    O/P: [5,6,6,10,15,30,40]
    
    Time Complexity: O(m+n)
    Space Complexity: O(n)
"""
def merger_sorted_arrays(l1,l2):
    res=[]
    i=0 
    j=0
    m=len(l1)
    n=len(l2)
    
    while i<m and j<n:
        if l1[i]<l2[j]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    while i<m:
        res.append(l1[i])
        i+=1
    while j<n:
        res.append(l2[j])
        j+=1
    return res
print("Merge of Sorted List: ",merger_sorted_arrays([10,15],[5,6,6,30,40]))

"""
Second Step - 2:
    Merge Of Subarray

I/P: l1 = [10,15,20,11,13]
O/P: [10,11,13,15,20]

Time Complexity: O(m+n)
Auxiliary Space: O(m+n)
"""
def merge_sub_array(l,low,mid,high):
    left=l[low:mid+1]
    right=l[mid+1:high+1]
    i=0
    j=0
    k=low
    
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            l[k]=left[i]
            k+=1
            i+=1
        else:
            l[k]=right[j]
            k+=1
            j+=1
    while i<len(left):
        l[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        l[k]=right[j]
        j+=1
        k+=1

"""
Step Three - 3:
    Merge Sort Recursive function
    
    I/P: arr = [10,5,30,15,7]
    O/P: [5,7,10,15,30]

    Time Complexity: O(nlog(n))
    Auxiliary Space: O(n)

"""
def merge_sort(arr,l,r):
    if r>l:
        m=(r+l)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge_sub_array(arr,l,m,r)

list_5=[10,5,30,15,7]
merge_sort(list_5,0,len(list_5)-1)
print("After MergeSort: ",list_5)

"""
Problem Statement: union of two sorted lists
I/P: l1 = [3,5,8] l2 = [2,8,9,10,15]
O/P: [2,3,5,8,9,10,15]

Time Complexity: O(m+n)
"""
def union_of_list(l1,l2):
    m=len(l1)
    n=len(l2)
    i=j=0
    while i<m and j<n:
        if(i>0 and l1[i]==l1[i-1]):
            i+=1
        elif(j>0 and l2[j]==l2[j-1]):
            j+=1
        elif(l1[i]<l2[j]):
            print(l1[i],end=" ")
            i+=1
        elif(l1[i]>l2[j]):
            print(l2[i],end=" ")
            j+=1
        else:
            print(l1[i],end=" ")
            i+=1
            j+=1
    
    while i<len(l1):
        if(i>0 and l1[i]!=l1[i-1]):
            print(l1[i],end=" ")
        i+=1
    while j<len(l2):
        if(j>0 and l2[j]!=l2[j-1]):
            print(l2[j],end=" ")
        j+=1
print()
print("Union of Two Sorted List: ")
union_of_list([2,20,20,20,40],[1,10,20])

""""
Problem Statement: Intersection of two sorted array

I/P: l1 = [3,5,10,10,10,15,15,20]
     l2 = [5,10,10,15,30]

O/P: 5 10 15

Time Complexity: 
"""
def intersection_of_list(l1,l2):
    m=len(l1)
    n=len(l2)
    i=j=0
    while(i<m and j<n):
        if(i>0 and l1[i-1]==l1[i]):
            i+=1
            continue
        if(l1[i]<l2[j]):
            i+=1
        elif l2[j]<l1[i]:
            j+=1
        else:
            print(l1[i],end=" ")
            i+=1
            j+=1
print()
print("Intersection of Sorted Array: ")
intersection_of_list([10,20,35,40],[20,35,50,90])

"""
Problem Statement: Count inversions in an array

Concept: A pair (arr[i],arr[j]) forms an count inversion when i<j and arr[i]>arr[j]

I/P: [2,4,1,3,5]
O/P: 3
"""
def naive_count_inversions(l):
    n = len(l)
    res = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if l[i] > l[j]:
                res+=1
    return res
print()
print("Count Inversions in list Part-1: ",naive_count_inversions([2,4,1,3,5]))

#Efficient Solution
def count_inversion(arr,l,r):
    res=0 
    if(l<r):
        m = (l+r)//2
        res += count_inversion(arr,l,m)
        res += count_inversion(arr,m+1,r)
        res += count_merge(arr,l,m,r)
    return res

def count_merge(arr,l,m,r):
    left=arr[l:m+1]
    right=arr[m+1:r+1]
    i=0
    j=0
    res=0
    k=l
    while (i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            arr[k]= left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
            res+=(len(left)-i)
        k+=1
    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    return res

print("Count Inversion of List Part-2: ",count_inversion([2,4,1,3,5],0,len([2,4,1,3,5])))

"""
Problem Statement: Partition a Given Array
I/P: l = [3,8,6,12,10,7] p=5
O/P: l = [3,6,7,8,12,10]
"""
def partition_list_naive(l,p):
    n=len(l)
    l[p],l[n-1]=l[n-1],l[p]
    temp =[]
    for x in l:
        if x<=l[n-1]:
            temp.append(x)
    for x in l:
        if x > l[n-1]:
            temp.append(x)
    for i in range(len(l)):
        l[i]=temp[i]
print()
print("Partition of list Naive: ")
list_6=[5,13,6,9,12,8,11]
partition_list_naive(list_6,5)
print(list_6)

"""
Partition Algorithm: LOMUTO PARTITION
    - Time Complexity: O(n)
    - Auxiliary Space: O(1)
"""
def lomuto_partition(arr,l,h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1

"""
Partition Algorithm: HOARE PARTITION
    - Time Complexity: O(n)
    - Auxiliary Space: O(1)
"""
def hoare_partition(arr,l,h):
    pivot=arr[l]
    i = l-1
    j=h+1
    while(True):
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while(arr[j]>pivot):
            j-=1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]

"""
Sorting Algorithm: QUICK SORT ALGORITHM
    - Divide and Conqueror
    - Time Complexity: O(n^2)
    - Despite O(n^2) worst case, it is considered faster, because of the following reasons.
        - In-place
        - Cache Friendly
        - Average Case is O(nlog(n))
        - Tail Recursive
    - Partition is key Function
    - Time Complexity: O(nlog(n))
    - Auxiliary Space: O(log(n))
"""
# Quick Sort Using Lomuto Partition
def quick_sort(arr,l,h):
    if l<h:
        p = lomuto_partition(arr,l,h)
        quick_sort(arr,l,p-1)
        quick_sort(arr,p+1,h)

list_7 = [8,4,7,9,3,10,5]
quick_sort(list_7,0,len(list_7)-1)
print()
print("After Quick Sort: ",list_7)

# Quick Sort Using Hoar's Partition
def quick_sort_2(arr,l,h):
    if l<h:
        p = hoare_partition(arr,l,h)
        quick_sort_2(arr,l,p)
        quick_sort_2(arr,p+1,h)
quick_sort_2(list_7,0,len(list_7)-1)
print()
print("After Quick Sort: ",list_7)

"""
Sorting Algorithm: HEAP SORT
    - Can be seen as an optimization over selection sort
    - Two Steps:
        - Build a Max Heap
        - Repeatedly SWAP root with last node, reduce heap size by 1 and heapify
    - Time Complexity: O(nlog(n))
    - Auxiliary Space: O(1)
    - Not Stable
    - Used in Hybrid Sorting Algorithm like as Intro Sort
"""
def heap_sort():
    