"""
Title : Merge K Sorted Lists
Link : https://leetcode.com/problems/merge-k-sorted-lists/
"""

from heapq import heapify, heappop, heappush
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node is None:
                continue
            heap.append((node.val, i, node))
        if not heap:
            return
        heapify(heap)
        ans = now = ListNode(None)
        while heap:
            x, idx, node = heappop(heap)
            now.next = ListNode(x)
            now = now.next
            if node.next is None:
                continue
            node = node.next
            heappush(heap, (node.val, idx, node))
        return ans.next


if __name__ == "__main__":
    pass
