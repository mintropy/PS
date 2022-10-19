"""
Title : 3Sum
Link : https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i, x in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = x + nums[left] + nums[right]
                if tmp < 0:
                    left += 1
                elif tmp > 0:
                    right -= 1
                else:
                    ans.add((x, nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return list(ans)


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2, 0, 1, 1, 2]

    solution = Solution()
    print(solution.threeSum(nums))
