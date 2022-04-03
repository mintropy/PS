import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))

# test case 
t = int(input())

def dfs(m: int):
    global n, tf, a, b
    if m == n:
        tf = True
        return
    if m < m * a < n:
        dfs(m * a)
    if m + b < n:
        dfs(m + b)


for _ in range(t):
    n, a, b = map(int, input().split())
    tf = False
    dfs(1)
    if tf:
        print("Yes")
    else:
        print("No")