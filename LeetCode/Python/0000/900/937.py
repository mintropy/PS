"""
Title : Reorder Data in Log Files
Link : https://leetcode.com/problems/reorder-data-in-log-files/
"""

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sorting_algorithm(log):
            if log[-1].isnumeric():
                return (1,)
            left, right = log.split(" ", 1)
            return (0, right, left)

        return sorted(logs, key=sorting_algorithm)


if __name__ == "__main__":
    Solution = Solution()

    logs = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]

    print(Solution.reorderLogFiles(logs))
