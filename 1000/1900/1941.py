"""
Title : 소문난 칠공주
Link : https://www.acmicpc.net/problem/1941
"""

import sys
input = sys.stdin.readline





students = [input().strip() for _ in range(5)]
students_check = [[False] * 5 for _ in range(5)]

possible_seven_princess = 0
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)



