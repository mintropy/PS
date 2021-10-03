"""
Title : 상어 초등학교
Link : https://www.acmicpc.net/problem/21608
"""

import sys
input = sys.stdin.readline

n = int(input())
# 학생 자리 배치 순서
students_order = [()] + [tuple(map(int, input().split())) for _ in range(n ** 2)]
# 각 학생의 자리
students_seat = [[] for _ in range(n ** 2 + 1)]
# 교실
classroom = [[0] * n for _ in range(n)]
