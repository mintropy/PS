"""
Title : 숌트링
Link : https://www.acmicpc.net/problem/1488
"""

import sys
input = sys.stdin.readline


def calc_piece(count_S, max_S) -> int:
    if max_S == 0:
        return 0
    elif max_S == 1:
        return count_S
    elif count_S % max_S:
        return count_S // max_S + 1
    return count_S // max_S


count_A, count_B, max_A, max_B = map(int, input().split())

if max_A == 0 or max_B == 0:
    if max_A == 0 and max_B == 0:
        print(0)
    elif max_A == 0:
        print(min(count_B, max_B))
    else:
        print(min(count_A, max_A))
else:
    piece_A, piece_B = calc_piece(count_A, max_A), calc_piece(count_B, max_B)
    if piece_A < piece_B:
        count_A, count_B = count_B, count_A
        max_A, max_B = max_B, max_B
        piece_A, piece_B = piece_B, piece_A
    if piece_B == 0:
        if piece_A == 0:
            print(0)
        elif piece_A == 1:
            print(count_A)
        else:
            print(max_A)
    else:
        if piece_A - piece_B <= 1:
            print(count_A + count_B)
        else:
            if max_A == 1:
                left = 1
            elif count_A % max_A == 0:
                left = max_A
            else:
                left = count_A % max_A
            
            print((count_A + count_B) - (left + max_A * (piece_A - piece_B - 2)))

'''
100 100 20 50
'''
