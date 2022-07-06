"""
Title : 1, 2, 3 더하기 2
Link : https://www.acmicpc.net/problem/12101
"""


def dfs(nums: list, sum: int):
    global n, k, count
    if sum == n:
        count += 1
        if count  == k:
            print('+'.join(map(str, nums)))
            exit()
        return
    for i in range(1, min([4, n - sum + 1])):
        nums.append(i)
        dfs(nums, sum + i)
        nums.pop()


n, k = map(int, input().split())
count = 0

dfs([], 0)
print(-1)
