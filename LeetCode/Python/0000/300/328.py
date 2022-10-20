"""
Title : Odd Even Linked List
Link : https://leetcode.com/problems/odd-even-linked-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        odd_list = ListNode(head.val)
        head = head.next
        if head is None:
            return odd_list
        even_list = ListNode(head.val)
        head = head.next

        odd_first = odd_list
        even_first = even_list
        count = 0
        while head is not None:
            if count % 2:
                even_list.next = ListNode(head.val)
                even_list = even_list.next
            else:
                odd_list.next = ListNode(head.val)
                odd_list = odd_list.next
            head = head.next
            count += 1
        odd_list.next = even_first
        return odd_first


if __name__ == "__main__":
    pass
