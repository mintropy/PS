"""
Title : 최댓값
Link : https://www.acmicpc.net/problem/2566
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    column, row = 0, 0
    max_value = 0
    for i in range(9):
        arr = list(map(int, input().strip().split()))
        if (max_in_row := max(arr)) > max_value:
            max_value = max_in_row
            column, row = i, arr.index(max_value)
    print(f"{max_value}\n{column + 1} {row + 1}")
