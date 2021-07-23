# Title : 여우가 정보섬에 올라온 이유
# Link : https://www.acmicpc.net/problem/17131

import sys

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


n = int(input())
stars = []
for _ in range(n):
    stars.append(list(map(int, input().split())))

# y 좌표 압축
stars.sort(key = lambda x: x[1])
compressed_y = 0
prev = stars[0][1]
for i in range(n):
    if stars[i][1] != prev:
        prev = stars[i][1]
        compressed_y += 1
    stars[i][1] = compressed_y

# V자 모양에서 오른쪽 감소하는 별 쌍의 개수 저장
descending = [0] * n
stars.sort(key = lambda x: -x[0])
# 펜윅 트리로 감소하는 쌍의 수 확인
fenwick = FenwickTree(n)
for i in range(n):
    y = stars[i][1]
    a = fenwick.query(0, compressed_y - y + 1)
    descending[i] = a
    fenwick.update(compressed_y - y, 1)

# 펜윅 트리로 증가하는 쌍의 수 확인
fenwick = FenwickTree(n)
answer = 0
for i in range(n):
    y = stars[i][1]
    answer += descending[i] * fenwick.query(0, y + 1)
    fenwick.update(y, 1)

print(answer)