"""
Title : Array Partition
Link : https://leetcode.com/problems/array-partition/
"""

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[i] for i in range(0, len(nums), 2)])


if __name__ == "__main__":
    pass
