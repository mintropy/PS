'''
Title : 숫자 정사각형
Link : https://www.acmicpc.net/problem/1051
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [[int(i) for i in input().strip()] for _ in range(n)]
max_rectangle = 1

for i in range(n - 1):
    for j in range(m - 1):
        # 왼쪽 위 기준점
        num = numbers[i][j]
        for k in range(j + 1, m):
            # 기준점에서 오른쪽으로 같은 수가 있는지
            # 없으면 넘어감
            if numbers[i][k] != num:
                continue
            # 밑으로 탐색 불가능할때
            if i + (k - j) >= n:
                break
            # 있으면 밑으로도 찾아보기
            if numbers[i + (k - j)][j] == num and numbers[i + (k - j)][k] == num:
                max_rectangle = max(max_rectangle, (k - j + 1) ** 2)

print(max_rectangle)