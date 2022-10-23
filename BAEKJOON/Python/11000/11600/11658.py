"""
Title : 구간 합 구하기 3
Link : https://www.acmicpc.net/problem/11658
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


class PrefixSum:
    def __init__(self, N: int, numbers: list[list[int]]) -> None:
        self.N = N
        self.prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
        self.init_prefix_sum(numbers)

    def init_prefix_sum(self, numbers: list[list[int]]) -> None:
        for i, line in enumerate(numbers):
            for j, x in enumerate(line):
                self.prefix_sum[i + 1][j + 1] = self.prefix_sum[i + 1][j] + x
            for j in range(self.N):
                self.prefix_sum[i + 1][j + 1] += self.prefix_sum[i][j + 1]

    def update(self, x: int, y: int, c: int) -> None:
        diff = c - self.get_sum(x, y, x, y)
        for i in range(x, self.N + 1):
            for j in range(y, self.N + 1):
                self.prefix_sum[i][j] += diff

    def get_sum(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return (
            self.prefix_sum[x2][y2]
            - self.prefix_sum[x2][y1 - 1]
            - self.prefix_sum[x1 - 1][y2]
            + self.prefix_sum[x1 - 1][y1 - 1]
        )


if __name__ == "__main__":
    N, M = MIIS()
    numbers = [list(MIIS()) for _ in range(N)]
    prefix_sum = PrefixSum(N, numbers)
    for _ in range(M):
        w, *cmd = MIIS()
        if not w:
            x, y, c = cmd
            prefix_sum.update(x, y, c)
        else:
            x1, y1, x2, y2 = cmd
            print(prefix_sum.get_sum(x1, y1, x2, y2))
