"""
Title : 암호
Link : https://www.acmicpc.net/problem/1394
"""

from sys import stdin

input = stdin.readline
IS = lambda: input().strip()


if __name__ == "__main__":
    total: str = IS()
    secrect: str = IS()

    positions = {x: idx + 1 for idx, x in enumerate(total)}
    ans: int = 0
    for x in secrect:
        ans *= len(total)
        ans += positions[x]
    print(ans)
