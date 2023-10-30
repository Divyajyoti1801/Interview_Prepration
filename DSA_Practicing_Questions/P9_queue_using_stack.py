"""
Problem - 9 : Queue using stack

Problem Statement: 
    - Implement a Queue using two stack s1 and s2.
    - Time Complexity : enqueue:O(1); dequeue:O(n) 
"""
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enque(self,X):
        # Add Element on the last index of the list
        self.s1.append(X)
        return
    def dequeue(self):
        # First store the value the del the value
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

print("Implementation of Queue using two stack: ")
input_queue= Queue()
input_queue.enque(2)
input_queue.enque(3)
print(input_queue.dequeue(),end=" ")
input_queue.enque(4)
print(input_queue.dequeue())