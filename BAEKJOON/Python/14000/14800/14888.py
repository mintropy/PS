import sys

input = lambda : sys.stdin.readline()
INF = sys.maxsize

# 연산 수행
def operation(x, y, i):
    if i == 0:
        return x + y
    elif i == 1:
        return x - y
    elif i == 2:
        return x * y
    elif i == 3:
        if x >= 0:
            return x // y
        else:
            return -1 * ((-1 * x) // y)

# dfs로 탐색
def dfs(result, idx):
    global n, seq, command, max_result, min_result
    if idx == n:
        if result > max_result:
            max_result = result
        if result < min_result:
            min_result = result
        return
    for i in range(4):
        if command[i] != 0:
            command[i] -= 1
            dfs(operation(result, seq[idx], i), idx + 1)
            command[i] += 1


n = int(input())
seq = list(map(int, input().split()))
command = list(map(int, input().split()))

# 최댓값, 최솟값 저장
max_result = -1 * INF
min_result = INF

dfs(seq[0], 1)
print(max_result)
print(min_result)