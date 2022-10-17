"""
Title : Two Sum
Link : https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, x in enumerate(nums):
            if (y := target - x) in nums_dict:
                return [nums_dict[y], i]
            nums_dict[x] = i


if __name__ == "__main__":
    pass
