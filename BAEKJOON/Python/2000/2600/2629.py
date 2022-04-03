"""
Title :  양팔저울
Link : https://www.acmicpc.net/problem/2629
"""

n = int(input())
weights = (list(map(int, input().split())))
weights_count = {}
for w in weights:
    if w in weights_count:
        weights_count[w] += 1
    else:
        weights_count[w] = 1

l = sum(weights)
dp = [False] * (l + 1)
for w in sorted(weights_count.keys()):
    # w 무게만으로 가능한 경우
    w_count = weights_count[w]
    if w_count == 1:
        dp[w] = True
    else:
        for i in range(w_count + 1):
            dp[w * i] = True
    # 기존 무게 활용
    for i in range(l):
        if dp[i] and i % w:
            for j in range(1, w_count + 1):
                if i - w * j > 0:
                    dp[i - w * j] = True
                if i + w * j <= l:
                    dp[i + w * j] = True

m = int(input())
check = list(map(int ,input().split()))

for c in check:
    print(dp[c], end = ' ')
