"""
Title : 물병
Link : https://www.acmicpc.net/problem/1052
"""

n, k = map(int, input().split())

n = bin(n)
bottles_now = list(map(int, n[2:]))

bought = 0
for i in range(len(bottles_now)):
    bottle_count = sum(bottles_now)
    if bottle_count <= k:
        print(bought)
        break
    else:
        if bottles_now[i]:
            bought += 2 ** i
            bottles_now[i] = 0
            if i == len(bottles_now):
                break
            elif bottles_now[i + 1] == 0:
                bottles_now[i + 1] = 1
            else:
                idx = i + 1
                while idx < len(bottles_now):
                    if bottles_now[idx] == 0:
                        bottles_now[idx] = 1
                    else:
                        bottles_now[idx] = 0
                    idx += 1
