"""
Title : 감시
Link : https://www.acmicpc.net/problem/15683
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

Coordinates = list[tuple[int]]


class CCTV:
    def __init__(self, N: int, M: int, office: list[list[int]]) -> None:
        self.office: list[list[int]] = office
        self.N = N
        self.M = M
        self.cctvs: Coordinates = []
        self.walls: Coordinates = []
        self.find_cctv_wall(self.office)
        self.cctv_count: int = len(self.cctvs)
        self.delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
        self.cctv_directions = {
            1: [[0], [1], [2], [3]],
            2: [[0, 2], [1, 3]],
            3: [[0, 1], [1, 2], [2, 3], [3, 0]],
            4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
            5: [[0, 1, 2, 3]],
        }
        self.max_watch = 0

    def find_cctv_wall(self, office: list[list[int]]) -> tuple[Coordinates]:
        for i, line in enumerate(office):
            for j, x in enumerate(line):
                if not x:
                    continue
                elif x == 6:
                    self.walls.append((i, j))
                else:
                    self.cctvs.append((i, j, x))

    def search(self, idx: int, watches: set[tuple[int]]):
        if idx == self.cctv_count:
            self.max_watch = max(self.max_watch, len(watches))
            return
        x, y, cctv_type = self.cctvs[idx]
        for direction in self.cctv_directions[cctv_type]:
            self.search(idx + 1, watches | self.search_cctv(x, y, direction))

    def search_cctv(self, x: int, y: int, direction: list[int]) -> set[tuple[int]]:
        watches = set()
        for d in direction:
            nx, ny = x, y
            while 0 <= nx < self.N and 0 <= ny < self.M and self.office[nx][ny] < 6:
                watches.add((nx, ny))
                nx, ny = nx + self.delta[d][0], ny + self.delta[d][1]
        return watches


if __name__ == "__main__":
    N, M = MIIS()
    office_map = [list(MIIS()) for _ in range(N)]
    cctv = CCTV(N, M, office_map)
    cctv.search(0, set())
    print(N * M - cctv.max_watch - len(cctv.walls))
