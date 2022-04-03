"""
Title : 구슬 탈출 2
Link : https://www.acmicpc.net/problem/13460
"""

import sys, collections
input = sys.stdin.readline


def bfs(ball_status, hall: list) -> int:
    while ball_status:
        red, blue, c = ball_status.popleft()
        r1, r2 = red
        b1, b2 = blue
        if c >= 10:
            break
        for d in range(4):
            nr1, nr2, nb1, nb2 = board_tilt(d, [r1, r2], [b1, b2])
            if r1 == nr1 and r2 == nr2 and b1 == nb1 and b2 == nb2:
                continue
            elif [nr1, nr2] == hall:
                if [nb1, nb2] == hall:
                    continue
                else:
                    return c + 1
            elif [nb1, nb2] == hall:
                continue
            else:
                ball_status.append(((nr1, nr2), (nb1, nb2), c + 1))
    return -1


def board_tilt(d: int, red: list, blue: list) -> tuple:
    global board, dx, dy
    r1, r2 = red
    b1, b2 = blue
    # 각 공이 움직일 수 있는지
    red_able = True
    blue_able = True
    
    while red_able or blue_able:
        # 둘 다 움직일 수 있을 때
        if red_able and blue_able:
            red_move = ball_move(r1, r2, d)
            blue_move = ball_move(b1, b2, d)
            
            if blue_move == 'hall':
                b1 += dx[d]
                b2 += dy[d]
                blue_able = False
            elif blue_move == 'wall':
                blue_able = False
            else:
                if red_move == 'wall':
                    red_able = False
                    continue
                else:
                    b1 += dx[d]
                    b2 += dy[d]
            
            if red_move == 'hall':
                r1 += dx[d]
                r2 += dy[d]
                red_able = False
            elif red_move == 'wall':
                red_able = False
            else:
                if blue_move == 'wall':
                    continue
                else:
                    r1 += dx[d]
                    r2 += dy[d]
        # 둘 중 하나만 움직일 수 있을 때
        else:
            if red_able:
                red_move = ball_move(r1, r2, d)
                if red_move == 'hall':
                    r1 += dx[d]
                    r2 += dy[d]
                    red_able = False
                elif red_move == 'wall':
                    red_able = False
                else:
                    nr1, nr2 = r1 + dx[d], r2 + dy[d]
                    if nr1 == b1 and nr2 == b2:
                        red_able = False
                    else:
                        r1, r2 = nr1, nr2
            elif blue_able:
                blue_move = ball_move(b1, b2, d)
                if blue_move == 'hall':
                    b1 += dx[d]
                    b2 += dy[d]
                    blue_able = False
                elif blue_move == 'wall':
                    blue_able = False
                else:
                    nb1, nb2 = b1 + dx[d], b2 + dy[d]
                    if nb1 == r1 and nb2 == r2:
                        blue_able = False
                    else:
                        b1, b2 = nb1, nb2        
    
    return r1, r2, b1, b2


def ball_move(x: int, y: int, d: int) -> str:
    global board, dx, dy
    nx, ny = x + dx[d], y + dy[d]
    if board[nx][ny] == '#':
        return 'wall'
    if board[nx][ny] == 'O':
        return 'hall'
    elif board[nx][ny] == '.':
        return 'go'



n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j] == 'B':
            blue_ball = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'R':
            red_ball = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'O':
            hall = [i, j]

ball_status = collections.deque([(red_ball, blue_ball, 0)])
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


print(bfs(ball_status, hall))



'''
#from sys import stdin
from collections import deque
# 인풋 받기

# n, m = map(int, stdin.readline().split())
# board = []
# for _ in range(n):
#     board.append(list(map(int, stdin.readline().split())))


# 예제
n, m = 5, 5
board = [['#','#','#','#','#'],
        ['#','.','.','B','#'],
        ['#','.','#','.','#'],
        ['#','R','O','.','#'],
        ['#','#','#','#','#']]


# 보드판에서 빨간공, 파란공 위치 확인
# 보드판은 벽, 길, 구멍만 표시
# 빨간공, 파란공 위치만 옮기며 실행

red_ball = []
blue_ball = []
target = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red_ball = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            blue_ball = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'O':
            target = [i, j]


def move(red_ball, blue_ball, d):
    global board
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 공을 더 굴릴 수 있으면 False, 못굴리면 True
    r1, r2 = red_ball
    b1, b2 = blue_ball
    board[r1][r2] = 'R'
    board[b1][b2] = 'B'

        

    return (r1, r2), (b1, b2)
    


def bfs():
    queue = deque([(red_ball, blue_ball, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[red_ball[0]][red_ball[1]] = True
    visited[blue_ball[0]][blue_ball[1]] = True
    possible = False
    ans = 0
    while queue:
        red, blue, count = queue.popleft()
        if count >= 11:
            break
        for d in range(4):
            red_new, blue_new = move(red, blue, d)
            r1, r2 = red_new
            b1, b2 = blue_new
            if visited[r1][r1] and visited[b1][b2]:
                continue
            if r1 == b2 and r2 == b2:
                if board[r1][r2] == 'O':
                    continue
                # 같은 위치이지만, 구멍이 아니라면 더 뒤에 있던 공 이동
                

            elif board[r1][r2] == 'O':
                possible = True
                ans = count
                break
            elif board[b1][b2] == 'O':
                continue
            queue.append(([r1, r2], [b1, b2], count + 1))
            visited[r1][r2] = True
            visited[b1][b2] = True
        if possible:
            return count
    return -1


print(bfs())
'''