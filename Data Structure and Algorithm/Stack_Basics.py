"""
STACK DATA STRUCTURE
    - Insert Operation: Push
    - Removal Operation: Pop
    - Only Top side is open for insertion and deletion

    Stack operations:
        - isEmpty() : Return true if stack is empty else false
        - push(): Inserts an item to the top of the stack
        - pop(): Removes an item from the top
        - peek(): Returns the top item
        - size(): Returns the size of stack
    
    Two Corner Condition: 
        - Underflow: When pop() or peek() called on an empty stack
        - Overflow: when push called on a full stack
    
    Stack Implementation in Python:
        - Using List
        - Using collections.deque
        - Using queue.LIFOQueue
        - Using your own implementation
"""
"""
Method 1: Using List
"""
stack_1=[]
stack_1.append(10)
stack_1.append(20)
stack_1.append(30)
print(stack_1.pop())
top = stack_1[-1]
print("Top Element from the Stack: ",top)
size = len(stack_1)
print("Length of the stack: ",size)

"""
Method 2: Using Deque
"""
from collections import deque
stack_2 = deque()
stack_2.append(10)
stack_2.append(20)
stack_2.append(30)
stack_2.append(40)
print(stack_2)
print(stack_2.pop())
top = stack_2[-1]
print(top)
size = len(stack_2)
print(size)

"""
Method 3: Linked List implementation of the Stack
"""
import math
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.sz = 0

    def push(self,data):
        temp = Node(data)
        temp.next = self.head # type: ignore
        self.head = temp
        self.sz +=1
    
    def display(self):
        res = []
        if self.sz <= 0:
            return []
        curr = self.head
        while curr!=None:
            res.append(curr.data)
            curr = curr.next
        return res[::-1]

    
    def pop(self):
        if self.head==None:
            return math.inf
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.sz-=1
        return temp.data
    
    def size(self):
        return self.sz
    
    def peek(self):
        if self.head==None:
            return math.inf
        return self.head.data

stack_3 = Stack()
stack_3.push(10)
stack_3.push(20)
stack_3.push(30)
print(stack_3.display())
print(stack_3.pop())
print(stack_3.peek())
print(stack_3.size())
print(stack_3.display())

"""
Applications of Stack:
    - Function calls (Basically Recursion)
    - Balanced Parenthesis 
    - Reversing Items
    - Infix to Postfix / Prefix
    - Evaluation of Postfix / Prefix
    - Stock Span Problem
    - Undo / Redo or Forward / Backward
"""

"""
Problem Statement: Check for Balanced Parenthesis
I/P: S = "([])"
O/P: Yes
"""
def isMatching(a,b):
    if (a == '(' and b == ')') or  (a == '{' and b == '}') or (a == '[' and b == ']'):
        return True
    else:
        return False

def isBalanced(exper):
    stack = []
    for x in exper:
        if x in ('(','{','['):
            stack.append(x)
        else:
            if not stack:
                return False
            elif isMatching(stack[-1],x) == False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
a = "{{[]{{(())}}}}"
print(isBalanced(a))