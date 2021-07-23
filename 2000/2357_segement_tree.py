import sys, math

input = sys.stdin.readline
inf = 1e10

class SegTree:
    def __init__(self, n, seq):
        self.min_tree = [inf] * (2 * n)
        self.min_tree[n:] = seq[1:]
        self.max_tree = [0] * (2 * n)
        self.max_tree[n:] = seq[1:]
        for i in range(n - 1, 0, -1):
            self.max_tree[i] = max(self.max_tree[i * 2], self.max_tree[i * 2 + 1])
            self.min_tree[i] = min(self.min_tree[i * 2], self.min_tree[i * 2 + 1])

    def find_min(self, st, end):
        r = inf
        while st <= end:
            if st % 2 == 1:
                r = min(r, self.min_tree[st])
                st += 1
            if end % 2 == 0:
                r = min(r, self.min_tree[end])
                end -= 1
            st //= 2
            end //= 2
        return r

    def find_max(self, st, end):
        r = 0
        while st <= end:
            if st % 2 == 1:
                r = max(r, self.max_tree[st])
                st += 1
            if end % 2 == 0:
                r = max(r, self.max_tree[end])
                end -= 1
            st //= 2
            end //= 2
        return r


n, m = map(int, input().split())
seq = [0]
for _ in range(n):
    seq.append(int(input()))
    
tree = SegTree(n, seq)
for _ in range(m):
    a, b = map(int, input().split())
    minimum = tree.find_min(a + n - 1, b + n - 1)
    maximum = tree.find_max(a + n - 1, b + n - 1)
    print(minimum, maximum)

