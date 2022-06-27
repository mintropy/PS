"""
Title : 로봇 청소기
Link : https://www.acmicpc.net/problem/14503
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    x, y, d = MIIS()
    my_map = [list(MIIS()) for _ in range(N)]
    clean_map = [[False] * M for _ in range(N)]
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    clean_count = 0
    while True:
        if not clean_map[x][y]:
            clean_map[x][y] = True
            clean_count += 1
        for _ in range(4):
            d = (d - 1) % 4
            nx, ny = x + dx[d], y + dy[d]
            if not my_map[nx][ny] and not clean_map[nx][ny]:
                break
        else:
            nx, ny = x - dx[d], y - dy[d]
            if my_map[nx][ny]:
                break
        x, y = nx, ny
    print(clean_count)

"""
N * M크기의 방,
    각 칸은 벽 또는 빈 칸
로봇 청소기 작동
    현재 위치 청소
    현재 위치에서 인접 칸 탐색
        현재 위치 왼쪽에 청소하지 않은 빈 공간 > 왼쪽 회전, 전진
        아니라면 왼쪽으로 회전
    후진하지 않고 왼쪽 회전이 네 번 이상 실행된 경우
        뒤가 벽인 경우 멈춤, 아니면 후진
"""
