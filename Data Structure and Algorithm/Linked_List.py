"""
LINKED LIST

    - Introduction
        = Either size is fixed and pre-allocated (in both fixed and variable sized array), OR the worst case insertion at the end is theta(n)
        = Insertion in the middle (or beginning) is costly.
        = Deletion from the middle (or beginning) is costly.
        = Implementation of data structure like queue and deque is complex with arrays
    
    - Problems with Array Implementation
        = Implementation of Round Robin scheduling.
        = Given a sequence of items. Whenever we see an item x in the sequence, we need to replace it with 5 instances of another item  y.
        = We have multiple sorted sequences and we need them frequently.
    
    - Linked List in Python:
        = The idea is to drop the contiguous memory requirement so that insert/delete can happen faster.
    10-_ --> 5-_ --> 20-_ --> 25-None
"""

"""
Simple Linked List Implementation
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
#creating first node of the Linked List
temp1= Node(10)
temp2= Node(20)        
temp3= Node(30)
temp1.link=temp2  # type: ignore
temp2.link=temp3 # type: ignore
head = temp1 #initialization of head
print("Head of the linked list: ",head.data)
print("Node-2 : ",head.link.data) # type: ignore
print("Node-3: ",head.link.link.data) # type: ignore

"""
Application of Linked List Data Structure:
    - Worst case insertion at the end and beginning are theta(1)
    - Worst case deletion in the middle are theta(1) if we have references to the previous node.
    - Round Robin implementation
    - Merging two sorted linked lists is faster than arrays.
    - Implementation of simple memory manager where we need to link free blocks.
    - Easier implementation of Queue and Deque data structures.
"""
"""
Problem Statement: traversing a linked list in python
I/P: 10->20->30->40->None
O/P: 10 20 30 40
"""
class Node2:
    def __init__(self,data):
        self.data=data
        self.link= None

# Driver Code
head= Node(10)
head.link=Node(20) # type: ignore
head.link.link=Node(15) # type: ignore
head.link.link.link=Node(30) # type: ignore

def traversing_of_linkedList(head):
    if head==None:
        print("List is empty")
    temp = head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.link
# traversing_of_linkedList(head)    
# Time Complexity : O(n)

"""
Problem Statement: Search element in the linked list
I/P: 10->5->20->15->None S = 20
O/P: 3 
"""
def search_the_element(head,S):
    if head==None:
        return -1
    temp = head
    count=1
    while temp!=None:
        if(temp.data == S):
            return count
        count+=1
        temp = temp.link
    return -1
print("Search the element: ",search_the_element(head,5))

"""
Problem Statement: Insert at the beginning of the linked List 
I/P: 10->20->30->None data = 5
O/P: 5->10->20->30->None
"""
def insert_at_beginning(head,data):
    if head==None:
        return -1
    temp_node=Node(data)
    temp_node.link=head
    return temp_node
# head = insert_at_beginning(head,55)
# traversing_of_linkedList(head)

"""
Problem Statement: Insert at the end of the linked list
I/P : 10->20->30->None data=35
O/P : 10->20->30->35->None
"""
def insert_at_end(head,data):
    temp_node=Node(data)
    if head == None:
        return temp_node
    temp=head
    while(temp.link!=None):
        temp=temp.link
    temp.link = temp_node # type: ignore
    return head

# head=insert_at_end(head,75)
# traversing_of_linkedList(head)

"""
Problem Statement: insert element at a given position.
I/P: 10->30->50->70 pos=2 data=20
O/P: 10->20->30->50->70
"""
def insert_at_position(head,pos,data):
    temp_node=Node(data)
    if head == None:
        return None
    
    if pos == 1:
        temp_node.link=head
        head = temp_node
        return head
    temp = head
    for i in range(pos-2):
        temp=temp.link
        if temp == None:
            return head
    temp_node.link=temp.link
    temp.link = temp_node
    return head

print()
print("Major Linked List")
traversing_of_linkedList(head)
print()
head=insert_at_position(head,2,35)
traversing_of_linkedList(head)
print()

"""
Problem Statement : delete the first node of the linked  list
I/P: 10->20->30->40
O/P: 20->30->40
"""
def delete_first_node(head):
    if head == None:
        return None
    head=head.link
    return head
print()
head=delete_first_node(head)
traversing_of_linkedList(head)

"""
Problem Statement: delete the last node of the linked list
I/P: 10->20->30->40->None
O/P: 10->20->30->None
"""
def delete_last_node(head):
    if head==None:
        return None
    temp = head
    prev=Node(-1)
    while temp.link!=None:
        prev=temp
        temp=temp.link
    prev.link=None
    return head
print()
head=delete_last_node(head)
traversing_of_linkedList(head)

"""
Problem Statement : delete a node with only pointer given to it
I/P: 10->20->30->40->25->NUll
O/P: 10->20->40->25->Null
"""

def delete_node_pointer(head,node):
    if head == None:
        return None
    temp=node.link
    node.link = temp.data
    node.link=temp.link
    return head

