"""
Title : Product of Array Except Self
Link : https://leetcode.com/problems/product-of-array-except-self/
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if (zero_count := nums.count(0)) >= 2:
            return [0] * len(nums)
        elif zero_count == 1:
            zero_index = nums.index(0)
            ans = [0] * len(nums)
            ans[zero_index] = 1
            for x in nums:
                if not x:
                    continue
                ans[zero_index] *= x
            return ans
        product = 1
        for x in nums:
            product *= x
        ans = []
        for x in nums:
            ans.append(product // x)
        return ans


if __name__ == "__main__":
    pass
