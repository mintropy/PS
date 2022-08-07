"""
Title : 제곱 ㄴㄴ 수
Link : https://www.acmicpc.net/problem/1016
"""

from sys import stdin

input = stdin.readline


# 1020ms
if __name__ == "__main__":
    min_val, max_val = map(int, input().split())
    check = [False] * (max_val - min_val + 1)
    ans = max_val - min_val + 1
    for n in range(2, int(max_val**0.5) + 1):
        n_square = n * n
        q = min_val // n_square + 1 if min_val % n_square else min_val // n_square
        q_max = max_val // n_square + 1
        for k in range(q, q_max):
            if not check[n_square * k - min_val]:
                check[n_square * k - min_val] = True
                ans -= 1
    print(ans)


# 280ms
if __name__ == "__main__":
    min_val, max_val = map(int, input().split())
    check = [True] * (max_val - min_val + 1)

    if max_val <= 3:
        print(max_val - min_val)
        exit()
    prime_square = [4]
    max_sqrt = int(max_val**0.5)
    is_prime = [True] * (max_sqrt // 2 + 1)
    for i in range(3, max_sqrt + 1, 2):
        if is_prime[i // 2]:
            i_square = i * i
            prime_square.append(i_square)
            is_prime[i_square // 2 :: i] = [False] * (
                (max_sqrt - i_square + 1) // (2 * i) + 1
            )
    for num in prime_square:
        st = num - min_val % num if min_val % num else 0
        check[st::num] = [False] * len(check[st::num])
    print(check.count(True))
