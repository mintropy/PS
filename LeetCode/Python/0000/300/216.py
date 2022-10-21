"""
Title : Remove Duplicate Letters
Link : https://leetcode.com/problems/remove-duplicate-letters/
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return "".join(sorted(set(s)))

if __name__ == "__main__":
    pass