"""
Title : Permuations
Link : https://leetcode.com/problems/permutations/
"""

from typing import List


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums:
            self.search(nums, [False] * len(nums), [])
        return self.ans

    def search(self, nums, check, tmp):
        if all(check):
            self.ans.append(tmp[::])
        for i, b in enumerate(check):
            if b:
                continue
            tmp.append(nums[i])
            check[i] = True
            self.search(nums, check, tmp)
            tmp.pop()
            check[i] = False


if __name__ == "__main__":
    nums = [1, 2, 3]

    solution = Solution()
    print(solution.permute(nums))
