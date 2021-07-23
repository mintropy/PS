#from sys import stdin
from collections import deque
# 인풋 받기
'''
n, m = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))
'''

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