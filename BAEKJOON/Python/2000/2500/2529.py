"""
Title : 부등호
Link : https://www.acmicpc.net/problem/2529
"""

from sys import stdin

input = stdin.readline


def search(idx: int):
    global K, seq, ans, num_check, numbers
    if idx == 0:
        for i in range(10):
            numbers.append(i)
            num_check[i] = True
            search(idx + 1)
            numbers.pop()
            num_check[i] = False
    elif idx == K + 1:
        ans.append("".join(map(str, numbers)))
        return
    else:
        for i in range(10):
            if num_check[i]:
                continue
            if not seq_check(idx, i):
                continue
            numbers.append(i)
            num_check[i] = True
            search(idx + 1)
            numbers.pop()
            num_check[i] = False


def seq_check(idx: int, x: int) -> bool:
    global seq, numbers
    if seq[idx - 1] == "<" and numbers[idx - 1] < x:
        return True
    if seq[idx - 1] == ">" and numbers[idx - 1] > x:
        return True
    return False


if __name__ == "__main__":
    K = int(input())
    seq = tuple(input().strip().split())
    ans = []
    num_check = [False] * 10
    numbers = []
    search(0)
    print(ans[-1], ans[0], sep="\n")
