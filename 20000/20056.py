from sys import stdin

N, M, k = map(int, stdin.readline.split())
graph = [[] * N for _ in range(N)]
# 순서대로 위치 r, c, 질량 m, 속력 s, 방향 d
for _ in range(M):
    r, c, m, s, d = map(int, stdin.readline().split())
    graph[r][c].append((m, s, d))
    

def move(r, c, s, d): 
    #위치 r, c, 속력 s, 방향 d
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    r, c = r + dx[d] * s, c + dy[d] * s
    if r < 0:
        r = N - r // N
    elif r >= N:
        r = (r + 1) // N - 1
    if c < 0:
        c = N - r // C
    elif c >= N:
        c = (c + 1) // N - 1
    return r, c


for _ in range(k):
    new_graph = [[] * N for _ in range(N)]
    # 파이어볼 이동
    for i in range(N):
        for j in range(N):
            if graph[i][j] == []:
                continue
            for m, s, d in graph[i][j]:
                r, c = move(i, j, s, d)
                new_graph[r][c].append(m, s, d)
    # 파이어볼이 같은 칸에 있음
    for i in range(N):
        for j in range(N):
            if new_graph[i][j] == []:
                continue
            len(new_graph[i][j]) = l
            m_sum = 0
            s_sum = 0
            for m, s, d in new_graph[i][j]:
                m_sum += m
                s_sum += s
            if l % 2 == 0:
                vector = [0, 2, 4, 6]
                tmp = []
                for k in range(4):
                    tmp.append((m_sum / 5, s_sum / 4, vector[k]))
            else:
                vector = [1, 3, 5, 7]
                tmp = []
                for k in range(4):
                    tmp.append((m_sum / 5, s_sum / 4, vector[k])
            graph[i][j] = tmp


ans = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == []:
            continue
        for m, s, d in graph[i][j]:
            ans += m

print(ans)