"""
Title : 직각 삼각형의 두 변
Link : https://www.acmicpc.net/problem/6322
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    triangle_num = 1
    ans = []
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        tmp = f"Triangle #{triangle_num}\n"
        triangle_num += 1
        if c == -1:
            tmp += "c = %.3f\n" % ((a**2 + b**2) ** 0.5)
        elif a == -1:
            if b >= c:
                tmp += "Impossible.\n"
            else:
                tmp += "a = %.3f\n" % ((c**2 - b**2) ** 0.5)
        elif b == -1:
            if a >= c:
                tmp += "Impossible.\n"
            else:
                tmp += "b = %.3f\n" % ((c**2 - a**2) ** 0.5)
        ans.append(tmp)
    print("\n".join(ans))
