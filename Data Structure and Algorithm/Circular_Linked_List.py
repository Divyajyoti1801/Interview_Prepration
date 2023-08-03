"""
Data Structure: Circular Linked List
""" 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
head = Node(10)
head.next = Node(20) # type: ignore
head.next.next = Node(30) # type: ignore
head.next.next.next = Node(40) # type: ignore
head.next.next.next.next = head # type: ignore

"""
Advantages and Disadvantages of Circular Linked List

HEAD => 10 -> 5 -> 20 -> 15 -> HEAD

Advantages:
    - We can traverse the whole list from any node
    - Implementation of algorithm like round robin
    - We can insert at the beginning and end by just maintaining one tail reference/pointer

Disadvantages:
    - implementation of basic operations becomes complex
"""

def traversal_linked_list(head):
    if head == None:
        print("Linked List is Empty")
    curr = head
    while curr.next!=head:
        print(curr.data,end = " ")
        curr = curr.next
    print(curr.data)
print("Main Circular Linked List: ")
traversal_linked_list(head)
print("\n")

"""
Problem Statement: Insert at the beginning of the linked list
I/P: 10 -> 20 -> 30 x = 15 
O/P: 15 -> 10 -> 20 -> 30
"""
def insert_at_beginning(head,x):
    temp = Node(x)
    if head==None:
        head = temp
        return head
    curr = head
    while curr.next!=head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    head = temp
    return head

head = insert_at_beginning(head,15)
traversal_linked_list(head)
print()
def optimized_insert_at_beginning(head,x):
    temp = Node(x)
    if head == None:
        head = temp
        return head
    temp.next = head.next
    head.next = temp
    head.data,temp.data = temp.data, head.data
    return head
head = optimized_insert_at_beginning(head,25)
traversal_linked_list(head)
print()

"""
Problem Statement: Insert at End of the circular linked list
I/P: 10 -> 20 -> 30 x = 15
O/P: 10 -> 20 -> 30 -> 15
"""
def insert_at_end(head,x):
    temp = Node(x)
    if head == None:
        head = temp
        temp.next = head # type: ignore
        return head
    temp.next = head.next
    head.next = temp
    temp.data,head.data = head.data,temp.data
    return temp

head = insert_at_end(head,75)
traversal_linked_list(head)
print()

"""
Problem Statement: Delete head of circular linked list
I/P: 10 -> 20 -> 30
O/P: 20 -> 30
"""
def deletion_of_head(head):
    if head == None:
        return head
    if head.next == head:
        return None
    head.data = head.next.data
    head.next = head.next.next
    return head
head = deletion_of_head(head)
traversal_linked_list(head)
print()

"""
Problem Statement: Delete the Kth Node of Circular Linked list
I/P: 10 -> 20 -> 30 k = 2
O/P: 10 -> 30
"""
def delete_kth_Node(head,K):
    if head == None:
        return Node
    if K == 1:
        return deletion_of_head(head)
    curr = head
    for i in range(K-2):
        curr = curr.next
    curr.next = curr.next.next
    return head
head = delete_kth_Node(head,2)
traversal_linked_list(head)
print()