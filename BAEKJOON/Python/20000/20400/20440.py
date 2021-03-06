"""
Title : ๐ต๋๊ฐ ์ซ์ด ์ซ์ด ๋๋ฌด ์ซ์ด ์ซ์ด ์ค์ง ๋ง ๋ด๊ฒ ์ฐ์ฉ๋์ง๋ง๐ต - 1
Link : https://www.acmicpc.net/problem/20440
"""

# import sys, collections
import sys
input = sys.stdin.readline

n = int(input())
'''
mosquito = collections.defaultdict(lambda: [0, 0])
for _ in range(n):
    enter, exit = map(int, input().split())
    mosquito[enter][0] += 1
    mosquito[exit][1] += 1
'''
mosquito = {}
for _ in range(n):
    enter, exit = map(int, input().split())
    if enter in mosquito:
        mosquito[enter] += 1
    else:
        mosquito[enter] = 1
    if exit in mosquito:
        mosquito[exit] -= 1
    else:
        mosquito[exit] = -1

# ๋ชจ๊ธฐ๊ฐ ์ต๋์ผ ๋
max_mosquitos: int = 0
# ๋ชจ๊ธฐ๊ฐ ์ต๋์ผ ๋ ์๊ฐ
max_mosquitos_durations: list = [-1, -1]
# ๊ฐ ์ต๋ ๋ชจ๊ธฐ์๋ฅผ ์ฒ์ ๋ง๋ฌ์ ๋
is_max_mosquito_fist = True
# ์ง๊ธ ๋ชจ๊ธฐ ์
mosquitos_now: int = 0

for time in sorted(mosquito.keys()):
    # ์ง๊ธ ์๊ฐ ์ด์ ๊น์ง ์ต๋ ๋ชจ๊ธฐ์์ ๊ฒฝ์ฐ
    if mosquitos_now == max_mosquitos and is_max_mosquito_fist:
        mosquitos_now += mosquito[time]
        max_mosquitos_durations[1] = time
        # ๋ชจ๊ธฐ์๊ฐ ์ฆ๊ฐํ๋ ๊ฒฝ์ฐ
        if mosquitos_now > max_mosquitos:
            is_max_mosquito_fist = True
            max_mosquitos = mosquitos_now
            max_mosquitos_durations = [time, time]
    # ์ง๊ธ ์๊ฐ ์ด์ ๊น์ง ์ต๋ ๋ชจ๊ธฐ๊ฐ ์๋ ๊ฒฝ์ฐ
    else:
        mosquitos_now += mosquito[time]
        is_max_mosquito_fist = False
        # ๋ชจ๊ธฐ์๊ฐ ๊ธฐ์กด ์ต๋ ๋ชจ๊ธฐ์๋ณด๋ค ๋ ๋ง์์ง๋ ๊ฒฝ์ฐ
        if mosquitos_now > max_mosquitos:
            is_max_mosquito_fist = True
            max_mosquitos = mosquitos_now
            max_mosquitos_durations = [time, time]

print(max_mosquitos)
print(*max_mosquitos_durations)


'''
13
2 8
5 6
3 8
1 9
10 56
2 5
6 90
5 8
3 60
4 89
10 13
10 13
10 13

2
0 1100000000
1000000000 2100000000

'''