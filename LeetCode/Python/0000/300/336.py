"""
Title : Palindrome Pairs
Link : https://leetcode.com/problems/palindrome-pairs/
"""

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backword = {word[::-1]: i for i, word in enumerate(words)}
        ans = []
        for i, word in enumerate(words):
            if word in backword and backword[word] != i:
                ans.append((i, backword[word]))
            if word and "" in backword and word == word[::-1]:
                ans.append((i, backword[""]))
                ans.append((backword[""], i))
            for j in range(len(word)):
                if word[j:] in backword and word[:j] == word[j - 1 :: -1]:
                    ans.append((backword[word[j:]], i))
                if word[:j] in backword and word[j:] == word[: j - 1 : -1]:
                    ans.append((i, backword[word[:j]]))
        return ans


if __name__ == "__main__":
    pass
