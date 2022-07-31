"""
Title : 평면 분할
Link : https://www.acmicpc.net/problem/18187
"""

n = int(input())

grids = 0

# 첫번째 직선
if n % 3:
    grids += n // 3 + 2
else:
    grids += n // 3 + 1

# 두번째 직선
if n == 1:
    pass
elif n % 3 == 2:
    grids *= n // 3 + 2
else:
    grids *= n // 3 + 1

# 세번째 직선
if n == 2:
    pass
else:
    grids += (n - n // 3 + 1) * (n // 3)

print(grids)
