"""
Title : 소수인팰린드롬
Link : https://www.acmicpc.net/problem/1990
"""

def is_prime_num(num: int, primes: list) -> bool:
    for prime in primes:
        if prime * prime > num:
            return True
        if num % prime == 0:
            return False
    return True


def is_pal(num: str) -> bool:
    if str(num) == str(num)[::-1]:
        return True
    return False


a, b = map(int, input().split())
b = min(b, 10 ** 8)

is_prime = [True] * (int(b ** 0.5) + 1)
primes = []
for i in range(2, int(b ** 0.5) + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, int(b ** 0.5) + 1, i):
            is_prime[j] = False

# 10 ** 8 ~ 10 ** 9사이 소수 팰린드롬 없음
if a <= 2 <= b:
    print(2)

if a <= 2:
    a = 3
elif a % 2 == 0:
    a += 1

for num in range(a, b + 1, 2):
    if is_prime_num(num, primes) and is_pal(str(num)):
        print(num)
else:
    print(-1)
