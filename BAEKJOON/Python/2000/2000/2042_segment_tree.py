from sys import stdin

n, m, k = map(int, stdin.readline().split())
seq = [0]
for _ in range(n):
    seq.append(int(stdin.readline().strip()))

segment_tree = [0 for _ in range(n * 4)]

# 처음 값 설정
def init(start, end, node):
    global seq, segment_tree
    if start == end:
        segment_tree[node] = seq[start]
        return seq[start]
    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]

# 부분합
def partial_sum(start, end, node, left, right):
    global segment_tree
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segment_tree[node]
    mid = (start + end) // 2
    return partial_sum(start, mid, node * 2, left, right) + partial_sum(mid + 1, end, node * 2 + 1, left, right)

# 값 변경
def update(start, end, node, idx, dif):
    global segment_tree
    if idx < start or idx > end:
        return
    segment_tree[node] += dif
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, dif)
    update(mid + 1, end, node * 2 + 1, idx, dif)

def solution():
    init(1, n, 1)
    for _ in range(m + k):
        a, b, c = map(int, stdin.readline().split())
        if a == 1:
            update(1, n, 1, b, c - seq[b])
            seq[b] = c
        elif a == 2:
            print(partial_sum(1, n, 1, b, c))

solution()