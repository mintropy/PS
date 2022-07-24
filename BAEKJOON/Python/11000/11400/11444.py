import sys, collections, math

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n = int(input())

a = [[0, 1], [0, 1]]
power = [[0, 1], [1, 1]]

def matrix_mul(x: list, y: list) -> list:
    tmp = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp[i][j] += x[i][k] * y[k][j]
            tmp[i][j] %= 1000000007
    return tmp

# 행렬의 2 ^ i 제곱의 저장
matrix = collections.defaultdict(list)
# 현재 제곱
order = 1
matrix[1] = power
result = power

while True:
    if order == n:
        break
    if order * 2 <= n:
        result = matrix_mul(result, result)
        order *= 2
        matrix[order] = result
    elif order * 2 > n:
        dif = n - order
        dif = int(math.log2(dif))
        order += 2 ** dif
        result = matrix_mul(result, matrix[2 ** dif])

a = matrix_mul(a, result)
print(a[0][0] % 1000000007)