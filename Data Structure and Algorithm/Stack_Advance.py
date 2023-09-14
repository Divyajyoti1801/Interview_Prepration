"""
STACK ADVANCE CONCEPTS AND QUESTIONS
"""

"""
Concept - 1: Implement two stacks in an Array 

    Brute Force:
        - We divide the array from middle
            = We use first half for stack_1 and second half for stack_2
        - Inefficient use of space
            = if we add 5 items to stack_1, and no items to stack_2, then we cannot add more items to stack_1 even if we have space in the array
    
    Efficient Solution: 
        - Begin both stacks from the two corners of the array
        - Now  we can insert items in any stack as long as we have space.
"""
class TwoStacks:
    def __init__(self,n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size
    
    def push_1(self,x):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
            return True
        return False
    
    def push_2(self,x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
            return True
        return False
    
    def pop_1(self):
        if self.top1>=0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        return None
    
    def pop_2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        return None
    
    def size_1(self):
        return self.top1 + 1
    
    def size_2(self):
        return self.size - self.top2
print("Concept of Two Stacks in an Array: ")
two_stacks = TwoStacks(5)
two_stacks.push_1(10)
two_stacks.push_2(20)
print("First Element of Stack 1: ",two_stacks.pop_1())
print()

"""
Concept - 2 : Implement K stacks in an Array
"""
class KStacks:
    def __init__(self,n,k):
        self.cap = n
        self.k = k
        self.arr = [None] * n
        self.top = [-1] * k
        self.next = [i+1 for i in range(n)]
        self.next[n-1] = -1
        self.free_top = 0
    
    def push(self,sn,x):
        i = self.free_top
        self.free_top = self.next[self.free_top]
        self.arr[i] = x
        self.next[i] = self.top[sn]
        self.top[sn] = i
    
    def pop(self,sn):
        prev_top = self.top[sn]
        self.top[sn] = self.next[prev_top]
        self.next[prev_top] = self.free_top
        self.free_top = prev_top
        return self.arr[prev_top]
    
    def isEmpty(self,sn):
        return self.top[sn] == -1


"""
Problem Statement: Stock span problem
"""
def stock_span_problem_1(arr):
    res = []
    for i in range(len(arr)):
        span = 1
        j = i-1
        while j>=0 and arr[i] >= arr[j]:
            span += 1
            j -= 1
        res.append(span)
    return res
print("Stock span problem (Naive) O(n^2): ",stock_span_problem_1([18,12,13,14]))
"""
Observation: 
=> If there is a greatest element on left side;
Span = (Index of Current Element) - (Index of Closest Greater Element on Left Side)
=> Otherwise;
Span = Index of current element + 1


"""
def stock_span_problem_2(arr):
    st = []
    res = []
    st.append(0)
    res.append(1)
    for i in range(1,len(arr)):
        while len(st)>=0 and arr[st[-1]]<=arr[i]:
            st.pop()
        span = (i+1) if len(st) == 0 else i-st[-1]
        res.append(span)
        st.append(i)
    return res
print("Stock span problem (Efficient): ",stock_span_problem_2([60,10,20,15,35,50]))
print()

"""
Problem Statement: Previous Greater element
"""
def previous_greater_element_1(arr):
    res = []
    for i in range(len(arr)):
        pg = -1
        for j in range(i-1,-1,-1):
            if arr[j]>arr[i]:
                pg = arr[j]
                break
        res.append(pg)
    return res
print("Previous greater element (Naive) O(n^2): ",previous_greater_element_1([20,30,10,5,15]))
def previous_greater_element_2(arr):
    res = []
    st = []
    for i in range(len(arr)):
        while len(st)>0 and st[-1]<=arr[i]:
            st.pop()
        pg = -1 if len(st) == 0 else st[-1]
        res.append(pg)
        st.append(arr[i])
    return res
print("Previous greater element (Efficient) O(n): ",previous_greater_element_2([20,30,10,5,15]))
print()

"""
Problem Statement : Next Greater Element
"""
def next_greater_element_1(arr):
    res = []
    for i in range(len(arr)):
        ng = -1
        for j in range(i+1,len(arr)):
            if arr[j] > arr[i]:
                ng = arr[j]
                break
        res.append(ng)
    return res
print("Next greater element (Naive) O(n^2): ",next_greater_element_1([5,15,10,8,6,12,7]))
def next_greater_element_2(arr):
    res = [None] * len(arr)
    st = []
    for i in range(len(arr)-1,-1,-1):
        while len(st)>0 and st[-1]<=arr[i]:
            st.pop()
        res[i] = -1 if len(st) == 0 else st[-1] # type: ignore
        st.append(arr[i])
    return res
print("Next greater element (Efficient) O(n): ",next_greater_element_2([5,15,10,8,6,12,7]))

"""
Problem Statement: Largest Rectangular area in a histogram
"""
def largest_rectangular_area_histogram_1(arr):
    res = 0
    for i in range(len(arr)):
        curr = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>=arr[i]:
                curr+=arr[i]
            else:
                break
        for j in range(i+1,len(arr)):
            if arr[j] >= arr[i]:
                curr+=arr[i]
            else:
                break
        res = max(res,curr)
    return res
print("Largest area of rectangular histogram: ",largest_rectangular_area_histogram_1([6,2,5,4,1,5,6]))
"""
Efficient Solution:
    - Initialize : res = 0
    - Find Pervious smaller element for every element
    - Find Next smaller element for every element
    - Do following for every element arr[i]
        curr = arr[i]
        curr += (i - ps[i] - 1) * arr[i]
        curr += (ns[i] - i - 1) * arr[i]
        res = max(res,curr)
    - return res
"""
def largest_rectangular_area_histogram_2(arr):
    res = 0
    st = []
    for i in range(len(arr)):
        while st and arr[st[-1]] >= arr[i]:
            tp = st[-1]
            st.pop()
            curr_width = (i-st[-1]-1) if st else i
            res = max(res,curr_width * arr[tp])
        st.append(i)
    
    while st:
        tp = st[-1]
        st.pop()
        curr_width = (len(arr) - st[-1] -1 ) if st else len(arr)
        res = max(res,curr_width*arr[tp])
    return res
print("Largest area of rectangular histogram (Efficient): ",largest_rectangular_area_histogram_2([6,2,5,4,1,5,6]))
