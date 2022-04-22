"""
Title : 출근 기록
Link : https://www.acmicpc.net/problem/14238
"""

import sys
input = sys.stdin.readline


def search(a, b, c, last1, last2):
    """
    A, B, C가 각각 출근한 날 수가 a, b, c이고
    전날 last1, 그 전날 last2가 출근했을 경우
    """
    global A, B, C, dp, count
    
    if a < 0 or b < 0 or c < 0:
        return False
    if a == 0 and b == 0 and c == 0:
        return True
    if dp[a][b][c][last1][last2]:
        return False
    dp[a][b][c][last1][last2] = True
    ans[count - a - b - c] = 'A'
    if search(a - 1, b, c, 0, last1):
        return True
    elif last1 != 1:
        ans[count - a - b - c] = 'B'
        if search(a, b - 1, c, 1, last1):
            return True
    elif last1 != 2 != last2:
        ans[count - a - b - c] = 'C'
        if search(a, b, c - 1, 2, last1):
            return True
    return False


if __name__ == "__main__":
    record = input().strip()
    A = record.count('A')
    B = record.count('B')
    C = record.count('C')
    count = len(record)
    
    dp = [[[[[False] * 3 for _ in range(3)] for _ in range(count + 1)] for _ in range(count + 1)] for _ in range(count + 1)]
    ans = [''] * (count - 1)
    if search(A, B, C, 0, 0):
        print(*ans, sep='')
    else:
        print(-1)
