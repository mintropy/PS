"""
Title : 주사위 굴리기
Link : https://www.acmicpc.net/problem/14499
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


class Dice:
    def __init__(self, N: int, M: int, x: int, y: int, my_map: list[list[int]]) -> None:
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.front = 0
        self.back = 0
        self.N = N
        self.M = M
        self.x = x
        self.y = y
        self.my_map = my_map

    def rotatable(self, direction: int) -> bool:
        if direction == 1 and self.y == self.M - 1:
            return False
        if direction == 2 and self.y == 0:
            return False
        if direction == 3 and self.x == 0:
            return False
        if direction == 4 and self.x == self.N - 1:
            return False
        return True

    def rotate(self, direction: int) -> None:
        if direction == 1:
            self.up, self.left, self.down, self.right = (
                self.left,
                self.down,
                self.right,
                self.up,
            )
            self.y += 1
        elif direction == 2:
            self.up, self.left, self.down, self.right = (
                self.right,
                self.up,
                self.left,
                self.down,
            )
            self.y -= 1
        elif direction == 3:
            self.up, self.front, self.down, self.back = (
                self.front,
                self.down,
                self.back,
                self.up,
            )
            self.x -= 1
        elif direction == 4:
            self.up, self.front, self.down, self.back = (
                self.back,
                self.up,
                self.front,
                self.down,
            )
            self.x += 1

    def copy(self) -> None:
        if not self.my_map[self.x][self.y]:
            self.my_map[self.x][self.y] = self.down
        else:
            self.down = self.my_map[self.x][self.y]
            self.my_map[self.x][self.y] = 0


if __name__ == "__main__":
    N, M, x, y, K = MIIS()
    my_map = [list(MIIS()) for _ in range(N)]

    dice = Dice(N, M, x, y, my_map)
    for cmd in MIIS():
        if not dice.rotatable(cmd):
            continue
        dice.rotate(cmd)
        dice.copy()
        print(dice.up)
