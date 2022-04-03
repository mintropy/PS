# WA

import sys
input = sys.stdin.readline


n = int(input())
dist = sorted(map(int, input().split()))
skills = sorted(map(int, input().split()))

ans = 1
while dist:
    group = 0
    max_dist = dist[-1]
    while skills:
        if skills[-1] >= max_dist:
            group += 1
            dist.pop()
            skills.pop()
        else:
            break
    ans *= group
    if group == 0:
        break

print(ans)

'''
5
10 15 20 25 30
21 21 21 26 30
'''
