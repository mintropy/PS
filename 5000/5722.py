"""
Title : DNA 부분 수열
Link : https://www.acmicpc.net/problem/5722
"""

import sys
input = sys.stdin.readline


while True:
    x = int(input())
    if x == 0:
        break
    seq1 = input().strip()
    seq2 = input().strip()
    len_s1, len_s2 = len(seq1), len(seq2)
    
    LCS = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    for i, s1 in enumerate(seq1):
        for j, s2 in enumerate(seq2):
            if s1 == s2:
                LCS[i + 1][j + 1] = LCS[i][j] + 1
    
    longest_common_sequence = 0
    i, j = len_s1, len_s2
    common_sequence = 0
    common_segment = 0
    while True:
        if i == 0:
            if longest_common_sequence < common_sequence and common_segment >= x:
                longest_common_sequence = common_sequence
            if j == 0:
                break
            i, j = len_s1, j - 1
            common_sequence = 0
            common_segment = 0
        while i > 0:
            if LCS[i][j]:
                if common_segment < LCS[i][j]:
                    common_segment = LCS[i][j]
                common_sequence += LCS[i][j]
                i, j = i - LCS[i][j], j - LCS[i][j]
                break
            i -= 1
    
    print(longest_common_sequence)
    
