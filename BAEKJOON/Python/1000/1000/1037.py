import sys

input = lambda : sys.stdin.readline()

def is_prime(k):
    prime = [True] * (k + 1)
    prime[0], prime[1] = False, False
    for i in range(2, int(k**0.5) + 1):
        if prime[i]:
            for j in range(2*i, k + 1, i):
                prime[j] = False
    # 소수가 담기는 리스트
    p = []
    for i in range(k + 1):
        if prime[i]:
            p.append(i)
    return p

def find(divisor, prime):
    # 거듭제곱 형태인지 확인
    p = min(divisor)
    is_power = True
    for i in range(len(divisor) - 1):
        if divisor[i] % p != 0:
            is_power = False
            break
    if is_power:
        return max(divisor) * p
    # 거듭제곱이 아닌 경우 확인
    prime_count = [0] * len(prime)
    for x in divisor:
        for i in range(len(prime)):
            p = prime[i]
            if x == 1:
                break
            t = 0
            while True:
                if x % p == 0:
                    t += 1
                    x //= p
                else:
                    break
            if prime_count[i] < t:
                prime_count[i] = t
    ans = 1
    for i in range(len(prime)):
        if prime_count[i] != 0:
            ans *= prime[i] ** prime_count[i]
    return ans

n = int(input())
divisor = list(map(int, input().split()))

# 구하는 정수의 소수인 약수
prime = is_prime(max(divisor))
# 출력
print(find(divisor, prime))
