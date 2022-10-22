"""
Title : Remove Duplicate Letters
Link : https://leetcode.com/problems/remove-duplicate-letters/
"""

from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack, check = Counter(s), [], set()
        for x in s:
            counter[x] -= 1
            if x in check:
                continue
            while stack and x < stack[-1] and counter[stack[-1]] > 0:
                check.remove(stack.pop())
            stack.append(x)
            check.add(x)
        return "".join(stack)


if __name__ == "__main__":
    pass
