import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, K = MIIS()
seq = list(MIIS())

K_seq = seq[:K]
heapq.heapify(K_seq)

ans = [K_seq[0]]
for i in range(K, N):
    n = seq[i]
    if n >= K_seq[0]:
        heapq.heappushpop(K_seq, n)
    ans.append(K_seq[0])

print(*ans, sep='\n')
