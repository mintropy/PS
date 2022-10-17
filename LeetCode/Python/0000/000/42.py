"""
Title : Trapping Rain Water
Link : https://leetcode.com/problems/trapping-rain-water/
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i, x in enumerate(height):
            while stack and stack[-1][1] <= x:
                pass


if __name__ == "__main__":
    pass
