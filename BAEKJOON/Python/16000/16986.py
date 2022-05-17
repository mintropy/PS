"""
Title : 인싸들의 가위바위보
Link : https://www.acmicpc.net/problem/16986
"""

import sys
imput = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def search(match: int, wins: list, player_x: int, player_y: int) -> bool:
    global N, K, sang_sung, KH, NH
    if match == 20:
        return False
    if player_x == 0:
        y = KH[match] - 1 if player_y == 1 else MH[match] - 1
        possible = set(sang_sung[x][y] for x in range(N))
        if 2 in possible:
            wins[0] += 1
            if wins[0] == K:
                return True
            next_player = 1 if player_y == 2 else 2
            if search(match + 1, wins, 0, next_player):
                return True
            wins[0] -= 1
        if 0 in possible or 1 in possible:
            wins[player_y] += 1
            if wins[player_y] == K:
                return False
            if search(match + 1, wins, 0, player_y):
                return True
            wins[player_y] -= 1
    else:
        x, y = KH[match] - 1, MH[match] - 1
        if find_winner(match, x, y):
            wins[player_x] += 1
            if wins[player_x] == K:
                return False
            if search(match + 1, wins, 0, player_x):
                return True
            wins[player_x] -= 1
        else:
            wins[player_y] += 1
            if wins[player_y] == K:
                return False
            if search(match + 1, wins, 0, player_y):
                return True
            wins[player_y] -= 1


def find_winner(x: int, y: int) -> bool:
    global sang_sung
    if sang_sung[x][y] == 2:
        return True
    return False


if __name__ == "__main__":
    N, K = MIIS()
    sang_sung = [tuple(MIIS()) for _ in range(N)]
    KH = tuple(MIIS())
    MH = tuple(MIIS())
    print(1 if search(0, [0] * 3, 0, 1) else 0)
