"""
Title : 소용돌이 예쁘게 출력하기
Link : https://www.acmicpc.net/problem/1022
"""

r1, c1, r2, c2 = map(int, input().split())

diagonal = [[1] for _ in range(4)]
max_grid = max((r1, r2, c1, c2))
# 0, 0 기준 오른쪽 위, 왼쪽 위, 왼쪽 아래, 오른쪽 아래
diagonal[0].append(3)
diagonal[1].append(5)
diagonal[2].append(7)
diagonal[3].append(9)
for _ in range(1, max_grid + 1):
    for i in range(4):
        diagonal[i].append(diagonal[i][-1] + (diagonal[i][-1] - diagonal[i][-2]) + 8)

grid = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
# 가장 윗 줄부터 한줄씩 채우기

