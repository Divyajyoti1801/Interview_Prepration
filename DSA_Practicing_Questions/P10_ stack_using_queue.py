"""
Problem - 10 : STACK USING QUEUE

Problem Statement : 
    - Implement a Stack using two queues q1 and q2
"""

from collections import deque

class Stack:
    def __init__(self):
        self.q1= deque()
        self.q2= deque()
    def push(self,X):
        self.q2.append(X)
        while self.q1:
            self.q2.append(self.q1.popleft())
            self.q1,self.q2 = self.q2,self.q1
    def pop(self):
        if self.q1:
            return self.q1.popleft()
        else:
            return -1

print("Implementation of stack is queue: ")
input_stack = Stack()
input_stack.push(2)
print(input_stack.pop())
print(input_stack.pop())
input_stack.push(3)
