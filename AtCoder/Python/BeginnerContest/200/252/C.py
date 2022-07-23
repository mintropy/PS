import sys
input = sys.stdin.readline


N = int(input())
slot_machine = list(list(input().strip()) for _ in range(N))

reels = [[] for _ in range(10)]
for reel in slot_machine:
    for idx, num in enumerate(reel):
        num = int(num)
        reels[num].append(idx)

ans = 10000
for reel in reels:
    num, count = -1, -1
    for i in range(10):
        _count = reel.count(i)
        if count < _count:
            num = i
            count = _count
        elif count == _count and num < i:
            num = i
    time = 10 * (count - 1) + num
    if ans > time:
        ans = time

print(ans)
