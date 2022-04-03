"""
Title : 맞춰봐
Link : https://www.acmicpc.net/problem/1248
"""

import sys
input = sys.stdin.readline


def dfs(candidate: list, N: int, code: list, idx: int) -> list:
    if idx == N + 1:
        return candidate
    if code[idx][idx] == '0':
        if verify(candidate, code, 0, idx):
            candidate.append(0)
            answer = dfs(candidate, N, code, idx + 1)
            if answer:
                return answer
            candidate.pop()
    elif code[idx][idx] == '+':
        for i in range(1, 11):
            if verify(candidate, code, i, idx):
                candidate.append(i)
                answer = dfs(candidate, N, code, idx + 1)
                if answer:
                    return answer
                candidate.pop()
    else:
        for i in range(-1, -11, -1):
            if verify(candidate, code, i, idx):
                candidate.append(i)
                answer = dfs(candidate, N, code, idx + 1)
                if answer:
                    return answer
                candidate.pop()


def verify(candidate: list, code: list, num: int, idx: int) -> bool:
    prefix_sum = num
    for i in range(1, idx):
        prefix_sum += candidate[-i]
        cmd = code[idx - i][idx]
        if cmd == '0' and prefix_sum != 0:
            return False
        if cmd == '+' and prefix_sum <= 0:
            return False
        if cmd == '-' and prefix_sum >= 0:
            return False
    return True


N = int(input())
commands = input().strip()

code = ['']
for i in range(N, 0, -1):
    code.append(' ' * (N + 1 - i) + commands[:i])
    commands = commands[i:]

print(*dfs([], N, code, 1))
