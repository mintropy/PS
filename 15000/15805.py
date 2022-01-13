"""
Title : 트리 나라 관광 가이드
Link : https://www.acmicpc.net/problem/15805
"""

import sys
input = sys.stdin.readline


K = int(input())
city_count = max(K) + 1


childs = [[] for _ in range(city_count)]
