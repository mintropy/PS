"""
Title : 파티가 끝나고 난 뒤
Link : https://www.acmicpc.net/problem/2845
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    L, P = MIIS()
    people_count = list(MIIS())
    participant = P * L
    print(*[count - participant for count in people_count])
