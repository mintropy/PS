"""
Title : 좋은 수
Link : https://www.acmicpc.net/problem/1060
"""

import sys
input = sys.stdin.readline


if __name__ == '__main__':
    L = int(input())
    nums = sorted(map(int, input().split()))
    N = int(input())
    
    ans = [nums] + [0] * (N - L)
    for i in range(L - 1):
        diff = ans[i + 1] - ans[i]
        if diff == 1:
            pass
