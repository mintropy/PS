"""
Title : 박 터트리기
Link : https://www.acmicpc.net/problem/19939
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N, K = map(int, input().split())
    if (K * (K + 1)) // 2 <= N:
        N -= (K * (K + 1)) // 2
        N %= K
        print(K if N else K - 1)
    else:
        print(-1)

"""
7 3
ans : 3

8 3
ans : 3
"""
