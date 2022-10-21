"""
Title : Valid Parentheses
Link : https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in "({[":
                stack.append(x)
            elif not stack:
                return False
            elif x == ")" and stack[-1] == "(":
                stack.pop()
            elif x == "]" and stack[-1] == "[":
                stack.pop()
            elif x == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True


if __name__ == "__main__":
    pass
