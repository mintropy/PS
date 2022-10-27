"""
Title : Longest Substring Without Repeating Characters
Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ""
        now = ""
        check = {x: 0 for x in s}
        for x in s:
            if check[x]:
                if len(ans) < len(now):
                    ans = now
                while ans:
                    y = now[0]
                    check[y] -= 1
                    now = now[1:]
                    if x == y:
                        break
            now += x
            check[x] += 1
        if len(ans) < len(now):
            ans = now
        return len(ans)


if __name__ == "__main__":
    s = "abcabcbb"

    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
