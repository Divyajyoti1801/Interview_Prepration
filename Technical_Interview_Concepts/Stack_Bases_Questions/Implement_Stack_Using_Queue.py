"""
IMPLEMENT STACK USING QUEUE

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]
"""
from collections import deque


class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

    def pop(self):
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self):
        return self.q[-1]

    def empty(self):
        return len(self.q) == 0


s = Stack()
s.push(1)
s.push(2)
print(s.top())
print(s.empty())
print(s.pop())
