"""
Title : 피보나치 수 3
Link : https://www.acmicpc.net/problem/2749
"""

def mat_mul(m1: list, m2: list) -> list:
    m3 = []
    a, b, c, d = sum(m1, start= [])
    e, f, g, h = sum(m2, start= [])
    m3.append([(a * e + b * g) % (10 ** 6), (a * f + b * h) % (10 ** 6)])
    m3.append([(c * e + d * g) % (10 ** 6), (c * f + d * h) % (10 ** 6)])
    return m3


n = int(input())

fib = [[0, 1], [0, 0]]
cmd = [[0, 1], [1, 1]]

if n == 0 or n == 1:
    print(n)
else:
    matrix = {1: cmd}
    fib_idx = 1
    while True:
        if fib_idx * 2 > n:
            break
        cmd = mat_mul(cmd, cmd)
        fib_idx *= 2
        matrix[fib_idx] = cmd
    
    power = sorted(matrix.keys(), reverse= True)
    
    for p in power:
        if fib_idx + p < n:
            fib_idx += p
            cmd = mat_mul(cmd, matrix[p])
            continue
        elif fib_idx + p == n:
            fib_idx += p
            cmd = mat_mul(cmd, matrix[p])
            break
        else:
            continue
    
    fib = mat_mul(fib, cmd)
    print(fib[0][0])