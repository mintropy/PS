"""
Title : Add Two Numbers
Link : https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = num2 = 0
        while l1 is not None:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2 is not None:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        num = num1 + num2
        new_list = []
        if not num:
            new_list.append(0)
        while num:
            new_list.append(num % 10)
            num //= 10
        ans = ListNode(new_list[0])
        now = ans
        for i in range(1, len(new_list)):
            now.next = ListNode(new_list[i])
            now = now.next
        return ans


if __name__ == "__main__":
    pass
