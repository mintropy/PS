import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, K, X = map(int, input().split())
    prices = list(map(int, input().split()))
    
    max_discount = sum([price // X for price in prices])
    if K <= max_discount:
        print(sum(prices) - K * X)
    else:
        lefts = sorted([price % X for price in prices], reverse=True)
        ans = sum(prices) - max_discount * X
        for i in range(K - max_discount):
            if i == N:
                break
            ans -= lefts[i]
        print(ans)