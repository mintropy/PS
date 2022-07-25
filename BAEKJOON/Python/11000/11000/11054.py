from sys import stdin

n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))


def incresing(n, seq):
    dp = [1 for _ in range(n)]
    # i번째 인덱스 요소가 최대가 되는 증가부분수열
    for i in range(n):
        for j in range(i):
            if seq[j] < seq[i] and dp[j] >= dp[i]:
                dp[i] = dp[j] + 1
    return dp

def decresing(n, seq):
    dp = [1 for _ in range(n)]
    # i번째 인덱스 요소가 최소가 되는 감소부분수열
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if seq[j] < seq[i] and dp[j] >= dp[i]:
                dp[i] = dp[j] + 1
    return dp



inc = incresing(n, seq)
dec = decresing(n, seq)

max_len = 1
for i in range(n):
    # i번재 요소 기준으로 바이토닉 부분수열의 최대 길이
    bitonic = inc[i] + dec[i] - 1
    max_len = max(max_len, bitonic)
print(max_len)