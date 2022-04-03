import sys

input = lambda : sys.stdin.readline()

# 시간초과와 오버플로우를 막기 위해, 모든 계산에 1,000,007로 나눈 나머지를 저장
def init(start, end, node):
    global seq, segment_tree
    if start == end:
        segment_tree[node] = seq[start]
        return seq[start]
    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    segment_tree[node] = (segment_tree[node * 2] * segment_tree[node * 2 + 1]) % 1000000007
    
def partial_product(start, end, node, left, right):
    global segment_tree
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return segment_tree[node]
    mid = (start + end) // 2
    return (partial_product(start, mid, node * 2, left, right) * partial_product(mid + 1, end, node * 2 + 1, left, right)) % 1000000007

# 자식 노드값을 모두 계산한 후 부모 노드 값을 계산하는 순서로 진행
def change_value(start, end, node, idx, old, new):
    global seq, segment_tree
    if idx > end or idx < start:
        return
    if start == end:
        segment_tree[node] = new
        return
    mid = (start + end) // 2
    change_value(start, mid, node * 2, idx, old, new)
    change_value(mid + 1, end, node * 2 + 1, idx, old, new)
    segment_tree[node] = (segment_tree[node * 2] * segment_tree[node * 2 + 1]) % 1000000007
    

n, m, k = map(int, input().split())
seq = [0]
for _ in range(n):
    seq.append(int(input()))
segment_tree = [0] * (n * 4)
init(1, n, 1)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        change_value(1, n, 1, b, seq[b], c)
        seq[b] = c
    elif a == 2:
        print(partial_product(1, n, 1, b, c))
