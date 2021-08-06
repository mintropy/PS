"""
Title : 다이아몬드 광산
Link : https://www.acmicpc.net/problem/1028
"""

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
mine = [[int(i) for i in input().strip()] for _ in range(r)]
# 각 칸은 가장 긴 이어진 대각선
# 각각 오른쪽 위>왼쪽 아래, 왼쪽 위>오른쪽 아래로 이어진 대각선
dp = [[[0] * 2 for _ in range(c)] for _  in range(r)]

max_diamond = 0

# 첫줄은 위를 참고할수 없어 1인 경우만 표시
for j in range(c):
    if mine[0][j] == 1:
        dp[0][j] = [1, 1]
        max_diamond = 1

for i in range(1, r):
    for j in range(c):
        # if j - max_diamond < 0 or j + max_diamond >= c:
        #     continue
        if mine[i][j] == 0:
            continue
        # 1인경우 오른쪽, 왼쪽 위 확인
        if j < c - 1:
            if mine[i - 1][j + 1] == 1:
                dp[i][j][0] = dp[i - 1][j + 1][0] + 1
            else:
                dp[i][j][0] = 1
        else:
            dp[i][j][0] = 1
        if j > 0:
            if mine[i - 1][j - 1] == 1:
                dp[i][j][1] = dp[i - 1][j - 1][1] + 1
            else:
                dp[i][j][1] = 1
        else:
            dp[i][j][1] = 1
        
        a, b = dp[i][j]
        if a <= max_diamond or b <= max_diamond:
            continue
        
        if a < b:
            m = a
        else:
            m = b
        
        for k in range(m, max_diamond, -1):
            left_right_up = dp[i - (k - 1)][j - (k - 1)][0]
            right_left_up = dp[i - (k - 1)][j + (k - 1)][1]
            if left_right_up >= k and right_left_up >= k:
                max_diamond = k
                break
        
        '''
        # 대각선 반대로 올라가면서 확인
        min_diagonal = min(dp[i][j])
        if min_diagonal <= max_diamond:
            continue
        # 최대한 가는 칸 부터 하나씩 줄여가며 실행
        for k in range(min_diagonal, max_diamond, -1):
            left_right_up = dp[i - (k - 1)][j - (k - 1)][0]
            right_left_up = dp[i - (k - 1)][j + (k - 1)][1]
            if left_right_up >= k and right_left_up >= k:
                max_diamond = k
                break
        '''


print(max_diamond)