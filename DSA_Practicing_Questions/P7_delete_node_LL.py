"""
Problem - 7 : DELETE OF NODE FROM THE LINKED LIST 

Problem Statement : 
    - Given a singly linked list and an integer x.Delete xth node from the singly linked list.

I/P : 1 ->  3 -> 4 ; pos = 3
O/P : 1 -> 3
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def Print_LL(head):
    if(head==None):
        return None
    temp = head
    while temp:
        print(temp.data,end=" ")
        temp=temp.next

# Input Linked List
head_1 = Node(1)
head_1.next = Node(5) # type: ignore
head_1.next.next = Node(2) # type: ignore
head_1.next.next.next = Node(9) # type: ignore

print("Input Linked List: ")
Print_LL(head_1)
print()


def delete_node_LL(head,pos):
    if head==None:
        return head
    if pos == 1:
        del_node = head
        head = head.next
        del_node.next = None
        del del_node
        return head
    temp = head
    i = 1
    while i<pos-1:
        temp = temp.next
        i+=1
    if temp.next != None:
        del_node = temp.next
        temp.next = del_node.next
        del_node.next = None
        del del_node
    
    return head

head_1 = delete_node_LL(head_1,2)
print("After Deleting Node: ")
Print_LL(head_1)