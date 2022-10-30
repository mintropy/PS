"""
Title : Combinations
Link : https://leetcode.com/problems/combinations/
"""

from typing import List


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.search(n, 0, k, [])
        return self.ans

    def search(self, n, check, k, nums):
        if check == k:
            self.ans.append(nums[::])
            return
        if not n:
            return
        nums.append(n)
        self.search(n - 1, check + 1, k, nums)
        nums.pop()
        self.search(n - 1, check, k, nums)


if __name__ == "__main__":
    pass
