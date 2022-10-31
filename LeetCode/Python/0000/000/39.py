"""
Title : Combination Sum
Link : https://leetcode.com/problems/combination-sum/
"""

from typing import List


class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.candidates = []
        self.target = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.target = target
        self.search(0, [], 0)
        return self.ans

    def search(self, idx, nums, sum_now):
        if sum_now == self.target:
            self.ans.append(nums[::])
            return
        for i in range(idx, len(self.candidates)):
            x = self.candidates[i]
            if (next_sum := sum_now + x) <= self.target:
                nums.append(x)
                self.search(i, nums, next_sum)
                nums.pop()
            else:
                break


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7

    solution = Solution()
    print(solution.combinationSum(candidates, target))
