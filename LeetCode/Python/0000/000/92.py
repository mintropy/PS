"""
Title : Reverse Linked List II
Title : https://leetcode.com/problems/reverse-linked-list-ii/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        left_list, mid_list, right_list = [], [], []
        idx = 0
        while head is not None:
            if idx < left:
                left_list.append(head.val)
            elif left <= idx < right:
                mid_list.append(head.val)
            else:
                right_list.append(head.val)
            head = head.next
            idx += 1
        mid_list.reverse()
        nums = left_list + mid_list + right_list
        return self.make_linked_list(nums)

    def make_linked_list(self, nums):
        if not nums:
            return
        linked_list = ListNode(nums[0])
        now = linked_list
        for x in nums[1:]:
            now.next = ListNode(x)
            now = now.next
        return linked_list


if __name__ == "__main__":

    def make_linked_list(nums: list[int]) -> ListNode:
        node = ListNode(nums[0])
        now = node
        for x in nums[1:]:
            now.next = ListNode(x)
            now = now.next
        return node

    head = make_linked_list([1, 2, 3, 4, 5])

    solution = Solution()
    ans = solution.reverseBetween(head, 1, 4)

    while ans is not None:
        print(ans.val, end=" ")
        ans = ans.next
