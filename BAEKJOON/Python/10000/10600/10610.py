"""
Title : 30
Link : https://www.acmicpc.net/problem/10610
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = list(input().strip())
    nums = [0] * 10
    for x in N:
        nums[int(x)] += 1
    if not nums[0] or sum([x * i for i, x in enumerate(nums)]) % 3:
        print(-1)
    else:
        ans = ""
        for i in range(9, -1, -1):
            ans += f"{i}" * nums[i]
        print(ans)
