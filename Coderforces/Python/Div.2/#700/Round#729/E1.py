import sys, itertools

input = sys.stdin.readline

def find_inversion(seq):
    global n
    c = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if seq[i] > seq[j]:
                c += 1
    return c

n, mod = map(int, input().split())

num = [i for i in range(1, n + 1)]
per = list(itertools.permutations(num, n))

count = 0
for seq1 in per:
    for seq2 in per:
        if seq1 >= seq2:
            continue
        if find_inversion(seq1) > find_inversion(seq2):
            count += 1
print(count % mod)