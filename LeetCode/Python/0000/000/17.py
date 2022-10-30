"""
Title : Letter Combinations of a Phone Number
Link : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

from typing import List


class Solution:
    def __init__(self) -> None:
        self.alphabets = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        self.ans = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits = [int(x) for x in digits]
        self.search(digits, 0, "")
        return self.ans

    def search(self, digits, idx, s):
        if idx == len(digits):
            self.ans.append(s)
            return
        for x in self.alphabets[digits[idx]]:
            self.search(digits, idx + 1, s + x)


if __name__ == "__main__":
    pass
