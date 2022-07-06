"""
Title : 큐빙
Link : https://www.acmicpc.net/problem/5373
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())


class RubiksCube:
    def __init__(self) -> None:
        self.up = [["w"] * 3 for _ in range(3)]
        self.down = [["y"] * 3 for _ in range(3)]
        self.front = [["r"] * 3 for _ in range(3)]
        self.back = [["o"] * 3 for _ in range(3)]
        self.left = [["g"] * 3 for _ in range(3)]
        self.right = [["b"] * 3 for _ in range(3)]

    def get_up(self) -> str:
        up = ""
        for line in self.up:
            up += f"{''.join(line)}\n"
        return up

    def rotate(self, commands: list[str]) -> None:
        for cmd in commands:
            clock = True if cmd[1] == "+" else False
            match cmd[0]:
                case "U":
                    self.rotate_up(clock)
                case "D":
                    self.rotate_down(clock)
                case "F":
                    self.rotate_front(clock)
                case "B":
                    self.rotate_back(clock)
                case "L":
                    self.rotate_left(clock)
                case "R":
                    self.rotate_right(clock)

    def rotate_up(self, clock: bool) -> None:
        if clock:
            self.front[0], self.left[0], self.back[0], self.right[0] = (
                self.right[0],
                self.front[0],
                self.left[0],
                self.back[0],
            )
        else:
            self.front[0], self.left[0], self.back[0], self.right[0] = (
                self.left[0],
                self.back[0],
                self.right[0],
                self.front[0],
            )

    def rotate_down(self, clock: bool) -> None:
        if clock:
            self.front[2], self.left[2], self.back[2], self.right[2] = (
                self.left[2],
                self.back[2],
                self.right[2],
                self.front[2],
            )
        else:
            self.front[2], self.left[2], self.back[2], self.right[2] = (
                self.right[2],
                self.front[2],
                self.left[2],
                self.back[2],
            )

    def rotate_front(self, clock: bool) -> None:
        left, right = [self.left[i][2] for i in range(3)], [
            self.right[i][0] for i in range(3)
        ]
        if clock:
            for i in range(3):
                self.left[i][2] = self.down[0][i]
                self.right[i][0] = self.up[2][i]
            self.up[2] = left[::-1]
            self.down[0] = right[::-1]
        else:
            for i in range(3):
                self.left[i][2] = self.up[2][2 - i]
                self.right[i][0] = self.down[0][2 - i]
            self.up[2] = right
            self.down[0] = left

    def rotate_back(self, clock: bool) -> None:
        left, right = [self.left[i][0] for i in range(3)], [
            self.right[i][2] for i in range(3)
        ]
        if clock:
            for i in range(3):
                self.left[i][2] = self.up[2][2 - i]
                self.right[i][0] = self.down[0][2 - i]
            self.up[2] = right
            self.down[0] = left
        else:
            for i in range(3):
                self.left[i][2] = self.down[0][i]
                self.right[i][0] = self.up[2][i]
            self.up[2] = left[::-1]
            self.down[0] = right[::-1]

    def rotate_left(self, clock: bool) -> None:
        front, back = [self.front[i][0] for i in range(3)], [
            self.back[i][2] for i in range(3)
        ]
        if clock:
            for i in range(3):
                self.front[i][0] = self.up[2][i]
                self.back[i][2] = self.down[0][i]
            self.up[2] = back[::-1]
            self.down[0] = front[::-1]
        else:
            for i in range(3):
                self.front[i][0] = self.down[0][2 - i]
                self.back[i][2] = self.up[2][2 - i]
            self.up[2] = front
            self.down[0] = back

    def rotate_right(self, clock: bool) -> None:
        front, back = [self.front[i][2] for i in range(3)], [
            self.back[i][0] for i in range(3)
        ]
        if clock:
            for i in range(3):
                self.front[i][2] = self.down[0][i]
                self.back[i][0] = self.up[2][i]
            self.up[2] = front[::-1]
            self.down[0] = back[::-1]
        else:
            for i in range(3):
                self.front[i][2] = self.up[2][2 - i]
                self.back[i][0] = self.down[0][2 - i]
            self.up[2] = back
            self.down[0] = front


if __name__ == "__main__":
    for _ in range(II()):
        _ = II()
        rubiks_cube = RubiksCube()
        rubiks_cube.rotate(list(input().strip().split()))
        print(rubiks_cube.get_up().strip())
