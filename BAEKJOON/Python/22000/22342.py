"""
Title : 계산 로봇
Link : https://www.acmicpc.net/problem/22342
"""

from sys import stdin
input = stdin.readline


def get_max_vlaue(output_value: list, i: int, j: int) -> int:
    global M
    values = [output_value[i][j - 1]]
    if i != 0:
        values.append(output_value[i - 1][j - 1])
    if i != M - 1:
        values.append(output_value[i + 1][j - 1])
    return max(values)


def get_max_saved_value(saved_value: list) -> int:
    return min([line[-1] for line in saved_value])


if __name__ == "__main__":
    M, N = map(int, input().split())
    my_map = list([int(i) for i in input().strip()] for _ in range(M))
    saved_value = [[0] * N for _ in range(M)]
    output_value = [[0] * N for _ in range(M)]
    for i in range(M):
        output_value[i][0] = my_map[i][0]
    for j in range(1, N):
        for i in range(M):
            saved_value[i][j] = get_max_vlaue(output_value, i, j)
            output_value[i][j] = saved_value[i][j] + my_map[i][j]
    print(get_max_saved_value(saved_value))
