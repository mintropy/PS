"""
Title : Most Common Word
Link : https://leetcode.com/problems/most-common-word/
"""

from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph += " "
        words = {}
        tmp = ""
        for x in paragraph:
            if x in "!?',;. ":
                if not tmp:
                    continue
                if tmp in words:
                    words[tmp] += 1
                else:
                    words[tmp] = 1
                tmp = ""
                continue
            x = x.lower()
            tmp += x
        for k, _ in sorted(words.items(), key=lambda x: -x[1]):
            if k in banned:
                continue
            return k


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    solution = Solution()
    print(solution.mostCommonWord(paragraph, banned))
