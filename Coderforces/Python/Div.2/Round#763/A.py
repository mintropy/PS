import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, m, rb, cb, rd, cd = map(int, input().split())
    if rd >= rb and cd >= cb:
        print(min(rd - rb, cd - cb))
    elif rd >= rb:
        print(min(rd - rb, (m - cb) * 2 + cb - cd))
    elif cd >= cb:
        print(min(cd - cb, (n - rb) * 2 + rb - rd))
    else:
        print(min((n - rb) * 2 + rb - rd, (m - cb) * 2 + cb - cd))
