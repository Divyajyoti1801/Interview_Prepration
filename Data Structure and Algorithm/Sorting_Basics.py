
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