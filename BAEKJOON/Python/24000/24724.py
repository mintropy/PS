"""
Title : 현대모비스와 함께하는 부품 관리
Link : 
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    for tc in range(1, int(input()) + 1):
        N = int(input())
        A, B = MIIS()
        materials = [tuple(MIIS()) for _ in range(N)]
        print(f"Material Management {tc}")
        print("Classification ---- End!")
