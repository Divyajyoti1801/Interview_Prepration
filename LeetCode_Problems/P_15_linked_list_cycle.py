"""
Problem - 15 : Linked List Cycle

Problem Statement : 
    - Given head, the head of a linked list, determine if the linked list has a cycle in it.

    - There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    - Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
"""

class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

def has_cycle(head):
    dict = {}
    while head:
        if head in dict:
            return True
        else:
            dict[head] = True
        head = head.next
    return False

head= Node(3)
head.next= Node(2) # type: ignore
head.next.next= Node(0) # type: ignore
head.next.next.next= Node(-4)# type: ignore
head.next.next.next.next = head.next # type: ignore
print("Linked List has Cycle: ",has_cycle(head))