"""
Title : 컬러볼
Link : https://www.acmicpc.net/problem/10800
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    balls = [tuple(map(int, input().split())) for _ in range(N)]


N = int(input())
balls = [list(map(int, input().split())) + [i] for i in range(N)]
balls.sort(key=lambda x:x[1])
ans = []

check_color = [0] * (N + 1)
prefix_sum = 0
last_score = -1
last_color = -1
continuous = 0
for c, s, _ in balls:
    if c == last_color:
        ans.append(prefix_sum - check_color[c])
    elif s == last_score:
        ans.append(prefix_sum - check_color[c] - continuous * s)
    else:
        ans.append(prefix_sum - check_color[c])
    prefix_sum += s
    check_color[c] += s
    last_color = c
    if last_score == s:
        continuous += 1
    else:
        last_score = s
        continuous = 0

sorted_ans = [0] * N
for i, (*_, j) in enumerate(balls):
    sorted_ans[j] = ans[i]

print(*sorted_ans, sep='\n')
