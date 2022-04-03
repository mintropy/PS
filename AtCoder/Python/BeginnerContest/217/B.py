import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
s3 = input().strip()
atcoder = {'ABC', 'ARC', 'AGC', 'AHC'}
atcoder -= {s1}
atcoder -= {s2}
atcoder -= {s3}

print(atcoder.pop())
