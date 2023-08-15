import math
"""
Data Structure: BINARY HEAP
    - Used in HeapSort
    - Used to implement Priority Queue
    - Two Types
        = Min Heap : Highest Priority item is assigned lowest value
        = Max Heap: Highest Priority item is assigned value
    - Binary heap is a complete Binary Tree (Sorted as an Array)
    - Left Child = (2*i)+1
    - Right Child = (2*i)+2
    - Parent(i) = [(i-1)/2]

    MIN Heap
        - Complete Binary Tree
        - Every node has value smaller than its descendants
"""

"""
Mean Heap Implementation
    - Main Operations:
        = Insert
        = Extract Min
        = Decrease Key
        = Delete
        = Constructor
    - Utility Functions:
        = Left Child
        = Right Child
        = Parent 
        = Min Heapify
"""
class MinHeap:
    def __init__(self):
        self.arr = []
    
    def parent(self,i):
        return (i-1)//2
    
    def leftChild(self,i):
        return (2*i)+1
    
    def rightChild(self,i):
        return (2*i)+2
    """
    Insert in Min-Heap
        - Time Complexity : O(log(n))
    """
    def insert(self,x):
        arr = self.arr
        arr.append(x)
        i = len(arr)-1
        while i>0 and arr[self.parent(i)]>arr[i]:
            p = self.parent(i)
            arr[i],arr[p]=arr[p],arr[i]
            i = p
    
    """
    Extract Min and Heapify
        - Min Heapify Operation
            = Input is a min heap where only the root be violating 
            = We need to fix the violation
            = Time Complexity : O(log(n))
    """
    def min_heapify(self,i):
        arr = self.arr
        lt = self.leftChild(i)
        rt = self.rightChild(i)
        
        smallest = i
        n = len(arr)
        
        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt
        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt
        
        if smallest != i:
            arr[smallest], arr[i] = arr[i],arr[smallest]
            self.min_heapify(smallest)
    
    def extract_min(self):
        arr = self.arr
        n = len(arr)
        if n == 0:
            return math.inf
        res = arr[0]
        arr[0] = arr[n-1]
        arr.pop()
        self.min_heapify(0)
        return res
    
    """
    Decrease Key
    """
    def decrease_key(self,i,x):
        arr = self.arr
        arr[i] = x
        while i!=0 and arr[self.parent(i)]>arr[i]:
            p = self.parent(i)
            arr[i],arr[p] = arr[p],arr[i]
            i = p
    """
    Delete Operation
    """
    def delete_key(self,i):
        n = len(self.arr)
        if i >= n:
            return
        else:
            self.decrease_key(i,-math.inf)
            self.extract_min()
    
    """
    Build Heap
        - Time Complexity: O(n)
    """
    def build_heap(self,l=[]):
        self.arr = l
        i  = (len(l)-2)//2
        while i>=0:
            self.min_heapify(i)
            i= i-1
"""
Implementation of Min-Heap with heapq
"""
import heapq
pq = [5,20,1,30,4]
heapq.heapify(pq)
print("After Heapify List: ",pq)
heapq.heappush(pq,3)
print("After inserting element in heap: ",pq)
print("Deleting element from the Heap: ",heapq.heappop(pq))
print("Largest element from the heap: ",heapq.nlargest(2,pq))
print("Smallest element from the heap: ",heapq.nsmallest(2,pq))