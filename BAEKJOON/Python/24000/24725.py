"""
Title : 엠비티아이
Link : 
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    boards = [input().strip() for _ in range(N)]
    
    dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
    MBTI_count = 0
    check = {
        0: 'NS', 1: 'FT', 2: 'PJ'
    }
    for i in range(N):
        for j in range(M):
            if boards[i][j] not in 'EI':
                continue
            for d in range(8):
                x, y = i + dx[d], j + dy[d]
                for k in range(3):
                    if x < 0 or x >= N or y < 0 or y >= M:
                        break
                    if boards[x][y] not in check[k]:
                        break
                    x, y = x + dx[d], y + dy[d]
                else:
                    MBTI_count += 1
    print(MBTI_count)
