"""
Title : 순열장난
Link : https://www.acmicpc.net/problem/10597
"""

from sys import stdin

input = stdin.readline


def search(idx: int):
    global seq, N, check
    if idx == len(seq):
        return [0]
    if not check[(x := seq[idx])]:
        check[x] = True
        if res := search(idx + 1):
            return [x] + res
        check[x] = False
    if idx < len(seq) - 1:
        num = seq[idx] * 10 + seq[idx + 1]
        if num > N or num < 10:
            return None
        if not check[num]:
            check[num] = True
            if res := search(idx + 2):
                return [num] + res
            check[num] = False
    return None


if __name__ == "__main__":
    seq = [int(x) for x in input().strip()]
    if (l := len(seq)) <= 9:
        print(*seq)
    else:
        N = (l + 9) // 2
        check = [False] * (N + 1)
        print(*search(0)[:-1])
