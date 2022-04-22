"""
Title : 혼자 하는 윷놀이 
Link : https://www.acmicpc.net/problem/24467
"""

from distutils import errors
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    pos = 0
    ans = "LOSE"
    while True:
        if pos == -1 and ans == "WIN":
            break
        try:
            move = input().strip()
            back = move.count("0")
            if pos == -1:
                ans = "WIN"
                break
            if not back:
                back = 5
            if pos == 33:
                pos = pos + back - 10
                if pos >= 35:
                    pos = -1
            elif pos == 5:
                pos = 20 + back
                if pos == 23:
                    pos = 33
            elif pos == 10:
                pos = 30 + back
            elif 21 <= pos <= 25:
                pos += back
                if pos == 23:
                    pos = 33
                elif pos > 25:
                    pos -= 9
            elif 31 <= pos <= 35:
                pos += back
                if pos >= 36:
                    pos = -1
            else:
                pos += back
                if pos >= 20:
                    pos = -1
        except errors:
            break
    print(ans)

'''
10  9  8  7  6  5
11  31      21  4
12    32  22    3
        33
13    24  34    2
14  25      35  1
15 16 17 18 19  0

'''
