"""
Title : 좋은수열
Link : https://www.acmicpc.net/problem/2661
"""

from sys import stdin

input = stdin.readline


def search(N: int, seq: str) -> str:
    if not N:
        return seq
    for s in ("1", "2", "3"):
        next_seq = seq + s
        if not is_good_seq(next_seq):
            continue
        if ans := search(N - 1, next_seq):
            return ans
    return ""


def is_good_seq(seq: str) -> bool:
    for l in range(1, len(seq) // 2 + 1):
        left, right = seq[len(seq) - (l * 2) : len(seq) - l], seq[len(seq) - l :]
        if left == right:
            return False
    return True


if __name__ == "__main__":
    N = int(input())
    print(search(N, ""))
