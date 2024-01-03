"""
Remove Nth Node From End Of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

"""

from REVERSE_LINKED_LIST import Node, print_linked_list


def remove_nth_node_from_the_end(head, n=0):
    fast = head
    slow = head

    for i in range(n):
        fast = fast.next

    if not fast:
        return head.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head


print("\n")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print_linked_list(head)
print()
print("Remove nth node from the end of the linked list: ")
head = remove_nth_node_from_the_end(head, n=2)
print_linked_list(head)
