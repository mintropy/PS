"""
Title : 감시
Link : https://www.acmicpc.net/problem/15683
"""

# 1번 cctv 감시 만드는 중 - 완료
# 2 ~ 5번 cctv 만들기 : 2 완료
# dfs 부분 수정해야됨

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

Coordinates = list[tuple[int]]


class CCTV:
    def __init__(self, N: int, M: int, office: list[list[int]]) -> None:
        self.office: list[list[int]] = office
        self.office_size: list[int] = [n, m]
        self.cctvs: Coordinates = []
        self.walls: Coordinates = []
        self.cctvs, self.walls = self.find_cctv_wall(self.office)
        self.delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
        self.max_watch = 0

    def find_cctv_wall(office: list[list[int]]) -> tuple[Coordinates]:
        cctvs: Coordinates = []
        walls: Coordinates = []
        for i, line in enumerate(office):
            for j, x in enumerate(line):
                if not x:
                    continue
                elif x == 6:
                    walls.append((i, j))
                else:
                    cctvs.append((i, j, x))
        return cctvs, walls

    def count_watch(self, office: list) -> int:
        """
        count all watched space
        """
        count = 0
        for i in range(self.office_size[0]):
            for j in range(self.office_size[1]):
                if office[i][j] == "#":
                    count += 1
        return count

    def cctv_1(self, i: int, j: int, office: list, d: int) -> list:
        """
        search office form (i, j) by given direction d
        """
        next_office = office.copy()
        next_office[i][j] = "#"
        x, y = i + self.direction[0][d], j + self.direction[1][d]
        while True:
            # 감시 범위가 사무실을 넘어가면 중지
            if x < 0 or x >= self.office_size[0]:
                break
            if y < 0 or y >= self.office_size[1]:
                break
            # 감시 범위가 벽을 만나면 중지
            if self.office[x][y] == 6:
                break
            # 해당되지 않으면, 감시 처리
            next_office[x][y] = "#"
            x += self.direction[0][d]
            y += self.direction[1][d]
        return next_office

    def cctv_2(self, i: int, j: int, office: list, d: int) -> list:
        # d = 0이면 위아래로, 1이면 좌우로 탐색
        next_office = office.copy()
        # d == 0 or 1에 해당하는 방향으로 탐색
        # 이후 d == 2 or 3에 해당하는 방향으로 탐색
        next_office = self.cctv_1(i, j, next_office, d)
        next_office = self.cctv_1(i, j, next_office, d + 2)
        return next_office

    def cctv_3(self, i: int, j: int, office: list, d: int) -> list:
        next_office = office.copy()
        # 주어진 방향 d와 그 오른쪽에 해당하는 방향 탐색
        # 0, 1, 2, 3이 주어지면 각각 1, 2, 3, 0을 같이 탐색
        if d == 3:
            next_office = self.cctv_1(i, j, next_office, d)
            next_office = self.cctv_1(i, j, next_office, 0)
        else:
            next_office = self.cctv_1(i, j, next_office, d)
            next_office = self.cctv_1(i, j, next_office, d + 1)
        return next_office

    def cctv_4(self, i: int, j: int, office: list, d: int) -> list:
        # 방향 d를 제외하고 탐색
        next_office = office.copy()
        for k in range(4):
            if k == d:
                continue
            next_office = self.cctv_1(i, j, next_office, k)
        return next_office

    def cctv_5(self, i: int, j: int, office: list) -> list:
        # 모든 방향 탐색
        next_office = office.copy()
        for k in range(4):
            next_office = self.cctv_1(i, j, next_office, k)
        return next_office

    def dfs(self, idx, office):
        if idx == len(self.cctv):
            count = self.count_watch(office)
            if count > self.max_watch:
                self.max_watch = count
            return
        i, j, cctv_num = self.cctv[idx]
        # cctv 종류에 따라 dfs 실시
        if cctv_num == 1:
            for d in range(4):
                next_office = self.cctv_1(i, j, office, d)
                self.dfs(idx + 1, next_office)
        elif cctv_num == 2:
            for d in range(2):
                self.dfs(idx + 1, self.cctv_2(i, j, office, d))
        elif cctv_num == 3:
            for d in range(4):
                self.dfs(idx + 1, self.cctv_3(i, j, office, d))
        elif cctv_num == 4:
            for d in range(4):
                self.dfs(idx + 1, self.cctv_4(i, j, office, d))
        elif cctv_num == 5:
            self.dfs(idx + 1, self.cctv_5(i, j, office))


if __name__ == "__main__":
    N, M = MIIS()
    office_map = [list(MIIS()) for _ in range(N)]
    cctv = CCTV(N, M, office_map)
