import sys

input = sys.stdin.readline

def length(x: list, y: list) -> int:
    '''
    두 점  x, y 사이의 거리의 제곱
    '''
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

def smaller(a: int, b: int) -> int:
    '''
    두 정수중 작은 값을 반환
    '''
    if a < b:
        return a
    else:
        return b

def solution(st: int, end: int) -> int:
    '''
    st와 end 인덱스 사이의 점들의 거리중 가장 작은값을 반환
    '''
    global n, points
    # 시작, 끝 인덱스 사이 점이 1개, 2개 또는 3개인 경우
    diff = end - st
    if diff == 1:
        return 0
    elif diff == 2:
        return length(points[st], points[st + 1])
    elif diff == 3:
        t1 = length(points[st], points[st + 1])
        t2 = length(points[st], points[st + 2])
        t3 = length(points[st + 1], points[st + 2])
        return smaller(t1, smaller(t2, t3))
    # 그렇지 않은 경우, 중간점을 선택하여 분할
    # 분할된 두 부분에서 최단 거리 탐색
    mid = (st + end) // 2
    mid_x = points[mid][0]
    p = solution(st, mid)
    q = solution(mid, end)
    # 최소 거리 r
    if p < q:
        r = p
    else:
        r = q
    # 두 점이 다른 분할에 있는 경우 탐색
    # 중간점부터 거리가 최대 거리보다 작은 경우
    # st, end 사이의 점과, 중간점사이 x좌표가 최소거리보다 작은 경우 추가
    tmp = []
    for i in range(st, end):
        if (mid_x - points[i][0]) ** 2 <= r:
            tmp.append(points[i])
    # 위의 선택한 점에서 y좌표에 대하여 정렬하여 다시 시행
    tmp.sort(key = lambda x: x[1])
    l = len(tmp)
    if l >= 2:
        for i in range(l - 1):
            for j in range(i + 1, l):
                dist = length(tmp[i], tmp[j])
                # 두 점 사이의 거리가 최솟값 보다 큰 경우
                if dist > r:
                    break
                # x기준 두 점이 왼쪽 또는 오른쪽에 있는 값인 경우
                elif tmp[i][0] > mid_x and tmp[j][0] > mid_x:
                    continue
                elif tmp[i][0] < mid_x and tmp[j][0] < mid_x:
                    continue
                # 그렇지 않은 경우 거리 계산, 최단거리로 최신화
                r = smaller(r, dist)
    return r


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
# 중복되는 점이 있을 때 0 출력, 아니면 탐색 함수 실행
if len(list(set(points))) != n:
    print(0)
else:
    points.sort()
    print(solution(0, n))
