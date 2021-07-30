"""
Title : 투에-모스 문자열
Link : https://www.acmicpc.net/problem/18222
"""

import sys, math
input = sys.stdin.readline

k = int(input())
first_8 = [0, 0, 1, 1, 0, 1, 0, 0, 1]

while True:
    k_log_2 = int(math.log2(k))
    power_of_2 = 1 << k_log_2
    