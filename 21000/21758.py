"""
Title : 꿀 따기
Link : https://www.acmicpc.net/problem/21758
"""

from itertools import accumulate
import sys
input = sys.stdin.readline


def solution() -> None:
    N = int(input())
    honey = list(map(int, input().split()))

    prefix_sum = list(honey)
    max_honey = 0
    
    for idx, hive in enumerate(prefix_sum):
        if idx == 0 or idx == N - 1:
            base_count = prefix_sum[-1] - honey[idx] - honey[0] - honey[-1]
        else:
            base_count = 0
        
    
    return None


solution()
