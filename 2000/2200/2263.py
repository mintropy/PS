"""
Title : 트리의 순회
Link : https://www.acmicpc.net/problem/2263
"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def find_pre_order(in_st, post_st, length):
    # 인오더, 포스트오더 시작과 길이
    global in_order, post_order, in_order_idx
    if length == 2:
        print(post_order[post_st + 1], end = ' ')
        print(post_order[post_st], end = ' ')
        return
    elif length == 1 :
        print(in_order[in_st], end = ' ')
        return
    elif length == 0:
        return
    # 루트는 항상 포스트 오더 마지막
    root = post_order[post_st + length - 1]
    print(root, end=' ')
    # left, right 찾기
    in_order_root = in_order_idx[root]
    left_len = in_order_root - in_st
    # left와 right는 길이가 같아야 함
    # left
    find_pre_order(in_st, post_st, left_len)
    # right
    find_pre_order(in_order_root + 1, post_st + left_len, length - left_len - 1)


n = int(input())
in_order = list(map(int, input().split()))
in_order_idx = {in_order[i]:i for i in range(n)}
post_order = list(map(int, input().split()))

find_pre_order(0, 0, n)
