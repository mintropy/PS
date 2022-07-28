"""
Title : DSLR
Link : https://www.acmicpc.net/problem/9019
"""

from collections import deque
from sys import stdin

input = stdin.readline


def rotate_num(x: int, left: bool) -> int:
    x = str(x).zfill(4)
    if left:
        x = x[1:] + x[0]
    else:
        x = x[-1] + x[:-1]
    return int(x)


if __name__ == "__main__":
    for _ in range(int(input())):
        A, B = map(int, input().split())
        queue = deque([(A, "")])
        check = [False] * 10001
        while queue:
            x, now = queue.popleft()
            if x == B:
                print(now)
                break
            if check[x]:
                continue
            check[x] = True
            y = (x * 2) % 10000
            if not check[y]:
                queue.append((y, now + "D"))
            y = (x - 1) % 10000
            if not check[y]:
                queue.append((y, now + "S"))
            y = rotate_num(x, True)
            if not check[y]:
                queue.append((y, now + "L"))
            y = rotate_num(x, False)
            if not check[y]:
                queue.append((y, now + "R"))
