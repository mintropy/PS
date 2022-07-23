import sys, itertools
input = sys.stdin.readline


s, k = input().strip().split()
k = int(k)

per = sorted(set(itertools.permutations(s, len(s))))
print(''.join(per[k - 1]))
