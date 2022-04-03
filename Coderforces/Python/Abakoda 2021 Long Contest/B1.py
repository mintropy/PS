import sys
input = sys.stdin.readline


n = int(input())
dist = sorted(map(int, input().split()), reverse=True)
skills = sorted(map(int, input().split()), reverse=True)

while dist:
    if skills[-1] >= dist[-1]:
        skills.pop()
        dist.pop()
    else:
        break

if dist:
    print('NO')
else:
    print('YES')
