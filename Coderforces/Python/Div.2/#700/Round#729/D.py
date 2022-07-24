import sys, heapq, itertools

input = sys.stdin.readline

n = int(input())
seq = [list(map(str, input().split())) for _ in range(n)]

def solution(seq: list) -> int:
    t = []
    for i in range(len(seq)):
        if seq[i][0] == '+':
            heapq.heappush(t, int(seq[i][1]))
        elif seq[i][0] == '-':
            if len(t) == 0:
                continue
            heapq.heappop(t)
    return sum(t) % 998244353

ans = 0
for i in range(1, n + 1):
    comb = list(itertools.combinations(seq, i))
    for sub_seq in comb:
        ans += solution(sub_seq)
print(ans % 998244353)

