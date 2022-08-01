"""
Title : 이차원 배열과 연산
Link : https://www.acmicpc.net/problem/17140
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def sort_row(idx: int):
    global seq, row, column
    count_nums = {}
    for i in range(column):
        x = seq[idx][i]
        if not x:
            continue
        if x in count_nums:
            count_nums[x] += 1
        else:
            count_nums[x] = 1
    new_nums = sorted([(v, k) for k, v in count_nums.items()][:50])
    for i, (x, y) in enumerate(new_nums):
        seq[idx][i * 2] = y
        seq[idx][i * 2 + 1] = x
    for j in range(len(new_nums) * 2, 100):
        seq[idx][j] = 0
    if column < len(new_nums) * 2:
        column = len(new_nums) * 2


def sort_column(idx: int):
    global seq, row, column
    count_nums = {}
    for i in range(row):
        x = seq[i][idx]
        if not x:
            continue
        if x in count_nums:
            count_nums[x] += 1
        else:
            count_nums[x] = 1
    new_nums = sorted([(v, k) for k, v in count_nums.items()][:50])
    for i, (x, y) in enumerate(new_nums):
        seq[i * 2][idx] = y
        seq[i * 2 + 1][idx] = x
    for j in range(len(new_nums) * 2, 100):
        seq[j][idx] = 0
    if row < len(new_nums) * 2:
        row = len(new_nums) * 2


if __name__ == "__main__":
    r, c, k = MIIS()
    r, c = r - 1, c - 1
    seq = [[0] * 100 for _ in range(100)]
    for i in range(3):
        x, y, z = MIIS()
        seq[i][0] = x
        seq[i][1] = y
        seq[i][2] = z
    row, column = 3, 3
    for count in range(101):
        if seq[r][c] == k:
            print(count)
            break
        if row >= column:
            for i in range(row):
                sort_row(i)
        else:
            for i in range(column):
                sort_column(i)
    else:
        print(-1)
