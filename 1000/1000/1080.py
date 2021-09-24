"""
Title : 행렬
Link : https://www.acmicpc.net/problem/1080
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def search(n: int, m: int, diff: list) -> int:
    count = 0 
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            # i, j 가 n - 1, m - 1이면 왼쪽 3개, 위 3개 확인
            # i, j 가 n - 2, m - 2이면 왼쪽-위에서 2개, 위-오른쪽에서 2개 확인
            # 아니라면 왼쪽 위 하나만 확인
            check = set()
            if i == n - 1:
                check.update(((i, j - 1), (i + 1, j - 1)))
            elif i == n - 2:
                check.add((i, j - 1))
            if j == n - 1:
                check.update(((i - 1, j), (i - 1, j + 1)))
            elif j == n - 2:
                check.add((i - 1, j))
            # check의 모든 칸을 확인, 뒤집어야 하는지
            pos = diff[i - 1][j - 1]
            for i, j in check:
                if diff[i][j] != pos:
                    return -1
            # 해당 범위 모든 칸 뒤집기
            if pos == 1:
                for a in range(i - 1, i + 2):
                    for b in range(j - 1, j + 2):
                        if diff[a][b]:
                            diff[a][b] = 0
                        else:
                            diff[a][b] = 1
                # 횟수 증가
                count += 1
    return count 


n, m = MIIS()
A = [list(int(i) for i in input().strip()) for _ in range(n)]
B = [list(int(i) for i in input().strip()) for _ in range(n)]

# 두 행렬 각 자리의 차이
diff = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            diff[i][j] = 1

print(search(n, m, diff))
