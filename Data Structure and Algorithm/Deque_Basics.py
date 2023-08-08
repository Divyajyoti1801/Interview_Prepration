"""
DEQUE Data Structure
    - Have front and rear side which can be used for insertion and deletion
    - Operations:
        = getFront()
        = getRear()
        = isFull()
        = isEmpty()
        = size()
    
    Applications of Deque:
        - A deque can be used as both stack and Queue
        - Maintaining history of actions
        - A Steal Process Scheduling Algorithms
        - Implementing a Priority Queue with two types of priorities
        - Maximum and Minimum of all sub arrays of size k in an array
    
    Time Complexities & Internal Working:
        - Underneath it uses doubly linked list 
        - O(1): append(),appendleft(),pop(),popleft()
        - O(n): d[i],count(),insert()
        - O(abs(r)): rotate(r)
        - O(len(l)): extend(),extendleft()

"""

"""
Implementation of Deque
"""
from collections import deque

d = deque()
d.append(10)
print("Insertion of Element: ",d)
d.append(20)
print("Insertion of Element: ",d)
d.append(30)
print("Insertion of Element: ",d)
d.appendleft(40)
print("Insertion of element from front: ",d)
print("Removing Element from right: ",d.pop())
print("Removing Element from left: ",d.popleft())
print("The final lis: ",d)

d2 = deque([10,20,30,40])
print("Main Operational Deque: ",d2)
d2.insert(2,10) # Positional insertion
print("Number of element present equal to 10: ",d2.count(10))
d2.remove(10)
print("Deque after deleting the element: ",d2)
d2.extend([50,60])
print("Extend deque from right: ",d2)
d2.extendleft([15,25])
print("Extend deque from left: ",d2)
d2.rotate(2)
print("Rotate deque with two elements: ",d2)
d2.rotate(-2)
print("Rotate deque with two elements anti-clockwise: ",d2)
d2.reverse()
print("Reverse of the deque: ",d2)
print(d2[2])
d2[2] = 100 # Deque is mutable by nature
print(d2)
print("First Element of deque: ",d2[0])
print("Last Element of deque: ",d2[-1])

"""
Doubly Linked List Implementation Of Deque
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self,c):
        self.front = None
        self.rear = None
        self.sz = 0
    
    def size(self):
        return self.sz
    
    def isEmpty(self):
        return self.sz == 0
    
    def insertRear(self,x):
        temp = Node(x)
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp # type: ignore
            temp.prev = self.rear # type: ignore
        self.rear = temp
        self.sz+=1

    def deletfront(self):
        if self.front == None:
            return None
        else:
            res = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            self.sz -= 1
            return res
    
    def getFront(self):
        if self.front:
            return self.front.data
    
    def getRear(self):
        if self.rear:
            return self.rear.data

d3 = Deque(3)
print(d3.isEmpty())
d3.insertRear(10)
print(d3.getFront(),d3.getRear())
d3.insertRear(20)
print(d3.getFront(),d3.getRear())
d3.insertRear(30)
print(d3.getFront(),d3.getRear())
d3.deletfront()
print(d3.getFront(),d3.getRear())

"""
List Implementation Of Deque
"""
class ListDeque:
    def __init__(self,c):
        self.l = [None] * c
        self.cap = c
        self.size = 0
        self.front = 0
    
    def deleteFront(self):
        if self.size == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front+1) % self.cap
            self.size -= 1
            return res
    
    def insertFront(self,x):
        if self.size == self.cap:
            return
        
        else:
            self.front = (self.front -1) % self.cap
            self.l[self.front] = x
            self.size +=1
    
    def insertRear(self,x):
        if self.size == self.cap:
            return
        new_rear = (self.front + self.size) % self.cap
        self.l[new_rear] = x
        self.size += 1
    
    def deleteRear(self):
        sz = self.size
        if sz == 0:
            return None
        else:
            rear = (self.front + sz -1) % self.cap
            self.size = sz - 1
            return self.l[rear]
    
    def frontEle(self):
        return self.l[self.front]
    
    def rearEle(self):
        rear = (self.front + self.size -1) % self.cap
        return self.l[rear]
print()
d4 = ListDeque(4)
d4.insertFront(10)
print(d4.frontEle(),d4.rearEle())
d4.insertFront(20)
print(d4.frontEle(),d4.rearEle())
d4.insertFront(30)
print(d4.frontEle(),d4.rearEle())
d4.deleteRear()
print(d4.frontEle(),d4.rearEle())
d4.insertRear(40)
print(d4.frontEle(),d4.rearEle())
d4.deleteRear()
print(d4.frontEle(),d4.rearEle())