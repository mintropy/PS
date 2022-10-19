"""
Title : Merge Two Sorted Lists
Link : https://leetcode.com/problems/merge-two-sorted-lists/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = []
        while list1 is not None:
            nums.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            nums.append(list2.val)
            list2 = list2.next
        if not nums:
            return 
        nums.sort()
        ans = ListNode(nums[0])
        now = ans
        for i in range(1, len(nums)):
            x = nums[i]
            now.next = ListNode(x)
            now = now.next
        return ans


if __name__ == "__main__":
    pass
