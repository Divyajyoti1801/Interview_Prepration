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