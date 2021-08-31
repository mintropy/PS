"""
Title : 종점
Link : https://www.acmicpc.net/problem/22867
"""

import sys
input = sys.stdin.readline


def check(leave_last: str, next_start: str) -> bool:
    # 시, 분, 초, 밀리초 순서로 탐색
    # idx : :2, 3:5, 6:8, 9:
    if next_start[:2] < leave_last[:2]:
        return False
    elif next_start[3:5] < leave_last[3:5]:
        return False
    elif next_start[6:8] < leave_last[6:8]:
        return False
    elif next_start[9:] < leave_last[9:]:
        return False
    return True


n = int(input())
# HH:MM:SS.sss
schedule = sorted(list(tuple(input().strip().split()) for _ in range(n)), key=lambda x: x[1])

count = 1
train_leave = schedule[0][1]

for i in range(1, n):
    st, end = schedule[i]
    if check(train_leave, st):
        train_leave = end
    else:
        count += 1

print(count)
