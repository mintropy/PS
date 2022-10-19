"""
Title: Reverse Linked List
Link : https://leetcode.com/problems/reverse-linked-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        if not nums:
            return
        ans = ListNode(nums[-1])
        now = ans
        for i in range(len(nums) - 2, -1, -1):
            now.next = ListNode(nums[i])
            now = now.next
        return ans


if __name__ == "__main__":
    pass
