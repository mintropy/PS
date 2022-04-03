"""
Title : 동전 문제
Link : https://www.acmicpc.net/problem/1398
"""

import sys
input = sys.stdin.readline

coins = [10 ** i for i in range(16)] + [25 * (100 ** i) for i in range(7)]
coins.sort(key=lambda x:-x)

# 0 ~ 100일때 최소 비용
costs = [100] * 101
costs[0] = 0
# 10의 배수일 때
for i in range(1, 11):
    costs[i * 10] = i
# 25의 배수일 때
for i in range(1, 5):
    costs[i * 25] = i
    # 추가적 10의 배수 더할 때
    for j in range(1, 10):
        if i * 25 + j * 10 > 100:
            break
        costs[i * 25 + j * 10] = i + j
# 나머지 값
for i in range(1, 100):
    if costs[i - 1] + 1 < costs[i]:
        costs[i] = costs[i - 1] + 1

for _ in range(int(input())):
    # 2자리씩 계산
    n = input().strip()
    n = n.zfill((len(n) // 2 + 1) * 2)
    
    total_count = 0
    for i in range(len(n) // 2):
        m = n[i * 2:(i + 1) * 2]
        total_count += costs[int(m)]
    print(total_count)
