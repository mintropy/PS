"""
Title : 인싸들의 가위바위보
Link : https://www.acmicpc.net/problem/16986
"""

from itertools import permutations
from sys import stdin

imput = stdin.readline
MIIS = lambda: map(int, input().split())


def find_winner(x: int, y: int) -> bool:
    global sang_sung
    if sang_sung[x][y] == 2:
        return True
    return False


def simulate(JO: tuple, KH: tuple, MH: tuple) -> bool:
    global K, sang_sung
    x, y = 0, 1
    turn = {0: JO, 1: KH, 2: MH}
    wins = [0] * 3
    # JO는 라운드별로 정해진걸 계산하는게 아니라서
    # 몇번째 자신의 차례인지 기준으로 계산해야함
    for r in range(20):
        if find_winner(turn[x][r] - 1, turn[y][r] - 1):
            wins[x] += 1
            if wins[x] == K:
                if x == 0:
                    return True
                return False
            if y == 1:
                x, y = 0, 2
            elif y == 2:
                x, y = 0, 1
        else:
            wins[y] += 1
            if wins[y] == K:
                return False
            if x == 0:
                x, y = 1, 2
            elif x == 1:
                x, y = 0, 2
    return False


if __name__ == "__main__":
    N, K = MIIS()
    sang_sung = [tuple(MIIS()) for _ in range(N)]
    KH = tuple(MIIS())
    MH = tuple(MIIS())
    for perm in permutations(range(N), N):
        if simulate(perm, KH, MH):
            print(1)
            break
    else:
        print(0)
