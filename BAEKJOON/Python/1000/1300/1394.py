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
    base: int = len(total)

    positions = {x: idx for idx, x in enumerate(total)}
    ans: int = 0

    for idx, x in enumerate(secrect[::-1]):
        pass

    for x in secrect:
        ans *= len(total)
        ans += positions[x]
    print(ans)
