"""
Title : 경사로
Link : https://www.acmicpc.net/problem/14890
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def solve(N: int, L: int, my_map: list[list[int]]) -> int:
    ans = 0
    for i in range(N):
        col = [my_map[i][0]] + my_map[i] + [my_map[i][-1]]
        row = [my_map[0][i]] + [my_map[x][i] for x in range(N)] + [my_map[-1][i]]
        if search(N, L, col):
            ans += 1
        if search(N, L, row):
            ans += 1
    return ans


def search(N: int, L: int, line: list[int]) -> bool:
    i = 1
    check = [False] * (N + 2)
    while i <= N:
        if line[i] == line[i + 1]:
            i += 1
            continue
        if line[i] == line[i + 1] + 1:
            if i + L > N:
                return False
            for j in range(i + 2, i + L + 1):
                if line[j] == line[i + 1]:
                    continue
                return False
            for j in range(i + 1, i + L + 1):
                check[j] = True
            i += L
        elif line[i] == line[i + 1] - 1:
            if i < L:
                return False
            if check[i]:
                return False
            for j in range(i - 1, i - L, -1):
                if check[j] or line[j] != line[i - 1]:
                    return False
            for j in range(i, i - L, -1):
                check[j] = True
            i += 1
        else:
            return False
    return True


if __name__ == "__main__":
    N, L = MIIS()
    my_map = [list(MIIS()) for _ in range(N)]
    print(solve(N, L, my_map))
