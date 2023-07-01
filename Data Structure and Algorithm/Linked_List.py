"""
Linked List
    - A Linked List is a linear data structure, in which elements are not stored at contiguous memory locations. The element in a linked list are linked using pointers.

    HEAD --> Data-Next --> Data-Next --> Data-Next

Linked List Operation and Time Complexity:
    - Insertion at end of the linked list O(1)
    - Deletion at end of the linked list O(n)
    - Insertion at rear of the linked list O(1)
    - Deletion at rear of the linked list O(1)
    - Insertion at any other position in linked list O(n).
    - Removing at any other position in linked list O(n)
    - Traversing in linked list is also O(n)

Structure of Node in Linked List
    
    NODE = {
        "value":4,
        "next": None
    }   
"""

# Code for creating Node
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

# Initialization of Linked List
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1;

# Print Linked List Element
def print_list(self):
    temp=self.head
    while temp is not None:
        print(temp.value)
        temp=temp.next
    
my_linked_list=LinkedList(4)

print(my_linked_list.head.value)


    
        



