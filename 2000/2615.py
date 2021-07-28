"""
Title : 오목
Link : https://www.acmicpc.net/problem/2615
"""

import sys
input = sys.stdin.readline


def is_omok(omok, color):
    # 각 색을 기준으로 네 방향으로 탐색
    # 오른쪽, 오른쪽 아래 대각선, 아래, 왼쪽 아래 대각선

    for i in range(1, 16):
        for j in range(1, 16):
            # 해당하는 색을 만나면
            if omok[i][j] == color:
                for d in range(4):
                    if search(omok, color, i, j, d):
                        return True
                    
                pass
            pass
    pass


def search(omok, color, i, j, d):
    # 양방향으로 확인하기
    dx, dy = [0, 1, 1, 1], [1, 1, 0, -1]
    # 해당 방향 d와 반대 방향
    dx1, dy1 = [0, -1, -1, -1], [-1, -1, 0, 1]
    # 해당 color의 돌이 몇 개인지
    count = 0
    
    

omok = list(map(int, input().split()) for _ in range(19))

