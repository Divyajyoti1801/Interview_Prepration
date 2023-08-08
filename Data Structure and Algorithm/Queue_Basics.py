"""
Queue Data Structure
    - Also known as FIFO Data Structure (First In First Out)
    - Operations:
        = enqueue(x)
        = dequeue()
        = getFront()
        = getRear()
        = size()
        = isEmpty()
    
    Application of Queue:
        - Single Resource and multiple consumers
        - Synchronization b/w slow and fast
        - In Operating Systems (Semaphores, FCFS Scheduling, Spooling, buffers, for devices like keyboard)
        - In Computer Networks (Routers/Switches and Mail Queues)
        - Variations : Deque, Priority Queue and Doubly Ended Priority Queue
"""

"""
Queue Implementation
    - Using List
    - Using Collections.dequeue (Thread Safe Env)
    - Using queue.Queue
    - Own Implementation: Circular Structure gives efficient results
"""
q1 = [] # Insertion must be from the end
q1.append(10)
q1.append(20)
q1.append(30)
print("Initial Queue: ",q1)
print(q1.pop(0)) # Deletion must be from the front
q1.append(40)
print(q1.pop(0))
print("Length of the Queue: ",len(q1))
print(q1[0])
print(q1[-1])

print()
from collections import deque
q2 = deque()
q2.append(10)
q2.append(20)
q2.append(30)
print("Queue made from deque: ",q2)
print(q2.popleft())
q2.append(40)
print(q2.popleft())
print("Length of the queue: ",len(q2))
print(q2[0])
print(q2[-1])

"""
Implementation of Queue using Array
"""
class Queue:
    def __init__(self,c):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c
    
    def queueEnqueue(self,data):
        if (self.capacity == self.rear):
            print("\n Queue is Full")
        else:
            self.queue.append(data)
            self.rear+=1
    
    def queueDequeue(self):
        if(self.front == self.rear):
            print("Queue is empty")
        else:
            x = self.queue.pop(0)
            self.rear -=1
    
    def queueDisplay(self):
        if(self.front == self.rear):
            print("\nQueue is Empty")
        
        for i in self.queue:
            print(i,"<--",end="")
    
    def queueFront(self):
        if (self.front == self.rear):
            print("\nQueue is empty")
        print("\nFront Element is: ",self.queue[self.front])
print("Self Created Queue Data Structure: ")
q3 = Queue(4)
q3.queueDisplay()
q3.queueEnqueue(20)
q3.queueEnqueue(30)
q3.queueEnqueue(40)
q3.queueEnqueue(50)
q3.queueDisplay()
q3.queueEnqueue(60)
q3.queueDisplay()
q3.queueDequeue()
q3.queueDequeue()
print("\n\nafter two node deletion\n")
q3.queueDisplay()
q3.queueFront()

"""
Implementation of Queue using Linked List
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    
    def size(self):
        return self.sz
    
    def isEmpty(self):
        return self.sz == 0
    
    def getFront(self):
        return self.front.data # type: ignore
    def getRear(self):
        return self.rear.data # type: ignore
    
    def enque(self,x):
        temp = Node(x)
        if self.rear ==None:
            self.front = temp
        else:
            self.rear.next = temp # type: ignore
        self.rear = temp
        self.sz+=1
    
    def deque(self):
        if self.front == None:
            return None
        else:
            res = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.sz -= 1
            return res

q4 = LinkedQueue()
q4.enque(10)
print(q4.getFront(), q4.getRear())
q4.enque(20)
print(q4.getFront(), q4.getRear())
q4.enque(30)
print(q4.getFront(), q4.getRear())
q4.deque()
print(q4.getFront(), q4.getRear())
            
