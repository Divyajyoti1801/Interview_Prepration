"""
Data Structure: Doubly Linked List
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
head.next= temp1 # type: ignore
temp1.prev = head # type: ignore
temp1.next = temp2 # type: ignore
temp2.prev = temp1 # type: ignore

"""
Advantages and Disadvantages of Doubly Linked List

Advantages:
    - Can be traversed in both directions
    - A given delete a node in O(1) time with given reference / pointer to it.
    - Insert / Delete before given node
    - Insert / Delete from both end in O(1) time by maintaining tail

Disadvantages:
    - Extra space for prev
    - Code becomes more complex
"""
def traverse_of_list(head):
    if head == None:
        print("List doesn't Exists")
    curr = head
    while curr:
        print(curr.data,end=" ")
        curr = curr.next
print("Major Operational List: ")
traverse_of_list(head)
print()


"""
Problem Statement: Insert at the beginning of Doubly Linked list
I/P: 10 15 20
O/P: 5 10 15 20
"""
def insert_at_beg(head,data):
    temp  = Node(data)
    if head == None:
        head = temp
        return head
    temp.next = head
    head.prev = temp
    head = temp
    return temp
print("Insertion at the beginning of the List: ")
head = insert_at_beg(head,5)
traverse_of_list(head)
print()

"""
Problem Statement: Insert at the end of the list
I/P: 10 20 30  x = 40
O/P: 10 20 30 40 
"""
def insert_at_end(head,data):
    temp = Node(data)
    if head == None:
        head = temp
        return head
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = temp
    temp.prev = curr
    return head
print("Insert at the end of the list: ")
head = insert_at_end(head,40)
traverse_of_list(head)
print()

"""
Problem Statement: Delete head of a Doubly Linked List
I/P: 10 20 30
O/P: 20 30
"""
def delete_from_head(head):
    if head == None:
        return head
    temp = head
    head.next.prev = None
    head = temp.next
    temp.next = None
    return head
print("Delete at the  head of linked list: ")
head = delete_from_head(head)
traverse_of_list(head)
print()

"""
Problem Statement: Delete last node from doubly linked list.
I/P: 10 20 30 
O/P: 10 20
"""
def delete_from_tail(head):
    if head==None:
        return head
    curr = head
    while curr.next:
        curr = curr.next
    curr.prev.next = None
    curr.prev = None
    return head 
print("Delete from the tail: ")
head = delete_from_tail(head)
traverse_of_list(head)
print()

"""
Problem Statement: Reverse of a doubly linked list
I/P: 10 20 30 40
O/P: 40 30 20 10
"""
def reverse_of_list(head):
    if head == None:
        return "List Doesn't exists"
    curr = head
    while curr.next:
        curr= curr.next
    while curr:
        print(curr.data,end=" ")
        curr = curr.prev
print("Reverse of the linked list:")
reverse_of_list(head)
print("\n")
    