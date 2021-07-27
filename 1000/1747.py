"""
Title : 소수 & 팰린드롬
Link : https://www.acmicpc.net/problem/1747
"""

# 가장 큰 소수 팰린드롬 1003001 기준으로 찾았으면 더 빨리 가능했을 듯

import sys
input = sys.stdin.readline

def is_pal(m: str) -> bool:
    for i in range(len(m) // 2):
        if m[i] != m[-1 -i]:
            return False
    return True

n = int(input())

is_prime = [True] * (int(1e7))
is_prime[1] = False

idx = 2
while True:
    if is_prime[idx]:
        if idx >= n and is_pal(str(idx)):
            print(idx)
            break
        for i in range(2 * idx, len(is_prime), idx):
            is_prime[i] = False
    idx += 1