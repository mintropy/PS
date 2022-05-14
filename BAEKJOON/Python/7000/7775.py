"""
Title : 최종 순위
Link : https://www.acmicpc.net/problem/7775
"""

import sys
input = sys.stdin.readline


def solve(n, p, k, d):
    ans = [0] * n
    if d * (d - 1) // 2 > p:
        print("Wrong information")
        return
    if d == 1:
        if n == k:
            if p % k:
                print("Wrong information")
                return
        elif p // k < p % k:
            print("Wrong information")
            return
        else:
            ans[k] = p % k 
        for i in range(k):
            ans[i] = p // k
    else:
        for i in range(d):
            ans[i] = d - i - 1
    ans[0] += p - sum(ans)
    print(*ans, sep="\n")
    return


if __name__ == "__main__":
    n, p, k, d = map(int, input().split())
    solve(n, p, k, d)

'''
5 6 3 1

5 6 4 1

5 6 2 1

5 7 2 1

5 9 2 1

5 6 5 1

5 5 5 1
'''
