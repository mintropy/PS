"""
Title : 장군
Link : https://www.acmicpc.net/problem/16509
"""

def search(x, y):
    global janggi, r2, c2, sang_move
    if x == r2 and y == c2:
        return
    move_now = janggi[x][y]
    # 8방향 탐색
    for d in range(8):
        # 각 방향 마지막까지 갈 수 있는지
        dx, dy = sang_move[d][2]
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 9:
            # 중간 경로 가능한지
            nx1, ny1 = x + sang_move[d][0][0], y + sang_move[d][0][1]
            nx2, ny2 = x + sang_move[d][1][0], y + sang_move[d][1][1]
            if (nx1 == r2 and ny1 == c2) or (nx2 == r2 and ny2 == c2):
                continue
            # 마지막 칸의 위치에 따라 최신화
            new_move = janggi[nx][ny]
            if new_move > move_now + 1:
                janggi[nx][ny] = move_now + 1
                search(nx, ny)


r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

janggi = [[90] * 9 for _ in range(10)]
janggi[r1][c1] = 0

# 상이 이동가능한 모든 방향
sang_move = [
    [(-1, 0), (-2, -1), (-3, -2)],
    [(-1, 0), (-2, 1), (-3, 2)],
    [(0, 1), (-1, 2), (-2, 3)],
    [(0, 1), (1, 2), (2, 3)],
    [(1, 0), (2, -1), (3, -2)],
    [(1, 0), (2, 1), (3, 2)],
    [(0, -1), (1, -2), (2, -3)],
    [(0, -1), (-1, -2), (-2, -3)],
]

search(r1, c1)

print(janggi[r2][c2])
