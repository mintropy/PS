import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cmd = []
for _ in range(n):
    x, y = map(int, input().split())
    if x > y:
        cmd.append((y, x))
cmd.sort()

pos = cmd[0][1]
reverse = cmd[0][1] - cmd[0][0]
for st, end in cmd[1:]:
    # 겹치는 구간이 있을 때
    if pos >= st:
        if end > pos:
            reverse += end - pos
            pos = end
    # 겹치는 구간이 없을 때
    else:
        reverse += end - st
        pos = end

print(m + reverse * 2)
