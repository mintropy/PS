"""
Title : 알프수
Link : 
"""

import sys
input = sys.stdin.readline


def check_alpsoo(X: list[int]) -> str:
    if X[0] >= X[1] or X[-2] <= X[-1]:
        return 'NON ALPSOO'
    ascending = True
    slope = X[1] - X[0]
    for i in range(2, len(X) - 1):
        if X[i] == X[i - 1]:
            return 'NON ALPSOO'
        is_ascending = True if X[i] > X[i - 1] else False
        if ascending != is_ascending:
            ascending = is_ascending
            slope = X[i] - X[i - 1]
        else:
            if slope != X[i] - X[i - 1]:
                return 'NON ALPSOO'
    return 'ALPSOO'


X = list(int(x) for x in input().strip())
print(check_alpsoo(X))
