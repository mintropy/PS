"""
Title : 알파 틱택토
Link : https://www.acmicpc.net/problem/16571
"""

import sys
input = sys.stdin.readline


def search(TIK_TAK_TOE: list, turn: int, count: int, target_player: int) -> str:
    if not count:
        return "D"
    result = is_tik_tak_toe(TIK_TAK_TOE)
    if result:
        if result == target_player:
            return "W"
        else:
            return "L"
    next_turn = 1 if turn == 2 else 2
    best_result = "L"
    for i in range(3):
        for j in range(3):
            if not TIK_TAK_TOE[i][j]:
                TIK_TAK_TOE[i][j] = turn
                result = search(TIK_TAK_TOE, next_turn, count - 1, target_player)
                if result == "W":
                    return result
                if result == "D":
                    best_result = result
                TIK_TAK_TOE[i][j] = 0
    return best_result


def is_tik_tak_toe(TIK_TAK_TOE) -> int:
    if [1, 1, 1] in TIK_TAK_TOE:
        return 1
    if [2, 2, 2] in TIK_TAK_TOE:
        return 2
    for i in range(3):
        if (
            TIK_TAK_TOE[0][i] == 1
            and TIK_TAK_TOE[1][i] == 1
            and TIK_TAK_TOE[2][i] == 1
        ):
            return 1
        if (
            TIK_TAK_TOE[0][i] == 2
            and TIK_TAK_TOE[1][i] == 2
            and TIK_TAK_TOE[2][i] == 2
        ):
            return 2
    return 0


if __name__ == "__main__":
    TIK_TAK_TOE = [list(map(int, input().split())) for _ in range(3)]
    zero_count = sum([l.count(0) for l in TIK_TAK_TOE])
    turn = 1 if zero_count % 2 else 2
    status = {0: "D", 1: "W", 2: "L"}
