"""
Title : 큰 놈, 작은 놈, 같은 놈
"""

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    if n < m:
        print(f'#{tc} <')
    elif n == m:
        print(f'#{tc} =')
    else:
        print(f'#{tc} >')