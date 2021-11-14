"""
Title : 회사에 있는 사람
Link : https://www.acmicpc.net/problem/7785
"""

import sys
input = sys.stdin.readline


N = int(input())

slaves = set()
for _ in range(N):
    slave, cmd = input().strip().split()
    if cmd == 'enter':
        slaves.add(slave)
    else:
        slaves.remove(slave)

print(*sorted(slaves, reverse=True), sep='\n')
