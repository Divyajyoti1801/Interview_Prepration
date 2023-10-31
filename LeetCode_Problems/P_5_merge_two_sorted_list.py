"""
Problem - 5 : MERGE TWO SORTED LIST

Problem Statement:
    - You are given the heads of two sorted linked lists list1 and list2.
    - Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
    - Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def print_LL(head):
    if head == None:
        return head
    temp = head
    while temp:
        print(temp.data,end=" ")
        temp = temp.next
    print()

def merge_two_sorted_list(head_1,head_2):
    h1 = head_1
    h2 = head_2
    res_head = Node(-1)
    res = res_head

    
    while h1 and h2:
        if h1.data<= h2.data:
            res.next = h1
            h1 = h1.next
        else:
            res.next = h2
            h2 = h2.next
        
        res = res.next
    
    res.next = h1 or h2    
    return res_head.next
    
head_1 = Node(1)
head_1.next = Node(2) # type: ignore
head_1.next.next = Node(4) # type: ignore
print("Input List - 1 :")
print_LL(head_1)
head_2 = Node(1)
head_2.next = Node(3) # type: ignore
head_2.next.next = Node(4) # type: ignore
print("Input List - 2 :")
print_LL(head_2)

print("Merge of Two Sorted Linked-List: ");
res_head = merge_two_sorted_list(head_1,head_2)
print_LL(res_head)