from sys import stdin

n, m = map(int, stdin.readline().split())
seq = [0]
for _ in range(n):
    seq.append(int(stdin.readline().strip()))

cmd = []
for _ in range(m):
    cmd.append(list(map(int, stdin.readline().split())))

segment_tree = [1e10 for _ in range(n * 4)]

# 처음 값 설정
def init(start, end, node):
    global seq, segment_tree
    if start == end:
        segment_tree[node] = seq[start]
        return seq[start]
    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    segment_tree[node] = min(segment_tree[node * 2], segment_tree[node * 2 + 1])

# 최소값 찾기
def find_min(start, end, node, left, right):
    global segment_tree
    if left > end or right < start:
        return 1e10
    if left <= start and right >= end:
        return segment_tree[node]
    mid = (start + end) // 2
    return min(find_min(start, mid, node * 2, left, right), find_min(mid + 1, end, node * 2 + 1, left, right))


def solution():
    init(1, n, 1)
    for a, b in cmd:
        print(find_min(1, n, 1, a, b))

solution()