"""
Title : 로봇 시뮬레이션
Link : https://www.acmicpc.net/problem/2174
"""

import sys
input = sys.stdin.readline


a, b = map(int, input().split())
n, m = map(int, input().split())

# 벽: -1, 로봇은 번호로
field = [[-1] * (b + 2)] + [[-1] + [0] * a + [-1] for _ in range(b)] + [[-1] * (b + 2)]
# 각 로봇 인덱스에, 로봇 위치, 방향 저장
robots = [[]]
for i in range(1, n + 1):
    x, y, f = map(str, input().strip().split())
    # x가 아래서부터, y가 왼쪽에서부터로 조정
    x, y = int(y), int(x)
    # 좌표 조정
    x = b + 1 - x
    # 로봇 지정
    field[x][y] = i
    robots.append([x, y, f])

direction = ['N', 'E', 'S', 'W']
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

for _ in range(m):
    robot, cmd, cnt = map(str, input().strip().split())
    # 로봇 번호
    robot = int(robot)
    # 반복 횟수
    cnt = int(cnt)
    if cmd == 'L':
        cnt %= 4
        d = robots[robot][2]
        for _ in range(cnt):
            d = (d - 1) % 4
        robots[robot][2] = d
    elif cmd == 'R':
        cnt %= 4
        d = robots[robot][2]
        for _ in range(cnt):
            d = (d + 1) % 4
        robots[robot][2] = d
    else:
        # 로봇 위치, 방향
        x, y, f = robots[robot]
        # 방향에 대한 인덱스
        d = direction.index(f)
        for i in range(1, cnt + 1):
            nx, ny = x + dx[d] * i, y + dy[d] * i
            if not field[x][y]:
                continue
            # 벽
            elif field[x][y] == 1:
                print(f'Robot {robot} crashes into the wall')
                exit()
            # 다른 로봇
            else:
                print(f'Robot {robot} crashes into robot {field[nx][ny]}')
                exit()
        # 바뀐 위치 조정
        field[x][y] = 0
        field[nx][ny] = robot
        robots[robot][0] = nx
        robots[robot][1] = ny
else:
    print('OK')
