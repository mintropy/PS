"""
Title : 1은 흥미로운 숫자
Link : https://www.acmicpc.net/problem/4530
"""

import sys, math
input = sys.stdin.readline


def positional_sum(m):
    total = 0
    while m:
        total += m % 10
        m //= 10
    return total


def positional_product(m):
    total = 1
    while m:
        total *= m % 10
        m //= 10
    return total


is_prime = [True] * (1_000_001)
is_prime[1] = False
for i in range(2, 1_000_001):
    if is_prime[i]:
        for j in range(i * 2, 1_000_001, i):
            is_prime[j] = False


for i in range(1, int(input()) + 1):
    n = int(input())
    s = list(int(input()) for _ in range(n))
    
    interests = {}
    # 각 숫자별로 확인
    for j in range(n):
        m = s[j]
        counts = [0] * 13
        # 개별 특성 먼저 확인
        # 1. 소수
        if is_prime[m]:
            counts[0] =  1
        # 2. 제곱수
        if int(math.log2(m)) ** 2 == m:
            counts[1] =  1
        # 3. 세제곱수
        if int(math.log(m, 3)) ** 3 == m:
            counts[2] =  1
        # 4. 네제곱수
        if int(math.log(m, 4)) ** 2 == m:
            counts[3] =  1
        # 5. 합배수
        if positional_sum(m) == m:
            counts[4] =  1
        # 6. 곱배수
        if positional_product(m) == m:
            counts[5] =  1
        # 다른 숫자들과 확인
        for k in range(n):
            if all(counts[6:]):
                break
            if j == k:
                continue
            # 7. 약수
            if not s[k] % m:
                counts[6] = 1
            # 8. 배수
            if not m % s[k]:
                counts[7] = 1
            # 9. 사과제곱수
            if m == s[k] ** 2:
                counts[8] = 1
            # 10. 사과세제곱수
            if m == s[k] ** 3:
                counts[9] = 1
            # 11. 사과네제곱수
            if m == s[k] ** 4:
                counts[10] = 1
            # 12. 사과합배수
            if not m % positional_sum(s[k]):
                counts[11] = 1
            # 13. 사과곱배수
            if positional_product(s[k]) and not m % positional_product(s[k]):
                counts[12] = 1
        ins = sum(counts)
        if ins in interests:
            interests[ins].add(m)
        else:
            interests[ins] = {m}
    
    print(f'DATA SET #{i}')
    print(*sorted(interests[max(interests.keys())]), sep='\n')
