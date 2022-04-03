"""
Title : 하얀 칸
Link : https://www.acmicpc.net/problem/1100
"""

cnt = 0

for i in range(1, 8 + 1):
    chess = list(input())
    if i % 2 == 0:
        white = 1
    else:
        white = 0
    
    for j in range(white, 8, 2):
        if chess[j] == 'F':
            cnt += 1

print(cnt)