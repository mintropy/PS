import sys
sys.setrecursionlimit(int(1e6))

# 처음 값 설정, 최솟값을 가지는 인덱스로
def init(start, end, node):
    '''
    start = 1, end = n, node = 1
    으로하는 segment tree 작성
    '''
    global seq, segment_tree
    if start == end:
        segment_tree[node] = start
        return start
    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    # 두 부분에서 최솟값을 가지는 인덱스
    s1 = segment_tree[node * 2]
    s2 = segment_tree[node * 2 + 1]
    if seq[s1] > seq[s2]:
        segment_tree[node] = s2
    # 두 부분의 최솟값이 같으면 더 작은 인덱스 값으로 입력
    elif seq[s1] <= seq[s2]:
        segment_tree[node] = s1

# 최솟값 찾기
def find_min(start, end, node, left, right):
    '''
    찾는 구간 start부터 end사이
    탐색하고 있는 점 node
    검색 범위 left에서 right
    '''
    global segment_tree
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segment_tree[node]
    mid = (start + end) // 2
    s1 = find_min(start, mid, node * 2, left, right)
    s2 = find_min(mid + 1, end, node * 2 + 1, left, right)
    # 해당하는 인덱스가 없는 경우
    if s1 == 0 and s2 == 0:
        return 0
    # 둘 중 하나만 존재할 때
    elif s1 == 0:
        return s2
    elif s2 == 0:
        return s1
    # 두 값 모두 존재하면 비교하여 출력
    else:
        if seq[s1] > seq[s2]:
            return s2
        elif seq[s1] <= seq[s2]:
            return s1
        
        
def solve(s, e):
    global ans, n, seq, segment_tree
    if e < s:
        return
    idx = find_min(1, n, 1, s, e)
    if idx == 0:
        return
    # 더 큰 직사각형을 찾으면 최신화
    ans = max(ans, (e - s + 1) * seq[idx])
    # 새로운 범위 탐색
    solve(s, idx - 1)
    solve(idx + 1, e)


while True:
    seq = list(map(int, sys.stdin.readline().split()))
    if seq == [0]:
        break
    n = seq[0]
    segment_tree = [0 for _ in range(n * 4)]
    init(1, n, 1)

    ans = 0
    solve(1, n)
    print(ans)
