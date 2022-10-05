"""
Title : 히스토그램
Link : https://www.acmicpc.net/problem/1725
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())

if __name__ == "__main__":
    N = II()
    histogram = [0] + [II() for _ in range(N)] + [0]
    stack = [0]
    ans = 0
    for i in range(1, N + 2):
        while stack and histogram[stack[-1]] > histogram[i]:
            h = stack.pop()
            ans = max(ans, histogram[h] * (i - stack[-1] - 1))
        stack.append(i)
    print(ans)
