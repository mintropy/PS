"""
Title : Longest Palindromic Substring
Link : https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        ans = s[0]
        for i, x in enumerate(s):
            tmp = x
            for j in range(1, length):
                if i - j < 0 or i + j >= length:
                    break
                if s[i - j] == s[i + j]:
                    tmp = s[i - j] + tmp + s[i + j]
                else:
                    break
                if len(tmp) > len(ans):
                    ans = tmp
            if i >= length - 1 or x != s[i + 1]:
                continue
            tmp = x + s[i + 1]
            if len(tmp) > len(ans):
                ans = tmp
            for j in range(1, length):
                if i - j < 0 or i + j + 1 >= length:
                    break
                if s[i - j] == s[i + j + 1]:
                    tmp = s[i - j] + tmp + s[i + j + 1]
                else:
                    break
                if len(tmp) > len(ans):
                    ans = tmp
        return ans


if __name__ == "__main__":
    s = "babad"
    s = "cbbd"

    solution = Solution()
    print(solution.longestPalindrome(s))
