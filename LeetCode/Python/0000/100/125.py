"""
Title : Valid Palindrome
Link : https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(x for x in s if x.isalnum())
        s = s.lower()
        if s == s[::-1]:
            return True
        return False


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    s = " "

    solution = Solution()
    print(solution.isPalindrome(s))
