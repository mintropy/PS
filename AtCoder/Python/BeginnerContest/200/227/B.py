import sys
input = sys.stdin.readline


N = int(input())
guess = list(map(int, input().split()))

possible_ans = set()
for a in range(1, 1000):
    for b in range(1, 1000):
        if 4 * a * b + 3 * a + 3 * b > 1000:
            break
        else:
            possible_ans.add(4 * a * b + 3 * a + 3 * b)

ans = 0
for sq in guess:
    if sq not in possible_ans:
        ans += 1

print(ans)
