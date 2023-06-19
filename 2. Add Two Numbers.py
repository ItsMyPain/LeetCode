# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        sm = node1.val + node2.val
        first_node = ListNode(sm % 10)
        current_node = first_node
        next_sm = sm // 10
        while node1.next is not None or node2.next is not None:
            node1 = node1.next or ListNode()
            node2 = node2.next or ListNode()

            sm = node1.val + node2.val + next_sm
            next_node = ListNode(sm % 10)
            next_sm = sm // 10
            current_node.next = next_node
            current_node = next_node

        if next_sm > 0:
            current_node.next = ListNode(next_sm)

        return first_node
