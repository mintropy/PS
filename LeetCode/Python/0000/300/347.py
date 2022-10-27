"""
Title : Top K Frequent Elements
Link : https://leetcode.com/problems/top-k-frequent-elements/
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        nums = sorted([(k, v) for k, v in counter.items()], key=lambda x: -x[1])
        return [nums[i][0] for i in range(k)]


if __name__ == "__main__":
    pass
