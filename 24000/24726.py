"""
Title : 미적분학 입문하기 2
Link : 
"""

import math
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    ans_x = ans_y = 0
    
    
    print(ans_x * math.pi, ans_y * math.pi)
