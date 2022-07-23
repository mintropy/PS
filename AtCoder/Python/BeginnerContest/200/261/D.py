import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
counter = tuple(map(int, input().split()))
bonus = {}
for _ in range(M):
    c, y = map(int, input().split())
    bonus[c] = y


def dfs(turn, money, streak):
    global N, counter, bonus, ans
    if turn == N:
        if ans < money:
            ans = money
        return
    _money = money + counter[turn]
    if streak + 1 in bonus:
        _money += bonus[streak + 1]
    dfs(turn + 1, _money, streak + 1)
    dfs(turn + 1, money, 0)


ans = 0
dfs(0, 0, 0)
print(ans)
