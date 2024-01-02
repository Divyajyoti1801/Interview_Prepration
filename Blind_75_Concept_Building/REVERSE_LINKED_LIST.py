"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_linked_list(head: Node):
    if head == None:
        print("Linked-List Empty")
        return

    temp = head
    while temp != None:
        print(temp.data, end=", ")
        temp = temp.next


def reverse_of_linked_list(head: Node):
    if head == None:
        return None

    if head.next == None:
        return head

    prev = None
    curr = head

    while curr != None:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex

    return prev


print("Reverse of the linked list: ")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = reverse_of_linked_list(head)

print_linked_list(head)
