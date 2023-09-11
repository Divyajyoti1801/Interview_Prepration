"""
LINKED LIST ADVANCE CONCEPTS AND QUESTIONS
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

head = Node(10)
head.link = Node(20) # type: ignore
head.link.link = Node(30) # type: ignore
head.link.link.link = Node(40) # type: ignore
head.link.link.link.link = Node(50) # type: ignore
head.link.link.link.link.link = Node(60) # type: ignore
head.link.link.link.link.link.link = Node(70) # type: ignore


def printList(head):
    curr = head
    while curr!=None:
        print(curr.data,end=" ")
        curr = curr.link
    print()

print("Initial Linked List to be used: ")
printList(head)
print("-------------------------------------------------------------")


"""
Problem Statement: Reverse a linked list in groups
"""
def reverse_linked_list_groups_1(head,k):
    curr = head
    prev_first = head
    first_pass = True
    while curr!=None:
        first,prev = curr,None
        count = 0
        while curr!=None and count<k:
            nex = curr.link
            curr.link = prev
            prev = curr
            curr = nex
            count+=1
        if first_pass:
            head = prev
            first_pass = False
        else:
            prev_first.link = prev
        prev_first =first
    return head
print("Reverse linked list in groups(Iterative): ")
ps1_head_1 = reverse_linked_list_groups_1(head,3)
printList(ps1_head_1)
def reverse_linked_list_groups_2(head,k):
    curr = head
    prev,nex = None,None
    count = 0
    while curr!=None and count<k:
        nex = curr.link
        curr.link = prev
        prev = curr
        curr = nex
        count+=1
    if nex!= None:
        rem_head = reverse_linked_list_groups_2(curr,k)
        head.link = rem_head
    return prev
print("Reverse Linked List in groups(Recursive): ");
ps1_head_2=reverse_linked_list_groups_2(head,3)
printList(ps1_head_2)
print()

"""
Problem Statement: Detect a loop in a linked list 
  Efficient Solution:
    - Create an empty set
    - Traverse through the list and do following for every node x
        = If x is already in the set; return True
        = Else put x in the set
    - Return False
    - Time Complexity: O(n)
    - Auxiliary Space: O(n)
"""
cycle_head = Node(10)
cycle_head.link = Node(15) # type: ignore
cycle_head.link.link = Node(12) # type: ignore
cycle_head.link.link.link = Node(20) # type: ignore
cycle_head.link.link.link = cycle_head.link # type: ignore

"""
Detect Loop using Floyd's Cycle Detection
    Algorithm : 
        - Initialize slow_p = head, fast_p = head;
        - Move slow_p by one fast_p by
        - two if these pointers meet, then there is a loop
        - Time Complexity: O(m+n)
"""
def floyd_cycle_detection(head):
    slow_p = head
    fast_p = head
    while fast_p!=None and fast_p.link!=None:
        slow_p = slow_p.link
        fast_p = fast_p.link.link
        if slow_p == fast_p:
            return True
    return False
print("Floyd's Cycle detection Algorithm: ",floyd_cycle_detection(cycle_head))
print()


"""
Problem Statement: Detect and remove the loop in the linked list
"""
def detect_and_remove_loop(head):
    slow = head
    fast = head
    while fast!=None and fast.link!=None:
        slow = slow.link
        fast = fast.link.link
        if slow == fast:
            break
    
    if slow!=fast:
        return head
    slow = head
    while slow.link!=fast.link:
        slow = slow.link
        fast = fast.link
    fast.link = None
    return head
print("Detect and Remove the loop from the linked list: ")
cycle_head=detect_and_remove_loop(cycle_head)
printList(cycle_head)
print()