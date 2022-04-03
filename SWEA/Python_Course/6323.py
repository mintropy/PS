'''
Title : 함수의 기초 4
'''

def fibonachi(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

n = int(input())
print(fibonachi(n))