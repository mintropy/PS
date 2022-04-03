import sys, heapq

input = sys.stdin.readline

class FenwickTree:
    """ Fenwick tree for sum operation """
    def __init__(self, n: int):
        self.size = n
        self.seq = [0] * n
        self.tree = [0] * n

    def update(self, pos: int, num: int):
        self.seq[pos] = num
        while pos < self.size:
            self.tree[pos] += num
            pos |= pos + 1

    def query(self, start: int, end: int) -> int:
        result = 0
        i = end - 1
        while i >= 0:
            result += self.tree[i]
            i = (i & (i + 1)) - 1
        i = start - 1
        while i >= 0:
            result -= self.tree[i]
            i = (i & (i + 1)) - 1
        return result


t = int(input())
for _ in range(t):
    n = int(input())
    # 각 섬 좌표 불러오기 & 정렬
    cor = []
    for i in range(n):
        x, y = map(int, input().split())
        cor.append([x, y])

    # y좌표 압축
    cor.sort(key = lambda x: x[1])
    compressed_y = 0
    prev = cor[0][1]
    for i in range(len(cor)):
        if cor[i][1] != prev:
            prev = cor[i][1]
            compressed_y += 1
        cor[i][1] = compressed_y
    
    # 펜윅 트리
    cor.sort(key = lambda x: -x[0])
    fenwick = FenwickTree(n)
    answer = 0
    for _, y in cor:
        answer += fenwick.query(0, y + 1)
        fenwick.update(y, 1)
        
    print(answer)