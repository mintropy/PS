"""
Title : 등차수열 변환
Link : https://www.acmicpc.net/problem/17088
"""

from sys import stdin

input = stdin.readline


def make_arithmetic_seq(N: int, seq: list[int]) -> int:
    ans = -1
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            tmp = abs(i) + abs(j)
            tmp_seq = seq[::]
            tmp_seq[0] += i
            tmp_seq[1] += j
            diff = tmp_seq[1] - tmp_seq[0]
            for k in range(2, N):
                _diff = tmp_seq[k] - tmp_seq[k - 1]
                if _diff == diff:
                    continue
                if _diff == diff + 1:
                    tmp_seq[k] -= 1
                    tmp += 1
                elif _diff == diff - 1:
                    tmp_seq[k] += 1
                    tmp += 1
                else:
                    break
            else:
                if ans == -1 or ans > tmp:
                    ans = tmp
    return ans


if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    if seq == [seq[0]] * N or N <= 2:
        print(0)
    else:
        print(make_arithmetic_seq(N, seq))
