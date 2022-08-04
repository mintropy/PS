"""
Title : 다각형 그리기
Link : https://www.acmicpc.net/problem/2641
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


def check(length: int, target: list, line: list) -> bool:
    def get_reverse_line(line: list) -> list:
        reverse_table = {1: 3, 2: 4, 3: 1, 4: 2}
        line.reverse()
        for idx, x in enumerate(line):
            line[idx] = reverse_table[x]
        return line

    for _ in range(length):
        if target == line:
            return True
        line = line[1:] + [line[0]]
    line = get_reverse_line(line)
    for _ in range(length):
        if target == line:
            return True
        line = line[1:] + [line[0]]
    return False


if __name__ == "__main__":
    length = II()
    target = list(MIIS())
    ans = []
    for _ in range(II()):
        line = list(MIIS())
        if check(length, target, line):
            ans.append(line)
    print(len(ans))
    for line in ans:
        print(*line)
