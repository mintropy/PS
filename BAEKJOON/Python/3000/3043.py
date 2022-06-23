"""
Title : 장난감 탱크
Link : https://www.acmicpc.net/problem/3043
"""

from sys import stdin

input = stdin.readline


def find_moves(N: int, board: dict, cmds: tuple):
    global ans
    for i in range(1, N):
        if len(board[i]) < 2:
            break
        for j in range(i + 2, N):
            if board[j]:
                continue
            for k in range(j - 1, i, -1):
                while board[k]:
                    x = board[k].pop()
                    board[k + 1].append(x)
                    ans.append((x, cmds[1]))
            while len(board[i]) > 1:
                x = board[i].pop()
                board[i + 1].append(x)
                ans.append((x, cmds[1]))
            break
    for i in range(1, N):
        if board[i]:
            continue
        for j in range(i + 1, N + 1):
            if not board[j]:
                continue
            x = board[j].pop()
            ans += [(x, cmds[0]) for _ in range(j - i)]
            board[i].append(x)
            break
    for i in range(N, 1, -1):
        if board[i]:
            continue
        for j in range(i - 1, 0, -1):
            if not board[j]:
                continue
            x = board[j].pop()
            ans += [(x, cmds[1]) for _ in range(i - j)]
            board[i].append(x)
            break


def make_output(ans: list) -> str:
    output = f"{len(ans)}\n"
    for x, cmd in ans:
        output += f"{x} {cmd}\n"
    return output


if __name__ == "__main__":
    N = int(input())
    board_rows = {i: [] for i in range(1, N + 1)}
    board_columns = {i: [] for i in range(1, N + 1)}
    for i in range(N):
        x, y = map(int, input().split())
        board_rows[x].append(i + 1)
        board_columns[y].append(i + 1)
    ans = []
    find_moves(N, board_rows, ("U", "D"))
    find_moves(N, board_columns, ("L", "R"))
    print(make_output(ans))


"""
상근이, 장난감 탱크 N개, 전장 N행 N열
    탱크, 한 번에 인접한 네 칸으로 이동
    같은 행, 열의 모든 칸을 공격 가능
    두 탱크가 같은 정사각형 ㄴㄴ
각 행, 열에 하나의 탱크만 있도록 배치 바꾸기 & 최소 이동 횟수
"""
