"""
Title : 본대 산책2
Link : https://www.acmicpc.net/problem/12850
"""

from sys import stdin

input = stdin.readline


def matrix_multiply(matrix1, matrix2):
    new_matrix = [[0] * 8 for _ in range(8)]
    if matrix2 is None:
        matrix2 = matrix1
    for i in range(8):
        for j in range(8):
            new_matrix[i][j] = (
                sum([matrix1[i][k] * matrix2[k][j] for k in range(8)]) % 1_000_000_007
            )
    return new_matrix


if __name__ == "__main__":
    adj_matrix = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
    ]
    matrix = [line[::] for line in adj_matrix]

    D = int(input())
    while D > 1:
        matrix = matrix_multiply(matrix, None)
        if D % 2:
            matrix = matrix_multiply(matrix, adj_matrix)
        D //= 2
    print(matrix[0][0])
