"""
Title : 소수 경로
Link : https://www.acmicpc.net/problem/1963
"""

import sys, collections
input = sys.stdin.readline


is_prime = [True for _ in range(10000)]
is_prime[1] = False
for i in range(2, 10000):
    if is_prime[i]:
        for j in range(2 * i, 10000, i):
            is_prime[j] = False


for _ in range(int(input())):
    p, q = map(int, input().split())
    visited = [False] * (10000)
    visited[p] = True
    queue = collections.deque([(p, 0)])
    while queue:
        p2, count = queue.popleft()
        if p2 == q:
            print(count)
            break
        # 각 자리수를 바꿔가며 확인
        # 0. 바꾼 수가 q면 종료
        # 1. 각 자리를 바꿨을 때 소수인지 확인
        # 2. 소수이고, 사용하지 않았다면 queue에 추가
        # 천의 자리수부터 시작
        for i in range(1, 10):
            p3 = i * 1000 + p2 % 1000
            if not is_prime[p3]:
                continue
            if visited[p3]:
                continue
            queue.append((p3, count + 1))
            visited[p3] = True
        # 백의 자리수
        for i in range(10):
            p3 = (p2 // 1000) * 1000 + i * 100 + p2 % 100
            if not is_prime[p3]:
                continue
            if visited[p3]:
                continue
            queue.append((p3, count + 1))
            visited[p3] = True
        # 십의 자리수
        for i in range(10):
            p3 = (p2 // 100) * 100 + i * 10 + p2 % 10
            if not is_prime[p3]:
                continue
            if visited[p3]:
                continue
            queue.append((p3, count + 1))
            visited[p3] = True
        # 일의 자리수
        for i in range(10):
            p3 = (p2 // 10) * 10 + i
            if not is_prime[p3]:
                continue
            if visited[p3]:
                continue
            queue.append((p3, count + 1))
            visited[p3] = True