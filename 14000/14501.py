'''
Title : 퇴사
Link : https://www.acmicpc.net/problem/14501
'''

# 브루트포스

import sys

input = sys.stdin.readline

def search(day, wage):
    global n, schedule, max_wage
    for i in range(day, n):
        next_day = i + schedule[i][0]
        next_wage = wage + schedule[i][1]
        if next_day == n:
            if next_wage >= max_wage:
                max_wage = next_wage
        elif next_day > n:
            if wage >= max_wage:
                max_wage = wage
        else:
            search(next_day, next_wage)


n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
max_wage = 0
search(0, 0)
print(max_wage)