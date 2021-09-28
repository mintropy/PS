"""
Title : 핑거 스냅
Link : https://www.acmicpc.net/problem/17394
"""

import bisect
import collections
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

is_prime = [True] * 100_001
is_prime[0] = is_prime[1] = False
primes = []
for i in range(2, 100_001):
    if is_prime[i]:
        primes.append(i)
        for j in range(2 * i, 100_001, i):
            is_prime[j] = False


for _ in range(int(input())):
    n, a, b = MIIS()
    # a와 b사이 소수
    prob_primes = []
    for i in range(bisect.bisect_left(primes, a), len(primes)):
        if a <= primes[i] <= b:
            prob_primes.append(primes[i])
        else:
            break
    
    # a, b 사이 소수가 없는 경우
    if not prob_primes:
        print(-1)
        continue
    # a보다 작으면 생명체를 늘리는 핑거스넵
    elif n <= a:
        print(prob_primes[0] - n)
        continue
    
    queue = collections.deque([(n, 0)])
    visited = [False] * (2_000_000 + 1)
    min_finger_snap = n
    while queue:
        m, finger_sanp = queue.popleft()
        # 지금 핑거스냅으로 완료된 경우
        if m in prob_primes:
            min_finger_snap = finger_sanp
            break
        # 이미 확인한 생명체 수 인 경우
        if visited[m]:
            continue
        visited[m] = True
        # 생명체 수가 a보다 작으면, 값 비교 후 continue
        if m < a:
            if min_finger_snap < finger_sanp + (prob_primes[0] - m):
                min_finger_snap = finger_sanp + (prob_primes[0] - m)
            continue
        else:
            if not visited[m // 2]:
                queue.append((m // 2, finger_sanp + 1))
            if not visited[m // 3]:
                queue.append((m // 3, finger_sanp + 1))
            if m + 1 < len(visited) and not visited[m + 1]:
                queue.append((m + 1, finger_sanp + 1))
            if n > 0 and not visited[m - 1]:
                queue.append((m - 1, finger_sanp + 1))
    print(min_finger_snap)
