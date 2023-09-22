"""
QUEUE AND DEQUE ADVANCE CONCEPTS AND PROBLEMS
"""

"""
Queue Implementation Using Circular List
"""
class Queue_1:
    def __init__(self,c):
        self.l = [None]*c
        self.cap = c
        self.size = 0
        self.front = 0
    
    def get_front(self):
        if self.size == 0:
            return None
        else:
            return self.l[self.front]
    
    def get_rear(self):
        if self.size == 0:
            return None
        else:
            rear = (self.front + self.size - 1) % self.cap
            return self.l[rear]
    
    def enque(self,x):
        if self.size == self.cap:
            return
        else:
            rear = (self.front + self.size - 1) % self.cap
            rear = (rear + 1) % self.cap
            self.l[rear] = x
            self.size = self.size + 1
    
    def deque(self):
        if self.size == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front + 1) % self.cap
            self.size = self.size - 1
            return res
print("Queue implementation using Circular List: ")
queue_1 = Queue_1(4)
queue_1.enque(10)
print(queue_1.get_front(),queue_1.get_rear())
queue_1.enque(20)
print(queue_1.get_front(),queue_1.get_rear())
queue_1.enque(30)
print(queue_1.get_front(),queue_1.get_rear())
queue_1.enque(40)
print(queue_1.get_front(),queue_1.get_rear())
queue_1.deque()
print(queue_1.get_front(),queue_1.get_rear())
queue_1.deque()
print(queue_1.get_front(),queue_1.get_rear())
queue_1.enque(50)
print(queue_1.get_front(),queue_1.get_rear())
print()

"""
Implementation stack using queue
    Basic Solution:
        q1: to keep the actual items
        q2: to be used as an auxiliary queue
        push(x):
            - Move everything from q1 to q2
            - Enqueue x to q1
            - Move everything back from q2 to q1
        pop():
            - Remove front of q1
        top():
            - Return front of q1
        size():
            - Return size of q1
    
    Efficient solution:
        q1: to keep the actual items
        q2: to be used as an auxiliary queue
        push(x):
            - Enqueue x to q2
            - Move everything from q1 to q2
            - Swap the variables q1 and q2
        pop():
            - Remove front of q1
        top():
            - Return front of q1
        size():
            - Return size of q1

"""
from collections import deque
class Stack_1:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self,x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2 = self.q2,self.q1
    def pop(self):
        if self.q1:
            self.q1.popleft()
    
    def top(self):
        if self.q1:
            return self.q1[0]
        else:
            return None
    
    def size(self):
        return len(self.q1)
print("Stack implementation with Dequeue")
stack_1 = Stack_1()
stack_1.push(3)
stack_1.push(4)
stack_1.push(5)
stack_1.push(6)
print("Size of the stack: ",stack_1.size())
print("Top of the Stack: ",stack_1.top())
stack_1.pop()
print("Now top of the Stack: ",stack_1.top())
print()

"""
Problem Statement: Reverse a Queue
    Iterative Solution: 
        - Create an empty stack
        - Move all items of q to stack
        - Move all items back to the q
"""
def reverse_of_queue_itr(q = deque()):
    st = []
    while q:
        st.append(q.popleft())
    while st:
        q.append(st.pop())
    return q
queue_2 = deque()
queue_2.append(20) 
queue_2.append(30) 
queue_2.append(10) 
print("Reverse of the queue (Iterative): ",reverse_of_queue_itr(queue_2))
def reverse_of_queue_recur(q = deque()):
    if len(q) == 0:
        return
    x = q.popleft()
    reverse_of_queue_recur(q)
    q.append(x)
    return q
print("Reverse of the queue (Recursion): ",reverse_of_queue_recur(queue_2))
print()

"""
Problem Statement: Generate first n numbers with given digits.

    Naive Solution:
        - Traverse through all natural numbers while we have not generate the numbers
        - For every traversed number, check if it has 5 and 6 only. if yes, print the number and increment the count.
    
    Efficient Solution:
        - Create an empty queue, q
        - Add 5 and 6 to q
        - Run a loop n times
            = Take out an item from q
            = Print the item
            = Append 5 to the item and add the new number to q
            = Append 6 to the items and add the new number to q
"""
def generate_first_n_numbers(n):
    q = deque()
    q.append("5")
    q.append("6")
    for i in range(n):
        curr = q.popleft()
        print(curr,end= " ")
        q.append(curr + "5")
        q.append(curr + "6")
    print()
print("Generate first n numbers with the given digits: ")
generate_first_n_numbers(3)
def generate_first_n_numbers_2(n):
    q = deque()
    q.append("5")
    q.append("6")
    i = 0
    while (i + len(q)) < n:
        curr = q.popleft()
        print(curr,end = " ")
        q.append(curr+"5")
        q.append(curr+"6")
        i+=1
    while i<n:
        print(q.popleft(),end=" ")
        i+=1
    print()
print("Generate first n numbers with the given digits (Better Implementation): ")
generate_first_n_numbers_2(3)
print()

"""
Problem Statement: Design a data structure with max/min operations
"""
class MaxMinStruct:
    def __init__(self):
        self.dq = deque()
    
    def insertMin(self,x):
        self.dq.appendleft(x)
    
    def insertMax(self,x):
        self.dq.append(x)
    
    def extractMin(self):
        return self.dq.popleft()
    
    def extractMax(self):
        return self.dq.pop()
    
    def getMin(self):
        return self.dq[0]
    
    def getMax(self):
        return self.dq[-1]
print("Design a data structure with max/min operations: ")
queue_3 = MaxMinStruct()
queue_3.insertMin(10)
queue_3.insertMin(5)
queue_3.insertMax(20)
queue_3.insertMin(3)
print(queue_3.extractMin())
print(queue_3.extractMax())
print(queue_3.getMin())
print(queue_3.getMax())
print()

"""
Problem Statement: Maximum in all subArrays of size k
"""
def max_in_all_subarray_1(arr,k):
    result = []
    for i in range(len(arr)-k+1):
        res = arr[i]
        for j in range(i+1,i+k):
            res = max(res,arr[j])
        result.append(res)
    return result
print("Maximum of all subarrays of size k(Naive): ",max_in_all_subarray_1([10,8,5,12,15,7,6],3))

def max_in_all_subarray_2(arr,k):
    dq = deque()
    for i in range(k):
        while dq and arr[i]>=arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    print(arr[dq[0]],end=" ")
    for i in range(k,len(arr)):
        while dq and dq[0]<=i-k:
            dq.popleft()
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
        print(arr[dq[0]],end=" ")
    print()
print("Maximum of all subarrays of size k (Efficient): ")
max_in_all_subarray_2([20,40,30,35,60],3)
print()
"""
Problem Statement: Consider an arrangement where n petrol pumps are arranged in a circular manner. We need to find the first petrol pump from where we can visit all petrol pumps and come back to the petrol pump without ever going out of the petrol.
I/P: Petrol = [4,8,7,4]
O/P: distance = [6,5,3,5]

    Better Solution:
        - keep adding items to the end of deque while curr_petrol is greater than equal to 0
        - Keep removing items from the front of degree while curr_petrol is negative.
    
    Efficient Solution:
        - if curr_petrol becomes negative at pi, then none of the petrol pumps from p0 to pi can be solution
            p0, p1, ....pi-1, pi, pi+1,....pn-1
        - Let pi be the first petrol pump where current petrol becomes negative, then
            curr_petrol = Sum(i,j=0)(petrol[j] - dist[j])
"""
def circular_tour_1(petrol=[],distance=[]):
    n = len(petrol)
    for start in range(n):
        curr_petrol = 0
        end = start
        while True:
            curr_petrol+= (petrol[end]-distance[end])
            if curr_petrol < 0:
                break
            end = (end+1)%n
            if end == start:
                return start+1
    return 1
print("Circular tour (Naive): ",circular_tour_1([4,8,7,4],[6,5,3,5]))
def circular_tour_2(petrol=[],distance=[]):
    start = 0
    curr_pet = 0
    prev_pet = 0
    for i in range(len(petrol)):
        curr_pet+=(petrol[i]-distance[i])
        if curr_pet<0:
            start = i+1
            prev_pet += curr_pet
            curr_pet = 0
    return (start + 1) if((curr_pet+prev_pet)>=0) else -1
print("Circular tour (Efficient): ",circular_tour_2([4,8,7,4],[6,5,3,5]))
