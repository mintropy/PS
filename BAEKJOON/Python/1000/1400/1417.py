"""
Title : 국회의원 선거
Link : https://www.acmicpc.net/problem/1417
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())

if __name__ == "__main__":
    N = II()
    dasom = II()
    votes = [0] * 101
    for _ in range(N - 1):
        v = II()
        votes[v] += 1
    answer = 0
    for i in range(100, 0, -1):
        if not votes[i]:
            continue
        while votes[i]:
            if dasom > i:
                break
            dasom += 1
            votes[i] -= 1
            votes[i - 1] += 1
            answer += 1
        if (not votes[i] and dasom >= i) or dasom > i:
            break
    print(answer)
