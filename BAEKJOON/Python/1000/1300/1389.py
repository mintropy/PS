"""
Title : 케빈 베이컨의 6단계 법칙
Link : https://www.acmicpc.net/problem/1389
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    friends = [[0] * N for _ in range(N)]
    for _ in range(M):
        a, b = MIIS()
        friends[a - 1][b - 1] = 1
        friends[b - 1][a - 1] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if not friends[i][k] or not friends[k][j]:
                    continue
                t = friends[i][k] + friends[k][j]
                if friends[i][j] and friends[i][j] <= t:
                    continue
                friends[i][j] = t
                friends[j][i] = t
    ans = [(sum(friends[i]), i + 1) for i in range(N)]
    ans.sort()
    print(ans[0][1])

"""
5 6
1 3
1 3
1 4
4 5
4 3
3 2
ans : 3

5 4
3 1
2 3
1 4
5 2
ans : 3
"""
