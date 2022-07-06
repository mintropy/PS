"""
Title : 사탕 줍기 대회
Link : https://www.acmicpc.net/problem/5721
"""

import sys
input = sys.stdin.readline


while True:
    m, n = map(int, input().split())
    if m == 0:
        break
    candy = [list(map(int, input().split())) for _ in range(m)]
    # dp = [[0] * n for _ in range(m)
    
    if n == 1:
        if m == 1:
            print(candy[0][0])
            continue
        for i in range(2, m):
            candy[i][0] += candy[i - 2][0]
        print(max(candy[-2] + candy[-1]))
        continue
    
    # max_candy = max(candy[0][:2])
    # 각 자리별로 가져갈 수 있는 최대 사탕 저장
    for i in range(m):
        for j in range(n):
            # 첫번째 줄
            if i == 0:
                if j == 0 or j == 1:
                    continue
                elif j == 2:
                    candy[i][j] += candy[i][j - 2]
                else:
                    candy[i][j] += max(candy[i][j-3:j-1])
                # if candy[i][j] > max_candy:
                #     max_candy = candy[i][j]
            # 두번째 줄
            elif i == 1:
                if j == 0 or j == 1:
                    continue
                elif j == 2:
                    candy[i][j] += candy[i][j - 2]
                else:
                    candy[i][j] += max(candy[i][j-3:j-1])
                # if candy[i][j] > max_candy:
                #     max_candy = candy[i][j]
            # 세번째 줄 이하
            else:
                if j == 0 or j == 1:
                    # 세번째 줄일 때
                    if i == 2:
                        candy[i][j] += max(candy[0][-2:])
                    else:
                        candy[i][j] += max(candy[i - 3][-2:] + candy[i - 2][-2:])
                elif j == 2:
                    candy[i][j] += candy[i][j - 2]
                else:
                    candy[i][j] += max(candy[i][j-3:j-1])
                # if candy[i][j] > max_candy:
                #     max_candy = candy[i][j]
    # print(max_candy)
    if m == 1:
        print(max(candy[0][-2:]))
    else:
        print(max(candy[-2][-2:] + candy[-1][-2:]))


'''
Counter Example
2 1
3
4
out : 3
ans : 4
'''