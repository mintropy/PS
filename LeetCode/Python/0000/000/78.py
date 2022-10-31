"""
Title : Subsets
Link : https://leetcode.com/problems/subsets/
"""

from typing import List


class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.nums = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.search([False] * len(nums), 0, [])
        return self.ans

    def search(self, check, idx, tmp):
        if idx == len(self.nums):
            self.ans.append(tmp[::])
            return
        tmp.append(self.nums[idx])
        check[idx] = True
        self.search(check, idx + 1, tmp)
        tmp.pop()
        check[idx] = False
        self.search(check, idx + 1, tmp)


if __name__ == "__main__":
    pass
