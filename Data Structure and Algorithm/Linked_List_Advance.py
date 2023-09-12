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
    Solution Algorithm: 
        - Detect loop using Floyd's detection algorithm
        - Move "slow_p" to the beginning of linked list and keep "fast_p" at the meeting point
        - Now one by one move slow and fast (at same speed). The point where they meet now in the 
"""
def detect_and_remove_loop(head):
    slow = head
    fast = head
    # Detect the loop
    while fast!=None and fast.link!=None:
        slow = slow.link
        fast = fast.link.link
        if slow == fast:
            break
    
    if slow!=fast:
        return head
    # Removing the loop
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

"""
Problem Statement: Intersection point of two linked list
    - Time Complexity: O(n+m)
    - Space Complexity: O(n)
"""
def get_intersection_of_two_linked_list_1(head1,head2):
    s = set()
    curr = head1
    while curr!=None:
        s.add(curr.data)
        curr = curr.link
    curr = head2
    while curr!=None:
        if curr.data in s:
            return curr.data
        curr = curr.link
    return -1
# Input linked list 1
head_1 = Node(10)
head_1.link = Node(20) # type: ignore
head_1.link.link = Node(30) # type: ignore
head_1.link.link.link = Node(40) # type: ignore
print("List-1: ")
printList(head_1)
# Input linked list 2
head_2 = Node(50)
head_2.link = Node(30) # type: ignore
head_2.link.link = Node(80) # type: ignore
head_2.link.link.link = Node(100) # type: ignore
print("List-2: ")
printList(head_2)
print("Intersection point of two linked list(Hashing Method): ",get_intersection_of_two_linked_list_1(head_1,head_2))
def get_size(head):
    if head is None:
        return 0
    count = 0
    while head!=None:
        count+=1
        head = head.link
    return count
def get_intersection_of_two_linked_list_2(d,head1,head2):
    curr1 = head1
    curr2 = head2
    for i in range(d):
        if curr1 == None:
            return -1
        curr1 = curr1.link
    while curr1!=None and curr2!=None:
        if curr1.data == curr2.data:
            return curr1.data
        curr1 = curr1.link
        curr2 = curr2.link
    return -1
print("Intersection of two linked list (Iterative) : ",get_intersection_of_two_linked_list_2(abs(get_size(head_1)-get_size(head_2)),head_1,head_2))
print()

"""
Problem Statement : Segregate Even and Odd Nodes
    - Naive Solution:
        - Find the last Node reference / pointer by doing a traversal
        - Traverse the linked list again. For every node, insert it after the last node and make the newly inserted node as the new last node.
"""
def segregate_even_and_odd(head):
    even_start,even_end,odd_start,odd_end = None,None,None,None
    curr = head
    while curr!=None:
        x = curr.data
        if x%2 == 0:
            if even_start == None:
                even_start = curr
                even_end = even_start
            else:
                even_end.link = curr
                even_end = even_end.link
        else:
            if odd_start == None:
                odd_start = curr
                odd_end = odd_start
            else:
                if odd_start == None:
                    odd_start = curr
                    odd_end = odd_start
                else:
                    odd_end.link = curr
                    odd_end = odd_end.link
        curr = curr.link
    
    if odd_start == None or even_start == None:
        return head
    even_end = odd_start
    odd_start = None
    return even_start
print("Segregate Even and Odd Node: ")
res_head = segregate_even_and_odd(head_1)
printList(res_head)

"""
Problem Statement: Pairwise swap Nodes
"""
def pairwise_swap_node_1(head):
    curr = head
    while curr != None and curr.link!=None:
        curr.data,curr.link.data = curr.link.data,curr.data
        curr = curr.link.link
    return head
print("Pair wise swapping Nodes (Swapping Data): ")
res_head = pairwise_swap_node_1(head_1)
printList(res_head)
def pairwise_swap_node_2(head):
    if head == None or head.link == None:
        return head
    curr = head.link.link
    prev = head
    head = head.link
    while curr!=None and curr.link!=None:
        prev.link = curr.link
        prev = curr
        nex = curr.link.link
        curr.link.link = curr
        curr = nex
    prev.link = curr
    return head
print("Pair wise swapping Node (Changing/pointers references): ")
res_head = pairwise_swap_node_2(head_1)
printList(res_head)