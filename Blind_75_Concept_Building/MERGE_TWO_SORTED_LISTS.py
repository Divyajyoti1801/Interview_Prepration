"""
Merge Two Sorted Lists 

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""
from REVERSE_LINKED_LIST import print_linked_list, Node


def merge_two_sorted_lists(head_1, head_2):
    if head_1 is None or head_2 is None:
        return None

    res_head = Node(-1)
    temp = res_head

    while head_1 and head_2:
        if head_1.data < head_2.data:
            temp.next = head_1
            head_1 = head_1.next
        elif head_1.data == head_2.data:
            temp.next = head_1
            head_1 = head_1.next
            head_2 = head_2.next
        else:
            temp.next = head_2
            head_2 = head_2.next
        temp = temp.next

    while head_1:
        temp.next = head_1
        head_1 = head_1.next
        temp = temp.next
    while head_2:
        temp.next = head_2
        head_2 = head_2.next
        temp = temp.next

    return res_head.next


head_1 = Node(1)
head_1.next = Node(2)
head_1.next.next = Node(4)
print()
print_linked_list(head_1)
print()
head_2 = Node(1)
head_2.next = Node(3)
head_2.next.next = Node(4)
print_linked_list(head_2)
print()
print("Merge of Two Sorted Linked list : ")
head = merge_two_sorted_lists(head_1, head_2)
print_linked_list(head)
