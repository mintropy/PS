"""
Title : Palindrome Linked List
Link : https://leetcode.com/problems/palindrome-linked-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        if nums[:] == nums[::-1]:
            return True
        return False


if __name__ == "__main__":
    pass
