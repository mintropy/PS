"""
Title : S를 T로
Link : https://www.acmicpc.net/problem/3806
"""

from collections import defaultdict
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    for _ in range(int(input())):
        S = input().strip()
        T = input().strip()
        changes = defaultdict(int)
        for idx, s in enumerate(S):
            if s != T[idx]:
                changes[(s, T[idx])] += 1
