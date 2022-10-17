"""
Title : 3Sum
Link : https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = set()
        while right - left >= 2:
            x, y = nums[left], nums[right]
            tmp = x + y
            for i in range(left + 1, right):
                z = nums[i]
                if tmp + z == 0:
                    ans.add((x, z, y))
                elif tmp + z > 0:
                    break
            if tmp == 0:
                if nums[left + 1] - x > y - nums[right - 1]:
                    right -= 1
                else:
                    left += 1
            elif tmp > 0:
                right -= 1
            else:
                left += 1
        return list(ans)


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2, 0, 1, 1, 2]
    nums = [-1, 0, 1, 2, -1, -4]

    solution = Solution()
    print(solution.threeSum(nums))
