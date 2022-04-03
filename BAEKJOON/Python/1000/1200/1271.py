"""
Title : 엄청난 부자2
Link : https://www.acmicpc.net/problem/1271
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    print(f'{N // M}\n{N % M}')
