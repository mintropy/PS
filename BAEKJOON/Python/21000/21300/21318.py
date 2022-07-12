"""
Title : 피아노 체조
Link : https://www.acmicpc.net/problem/21318
"""

import sys
input = sys.stdin.readline


n = int(input())
music_sheet = [0] + list(map(int, input().split()))

level = [[0, False] for _ in range(n + 1)]
for i in range(1, n):
    if music_sheet[i] > music_sheet[i + 1]:
        level[i][0] += 1
        level[i][1] = True
    level[i][0] += level[i - 1][0]

level[-1][0] = level[-2][0]

for _ in range(int(input())):
    st, end = map(int ,input().split())
    if st == end:
        print(0)
    else:
        st_level = level[st][0]
        end_level = level[end][0]
        ans = end_level - st_level
        if level[st][1]:
            ans += 1
        if level[end][1]:
            ans -= 1
        print(ans)