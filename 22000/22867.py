"""
Title : 종점
Link : https://www.acmicpc.net/problem/22867
"""

import sys
input = sys.stdin.readline


def check(leave_last: str, next_start: str) -> bool:
    # 시, 분, 초, 밀리초 순서로 탐색
    # idx : :2, 3:5, 6:8, 9:
    if int(next_start[:2]) < int(leave_last[:2]):
        return False
    elif int(next_start[3:5]) < int(leave_last[3:5]):
        return False
    elif int(next_start[6:8]) < int(leave_last[6:8]):
        return False
    elif int(next_start[9:]) < int(leave_last[9:]):
        return False
    return True


n = int(input())
# HH:MM:SS.sss
schedule = []
for _ in range(n):
    arrival, leave = input().strip().split()
    arrival = arrival.replace(':', '')
    arrival = arrival.replace('.', '')
    leave = leave.replace(':', '')
    leave = leave.replace('.', '')
    arrival, leave = int(arrival), int(leave)
    schedule.append((arrival, leave))
    if leave < arrival:
        schedule.append((0, leave))

schedule.sort()
max_area = 1
for i in range(n):
    if i + max_area >= n:
        break
    for j in range(i + 1, n):
        if schedule[j][0] > schedule[i][1]:
            break
    if max_area < j - i:
        max_area = j - i

print(max_area)
