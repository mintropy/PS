"""
Title : Kth Largest Element in an Array
Link : https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

from heapq import heapify, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapify(nums)
        for _ in range(k - 1):
            heappop(nums)
        return -nums[0]


if __name__ == "__main__":
    pass
