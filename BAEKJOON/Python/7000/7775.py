"""
Title : 최종 순위
Link : https://www.acmicpc.net/problem/7775
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, p, k, d = map(int, input().split())
    if (d * (d + 1)) // 2 + (k - d) > p:
        print("Wrong information")
    else:
        ans = [0] * n
        for i in range(d):
            ans[i] = d - i
        for j in range(d, k):
            ans[i] = 1
        ans[0] += p - sum(ans)
        print(*ans, sep="\n")
