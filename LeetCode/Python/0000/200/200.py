"""
Title : Number of Islands
Link : https://leetcode.com/problems/number-of-islands/
"""

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        ans = 0
        delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "0":
                    continue
                ans += 1
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    if grid[x][y] == "0":
                        continue
                    grid[x][y] = "0"
                    for dx, dy in delta:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w:
                            if grid[nx][ny] == "1":
                                queue.append((nx, ny))
        return ans


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    solution = Solution()
    print(solution.numIslands(grid))
