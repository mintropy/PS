"""
Title : Group Anagrams
Link : https://leetcode.com/problems/group-anagrams/
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for str in strs:
            check = [0] * 26
            for s in str:
                check[ord(s) - 97] += 1
            check = tuple(check)
            if check in words:
                words[check].append(str)
            else:
                words[check] = [str]
        return list(words.values())


if __name__ == "__main__":
    pass
