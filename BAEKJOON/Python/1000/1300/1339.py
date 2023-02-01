"""
Title : 단어 수학
Link : https://www.acmicpc.net/problem/1339
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    alps = {chr(65 + x): 0 for x in range(26)}
    numbers = []
    for _ in range(N):
        s = input().strip()
        for i, x in enumerate(s):
            alps[x] += 10 ** (len(s) - i)
        numbers.append(s)
    tmp = sorted([(k, v) for k, v in alps.items() if v], key=lambda x: -x[1])
    alp_to_num = {}
    for i, (k, v) in enumerate(tmp):
        alp_to_num[k] = 9 - i
    ans = 0
    for s in numbers:
        p = 0
        for i, x in enumerate(s):
            p *= 10
            p += alp_to_num[x]
        ans += p
    print(ans)
