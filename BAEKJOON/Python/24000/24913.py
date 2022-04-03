"""
Title : 개표
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ =="__main__":
    N, Q = MIIS()
    votes = [0] * (N + 2)
    max_vote = 0
    for _ in range(Q):
        q_type, a, b = MIIS()
        if q_type == 1:
            votes[b] += a
            if b == N + 1:
                continue
            if max_vote < votes[b]:
                max_vote = votes[b]
        else:
            if votes[N + 1] + a >= max_vote + b:
                print("YES")
            else:
                print("NO")

'''
1 5
1 5 1
1 3 2
1 3 2
2 1 2
2 0 2
'''
