"""
Title : 직각이등변삼각형찾기
Link : https://www.acmicpc.net/problem/2658
"""

from sys import stdin

input = stdin.readline


def search(vertax: list) -> None:
    x, y = search[0]


if __name__ == "__main__":
    my_map = [f"0{input().strip()}0" for _ in range(10)]
    vertax = []
    for i in range(1, 11):
        for j in range(1, 11):
            if my_map[i][j] == "1":
                vertax.append((i, j))
                break
        else:
            continue
        break
    if not vertax:
        print(0)
    else:
        pass
