"""
Problem - 16 : Intersection Of Two Linked-List

Problem Statement:
    - Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def intersection_of_node(head1,head2):
    one = head1
    two = head2

    while one!=two:
        one = head2 if one is None else one.next
        two = head1 if two is None else two.next

    return None