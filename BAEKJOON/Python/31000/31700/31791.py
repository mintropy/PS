"""
Title : 바이러스 공격
Link : https://www.acmicpc.net/problem/31791
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


class VirusAttack:
    def __init__(
        self, N: int, M: int, Tg: int, Tb: int, city_map: list[list[str]]
    ) -> None:
        self.VIRUS = "*"
        self.EMPTY = "."
        self.BUILDING = "#"
        self.BUILDING_INFECTED = "X"

        self.N = N
        self.M = M
        self.Tg = Tg
        self.Tb = Tb
        self.city_map: list[list[str]] = city_map
        self.viruses = self.search_initial_virus()
        self.buildings: dict[int, set[tuple[int, int]]] = {
            i: set() for i in range(Tb + 1)
        }

    def search_initial_virus(self) -> list[tuple[int, int]]:
        viruses = []
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                if self.city_map[i][j] == self.VIRUS:
                    viruses.append((i, j))
        return viruses

    def attack(self) -> None:
        for _ in range(self.Tg):
            new_viruses = []
            while self.viruses:
                x, y = self.viruses.pop()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    position = self.city_map[nx][ny]
                    if position == self.EMPTY:
                        self.city_map[nx][ny] = self.VIRUS
                        new_viruses.append((nx, ny))
                    elif position == self.BUILDING:
                        self.city_map[nx][ny] = self.BUILDING_INFECTED
                        self.buildings[self.Tb].add((nx, ny))
            self.viruses = new_viruses

            for x, y in self.buildings[0]:
                self.city_map[x][y] = self.VIRUS
                self.viruses.append((x, y))
            self.buildings[0] = set()
            for i in range(1, self.Tb + 1):
                for x, y in self.buildings[i]:
                    self.buildings[i - 1].add((x, y))
                self.buildings[i] = set()

    def get_answer(self) -> int | str:
        answer = []
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                if self.city_map[i][j] != self.VIRUS:
                    answer.append((i, j))
        if answer:
            return "\n".join([f"{x} {y}" for x, y in answer])
        return -1


if __name__ == "__main__":
    N, M = MIIS()
    Tg, Tb, X, B = MIIS()
    city_map = (
        [[" "] * (N + 2)]
        + [[" "] + [x for x in input().strip()] + [" "] for _ in range(N)]
        + [[" "] * (N + 2)]
    )

    va = VirusAttack(N, M, Tg, Tb, city_map)
    va.attack()
    print(va.get_answer())
