"""
Title : 카카오머니
Link : https://www.acmicpc.net/problem/15998
"""

from math import gcd
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    logs = [tuple(map(int, input().split())) for _ in range(N)]
    auto_deposit = []
    if logs[0][0] < 0:
        auto_deposit.append(sum(logs[0]))
    for i in range(1, N):
        if logs[i][0] > 0 or logs[i - 1][1] + logs[i][0] >= 0:
            continue
        auto_deposit.append(logs[i][1] + -logs[i][0] - logs[i - 1][1])
    if len(auto_deposit) <= 1:
        print(1)
    else:
        g = gcd(*auto_deposit)
        if g == 1:
            for a, b in logs:
                if a < 0 and b:
                    print(-1)
                    break
            else:
                print(1)
        else:
            print(g)

'''
2
-5 0
-6 0
# 1

2
1500 1500
-300 1200
# 1

3
1500 1500
-1600 1200
-400 0
# -1

'''
