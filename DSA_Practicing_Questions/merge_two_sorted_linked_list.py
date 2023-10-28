"""
Problem - 6 : MERGE OF TWO SORTED LINKED LIST

Problem Statement:
    - Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.

I/P : N = 4, M = 3
valueN[] = {5,10,15,40}
valueM[] = {2,3,20}
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head_1 = Node(5)
head_1.next = Node(10) # type: ignore
head_1.next.next = Node(15) # type: ignore
head_1.next.next.next = Node(40) # type: ignore
head_2 = Node(2)
head_2.next = Node(3) # type: ignore
head_2.next.next = Node(20) # type: ignore

def print_LL(head):
    if head==None:
        return None
    temp = head
    while(temp!=None):
        print(temp.data,end=" ")
        temp = temp.next
print("Input Linked-List: ")
print_LL(head_1)
print()
print_LL(head_2)
print()

def merge_of_two_sorted_linked_list(head_1,head_2):
    h1= head_1
    h2= head_2
    x = Node(0)
    y= x
    
    while h1 and h2:
        y.next = Node(0) # type: ignore
        y = y.next
        if h1.data<= h2.data:
            y.data = h1.data
            h1 = h1.next
        else:
            y.data= h2.data
            h2  = h2.next
    
    if h1:
        while h1:
            y.next = Node(0)#type:ignore
            y = y.next
            y.data = h1.data
            h1 = h1.next
    if h2:
        while h2:
            y.next = Node(0) #type:ignore
            y = y.next
            y.data = h2.data
            h2 = h2.next
    return x.next
            
            
        
print("Merging Two Sorted Linked List: ")
res_head = merge_of_two_sorted_linked_list(head_1,head_2) 
print_LL(res_head)       
    

            

            