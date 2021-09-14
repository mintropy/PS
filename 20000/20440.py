"""
Title : 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1
Link : https://www.acmicpc.net/problem/20440
"""

import sys, collections
input = sys.stdin.readline



n = int(input())
mosquito = collections.defaultdict(lambda: [0, 0])
for _ in range(n):
    enter, exit = map(int, input().split())
    mosquito[enter][0] += 1
    mosquito[exit][1] += 1

max_mosquitos = 0
max_mosquitos_durations = [-1, -1]

mosquitos_now = 0

for time in sorted(mosquito.keys()):
    # 지금 시간 이전까지 최대 모기였을 경우
    if mosquitos_now == max_mosquitos:
        mosquitos_now += mosquito[time][0] - mosquito[time][1]
        max_mosquitos_durations[1] = time
        # 모기수가 증가하는 경우
        if mosquitos_now > max_mosquitos:
            max_mosquitos = mosquitos_now
            max_mosquitos_durations = [time, time]
    # 지금 시간 이전까지 최대 모기가 아닌 경우
    else:
        mosquitos_now += mosquito[time][0] - mosquito[time][1]
        # 모기수가 기존 최대 모기수보다 더 많아지는 경우
        if mosquitos_now > max_mosquitos:
            max_mosquitos = mosquitos_now
            max_mosquitos = [time, time]

print(max_mosquitos)
print(*max_mosquitos_durations)
