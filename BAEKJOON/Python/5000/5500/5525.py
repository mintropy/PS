"""
Title : IOIOI
Link : https://www.acmicpc.net/problem/5525
"""

from sys import stdin

input = stdin.readline


def get_count(N: int, left: int, right: int) -> int:
    o_count = (right - left) // 2
    if o_count < N:
        return 0
    return o_count - N + 1


if __name__ == "__main__":
    n, m = int(input()), int(input())
    s = str(input().strip())

    count = 0
    left, right = -1, -1
    idx = 0
    while True:
        if idx == m:
            count += get_count(n, left, right)
            break
        if left == right:
            if s[idx] == "I":
                left = idx
            idx += 1
        else:
            if idx == m - 1:
                idx += 1
            elif s[idx : idx + 2] == "OI":
                right = idx + 1
                idx += 2
            else:
                count += get_count(n, left, right)
                left = right = idx - 1
    print(count)
