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
        if left == right:
            return head
        ans = now = ListNode(None)

        now.next = head
        for _ in range(left - 1):
            now = now.next
        next_node = now.next

        for _ in range(right - left):
            tmp, now.next, next_node.next = (
                now.next,
                next_node.next,
                next_node.next.next,
            )
            now.next.next = tmp
        return ans.next


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
