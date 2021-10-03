"""
Title : 이 쿠키 달지 않아!
Link : https://www.acmicpc.net/problem/2031
"""



# python TLE & pypy WA
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def bin_search(left: int, right: int, m: int) -> int:
    global foods
    st = left
    st_time = foods[left]
    max_count = 1
    while left <= right:
        mid = (left + right) // 2
        if foods[mid] - st_time >= m:
            right = mid - 1
        else:
            if mid - st + 1 > max_count:
                max_count = mid - st + 1
            left = mid + 1
    return max_count


t, n, d, k = MIIS()
foods = sorted(list(MIIS()))

# 각 시간마다 효과 받는 음식 수
foods_count = [1] * n
for i in range(n):
    foods_count[i] = bin_search(i, n - 1, d)

# j번째 차를 마실 때, i번째 음식을 먹기 시작
dp = [[0] * n for _ in range(k)]
dp[0] = foods_count[::]

max_foods = 0
for i in range(1, k):
    tea_before = n - 1
    for j in range(n - 1, -1, -1):
        while True:
            if tea_before == -1:
                break
            elif foods[j] - foods[tea_before] >= d:
                if foods[tea_before] == foods[tea_before - 1]:
                    tea_before -= 1
                else:
                    break
            else:
                tea_before -= 1
        if tea_before == -1:
            break
        dp[i][j] = dp[i - 1][tea_before] + foods_count[j]
        if dp[i][j] > max_foods:
            max_foods = dp[i][j]

print(max_foods)
