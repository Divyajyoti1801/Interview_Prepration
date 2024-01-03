"""
Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""
from REVERSE_LINKED_LIST import Node, print_linked_list


def reorder_list(head):
    slow, fast = head, head.next
    # For finding middle of the Linked-List
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # Merge two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
print("\n")
print_linked_list(head)
print()
print("Reorder the List : ")
reorder_list(head)
print_linked_list(head)
