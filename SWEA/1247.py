'''
Title : 최적 경로
'''

def find_length(a, b, c, d):
    '''
    [a, b] 부터 [c, d]까지 택시 거리
    '''
    return abs(a - c) + abs(b - d)

def dfs(count: int, a: int, b: int):
    '''
    방문한 점의 수 c, 이전 방문한 점 [a, b]
    '''
    global n, x1, y1, x2, y2, total_length, min_length, visited
    # 모든 점을 방문한 경우
    if count == n:
        l = find_length(a, b, x2, y2)
        total_length += l
        if total_length < min_length:
            min_length = total_length
        total_length -= l
        return
    # 그렇지 않으면 다른 점을 확인 & 방문
    for i in range(n):
        if visited[i]:
            continue
        c, d = customer[i * 2], customer[i * 2 + 1]
        l = find_length(a, b, c, d)
        total_length += l
        visited[i] = True
        dfs(count + 1, c, d)
        total_length -= l
        visited[i] = False

t = int(input())
for i in range(t):
    n = int(input())
    x1, y1, x2, y2, *customer = list(map(int, input().split()))
    total_length = 0
    min_length = int(1e10)
    visited = [False] * n
    dfs(0, x1, y1)
    print('#', i + 1, ' ', min_length, sep = '')

