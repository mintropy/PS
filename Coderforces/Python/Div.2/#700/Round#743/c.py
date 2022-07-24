import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    required_chapter = [[] for _ in range(n + 1)]
    required_reverse = [[] for _ in range(n + 1)]
    for i in range(n):
        k, *rq = map(int, input().split())
        required_chapter[i] = set(rq)
        for ch in rq:
            required_reverse[ch].append(i)
    
    if all(required_chapter):
        print(-1)
        continue
    