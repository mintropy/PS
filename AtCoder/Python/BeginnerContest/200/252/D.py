'''
pypy RuntimeError
python AC
'''

from math import comb
import sys
input = sys.stdin.readline


N = int(input())
seq = list(map(int, input().split()))

nums = {}
for idx, num in enumerate(seq):
    if num in nums:
        nums[num].append(idx)
    else:
        nums[num] = [idx]

max_count = comb(N, 3)
for idxs in nums.values():
    count = len(idxs)
    if count == 1:
        continue
    max_count -= comb(count, 3) + comb(count, 2) * (N - 2 - (count - 2))
print(max_count)
