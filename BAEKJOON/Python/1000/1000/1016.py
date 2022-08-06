"""
Title : 제곱 ㄴㄴ 수
Link : https://www.acmicpc.net/problem/1016
"""

from sys import stdin

input = stdin.readline


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
