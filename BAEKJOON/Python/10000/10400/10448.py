"""
Title : 유레카 이론
Link : https://www.acmicpc.net/problem/10448
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())


def find_triangulars(triangular_numbers: list, K: int) -> int:
    for x in triangular_numbers:
        for y in triangular_numbers:
            for z in triangular_numbers:
                if x + y + z == K:
                    return 1
    return 0


if __name__ == "__main__":
    triangular_numbers = [1]
    for i in range(2, 1000):
        triangular_numbers.append(triangular_numbers[-1] + i)
        if triangular_numbers[-1] > 1000:
            break
    for _ in range(II()):
        print(find_triangulars(triangular_numbers, II()))
