"""
Title : 심각한 계단 중독입니다
Link : 
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    array = sorted(map(int, input().split()))
    for i in range(1, N - 1):
        if abs(array[i] - array[i - 1]) != 1:
            array[i], array[i + 1] = array[i + 1], array[i]
        if abs(array[i] - array[i - 1]) != 1:
            print(-1)
            break
    else:
        if abs(array[-1] - array[-2]) == 1 and abs(array[0] - array[-1]) == 1:
            print(1)
        else:
            print(-1)
