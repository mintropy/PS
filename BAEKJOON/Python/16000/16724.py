"""
Title : 피리 부는 사나이
Link : https://www.acmicpc.net/problem/16724
"""

import sys
input = sys.stdin.readline


def solution() -> None:
    N, M = map(int, input().split())
    my_map = [input().strip() for _ in range(N)]
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    directions = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
    
    visited = [[0] * M for _ in range(N)]
    count = 1
    is_final = False
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            is_final = False
            while True:
                if visited[i][j]:
                    if visited[i][j] != count:
                        count_before = visited[i][j]
                        for x in range(N):
                            for y in range(M):
                                if visited[x][y] == count:
                                    visited[x][y] = count_before
                    elif visited[i][j] == count:
                        count += 1
                    is_final = True
                    break
                visited[i][j] = count
                d = directions[my_map[i][j]]
                i, j = i + dx[d], j + dy[d]
    print(count - 1 if is_final else count)
    return None


solution()
