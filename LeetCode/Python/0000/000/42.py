"""
Title : Trapping Rain Water
Link : https://leetcode.com/problems/trapping-rain-water/
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans

    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i, x in enumerate(height):
            while stack and x > height[stack[-1]]:
                y = stack.pop()
                if not stack:
                    break
                ans += (i - stack[-1] - 1) * (
                    min(height[i], height[stack[-1]]) - height[y]
                )
            stack.append(i)
        return ans


if __name__ == "__main__":
    pass
