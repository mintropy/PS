"""
Title : Daily Temperatures
Link : https://leetcode.com/problems/daily-temperatures/
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    solution = Solution()
    print(solution.dailyTemperatures(temperatures))
