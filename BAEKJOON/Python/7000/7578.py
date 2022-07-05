"""
Title : 공장
Link : https://www.acmicpc.net/problem/7578
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N = int(input())
    row_a = list(MIIS())
    row_b = list(MIIS())
    connect = [0] * N
    for i, x in enumerate(row_a):
        for j, y in enumerate(row_b):
            if x == y:
                connect[i] = j
                break


"""
공장, 2N개 기계 2열에 N개씩, A열 B열
A열 기계는 각각 B열 기계와 쌍을 이룸

각 기계 고유번호, 작이 맺어진 기계끼리 같은 식별번호
순서대로 배치되어 있지 않아, 케이블 엉킴 >> 고장 원인
기계 위치를 바꾸지 않은 상태에서 기계를 잇는 직선 형태

132 392 311 351 231
392 351 132 311 231
>> 교차 횟수는 3
>> 교차 횟수 세는 프로그램
"""
