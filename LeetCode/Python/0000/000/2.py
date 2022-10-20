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
        num1, num2 = [], []
        while l1 is not None:
            num1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            num2.append(l2.val)
            l2 = l2.next
        num1.reverse()
        num2.reverse()
        n1 = n2 = 0
        for x in num1:
            n1 = n1 * 10 + x
        for x in num2:
            n2 = n2 * 10 + x
        num = n1 + n2
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

    def make_linked_list(nums: list[int]) -> ListNode:
        node = ListNode(nums[0])
        now = node
        for x in nums[1:]:
            now.next = ListNode(x)
            now = now.next
        return node

    list1 = make_linked_list([2, 4, 9])
    list2 = make_linked_list([5, 6, 4, 9])

    list1 = make_linked_list([0, 8, 6, 5, 6, 8, 3, 5, 7])
    list2 = make_linked_list([6, 7, 8, 0, 8, 5, 8, 9, 7])

    solution = Solution()
    print(solution.addTwoNumbers(list1, list2))
