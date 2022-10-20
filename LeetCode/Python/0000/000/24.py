"""
Title : Swap Nodes in Pairs
Link : https://leetcode.com/problems/swap-nodes-in-pairs/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        if not nums:
            return
        for i in range(0, len(nums) // 2):
            x, y = i * 2, i * 2 + 1
            nums[x], nums[y] = nums[y], nums[x]
        ans = ListNode(nums[0])
        now = ans
        for x in nums[1:]:
            now.next = ListNode(x)
            now = now.next
        return ans


if __name__ == "__main__":
    pass
