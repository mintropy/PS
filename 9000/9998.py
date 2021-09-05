"""
Title : 블록 쌓기
Link : https://www.acmicpc.net/problem/9998
"""

import sys
input = sys.stdin.readline

n = int(input())
yoon = list(map(int, input().split()))
dong = list(map(int, input().split()))

ans = [0] * n
ans[n // 2] = (yoon[n // 2] + dong[n // 2]) // 2
action = abs(ans[n // 2] - yoon[n // 2]) + abs(ans[n // 2] - dong[n // 2])

for i in range(1, n // 2 + 1):
    # 왼쪽
    left = (yoon[n // 2 - i] + dong[n // 2 - i]) // 2
    if left <= ans[n // 2 - i + 1]:
        ans[n // 2 - i] = ans[n // 2 - i + 1] + 1
    else:
        ans[n // 2 - i] = left
    action += abs(ans[n // 2 - i] - yoon[n // 2 - i]) + abs(ans[n // 2 - i] - dong[n // 2 - i])
    # 오른쪽
    right = (yoon[n // 2 + i] + dong[n // 2 + i]) // 2
    if right <= ans[n // 2 + i - 1]:
        ans[n // 2 + i] = ans[n // 2 + i - 1] + 1
    else:
        ans[n // 2 + i] = right
    action += abs(ans[n // 2 - i] - yoon[n // 2 + i]) + abs(ans[n // 2 - i] - dong[n // 2 + i])

print(action)


'''
Counter Example
5
3 2 5 2 3
3 2 4 2 3
ans : 7

5
3 2 5 8 15
3 2 5 8 15


'''