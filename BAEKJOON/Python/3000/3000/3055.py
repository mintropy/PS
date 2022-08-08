'''
Title : 탈출
Link : https://www.acmicpc.net/problem/3055
'''

import sys, collections

input = sys.stdin.readline

def check_water(new, i, j):
    
    return True


def bfs(forest, r, c):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 고슴도치 위치
    for i in range(r):
        for j in range(c):
            if forest[i][j] == 'S':
                hedgehog = [i, j]
    # queue에 숲 상황, 고슴도치 위치, 수행된 시간 저장
    queue = collections.deque([(forest, hedgehog, 0)])
    while queue:
        now, hog, count = queue.popleft()
        for i in range(4):
            new = [['.' for _ in range(c)] for _ in range(r)]
            next_hog = [hog[0] + dx[i], hog[1] + dy[i]]
            new[next_hog[0]][next_hog[1]] = 'S'
            
                        

    return -1

r, c = map(int, input().split())
forest = [list(input()) for _ in range(r)]

answer = bfs(forest)
if answer == -1:
    print('KAKTUS')
else:
    print(answer)