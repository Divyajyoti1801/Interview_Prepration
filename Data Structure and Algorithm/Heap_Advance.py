"""
HEAP ADVANCE QUESTIONS AND CONCEPTS
"""
import heapq
"""
Problem Statement: Sort K Sorted Array
    Efficient Solution: Using Min-Heap Concept
"""
def k_sorted_array(arr,k):
    n = len(arr)
    pq = arr[:k+1]
    heapq.heapify(pq)
    
    index = 0
    for i in range(k+1,n):
        arr[index] = heapq.heappop(pq)
        index+=1
        heapq.heappush(pq,arr[i])
    
    while pq:
        arr[index] = heapq.heappop(pq)
        index+=1
arr_1 = [2,6,3,12,56,8]
k = 3
k_sorted_array(arr_1,k)
print("Kth Sorted Array: ",arr_1)
print()
"""
Problem Statement : Purchase Maximum items
"""
def purchase_maximum_items_1(arr=[],sum=0):
    res = 0
    arr.sort()
    for i in arr:
        if i <= sum:
            sum-=i
            res+=1
        else:
            break
    return res
print("Purchase maximum items (Naive): ",purchase_maximum_items_1([1,12,5,111,200],10))
def purchase_maximum_items_2(arr=[],sum=0):
    res = 0
    pq = arr
    heapq.heapify(pq)

    for i in arr:
        top = heapq.heappop(pq)
        if top<=sum:
            sum-=top
            res+=1
        else:
            break
    return res
print("Purchase maximum items (Efficient): ",purchase_maximum_items_2([1,12,5,111,200],10))
print()
"""
Problem Statement: Kth Largest Elements
    1st Approach : Max-Heap Concepts O(n + k log(n))
    Efficient Approach:
        - Build a Min-Heap of first K items
        - Traverse from (K+1)th element
            = Compare current element with top of heap. If Smaller that top, ignore it.
            = Else remove the top element and insert the current element in the min Heap
        - Print Content of min-heap
        - Time Complexity : O(k + (n-k) * log(k))
"""
def Kth_largest_element(arr,size,k):
    min_heap = []
    for i in range(k):
        min_heap.append(arr[i])
        heapq.heapify(min_heap)

    for i in range(k,size):
        if min_heap[0] > arr[i]:
            continue
        else:
            min_heap[0] = min_heap[-1]
            min_heap.pop()
            min_heap.append(arr[i])
            heapq.heapify(min_heap)
    for i in min_heap:
        print(i,end= " ")
print("Kth largest element in the array: ")
arr_2 = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
Kth_largest_element(arr_2,len(arr_2),3)
print() 

"""
Problem Statement : K Closest Elements
"""
def K_closest_elements_1(arr,k,x):
    for i in range(k):
        mi = 0
        for i in range(1,len(arr)):
            if (abs(arr[mi]-x)>abs(arr[i]-x)):
                mi = i
        print(arr[mi],end = " ")
        arr.pop(mi)
arr_3 = [10,31,5,40,38,80]
print("K Closest Element (Naive): ")
K_closest_elements_1(arr_3,3,35);
print()
def K_closest_element_2(arr,x,k):
    h = []
    for i in range(k):
        heapq.heappush(h,(-abs(arr[i]-x),i))
    for i in range(k,len(arr)):
        curr = -abs(arr[i]-x)
        p,pi=h[0]
        if curr>p:
            heapq.heappop(h)
            heapq.heappush(h,(curr,i))
    while h:
        p,pi = heapq.heappop(h)
        print(arr[pi],end=" ")
print("K Closest Element(Efficient): ")
K_closest_element_2(arr_3,35,3)
print()

"""
Problem Statement: Merge K Sorted Array
"""
def merge_k_sorted_array(arr):
    res = []
    h = []
    for i in range(len(arr)):
        heapq.heappush(h,(arr[i][0],i,0))
    while h:
        val,ap,vp = heapq.heappop(h)
        res.append(val)
        if (vp+1 < len(arr[ap])):
            heapq.heappush(h,(arr[ap][vp+1],ap,vp+1))
    return res

arr_4 = [[10,20,30],[5,15],[1,9,11,18]]
print("Merge k Sorted Arrays: ",merge_k_sorted_array(arr_4))

"""
Problem Statement: Median of a stream
    Idea for Implementation:
        - s : Max-Heap containing Smaller Half
        - g : Min-Heap containing Smaller Half
        - Do the following for every item x:
            = s.push(x)
            = g.push(s.pop())
            = if size(g) > size(s): s.push(g,pop()) 
            = if size(s) > size(g): print(s.top())
                else: print(s.top()+g.top())           
"""
