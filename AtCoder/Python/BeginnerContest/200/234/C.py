import sys
input = sys.stdin.readline


K = int(input())

dp = [0, 1]
while True:
    if K <= dp[-1]:
        break
    dp.append(dp[-1] * 2)
if K < dp[-1]:
    dp.pop()

num = ''
length = len(dp) - 1

while K and dp:
    length -= 1
    if K >= dp[-1]:
        num += '2'
        K -= 2 ** length
    else:
        num += '0'
    dp.pop()

num += '0' * length
print(num)
