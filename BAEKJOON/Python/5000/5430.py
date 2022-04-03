from sys import stdin
from collections import deque

t = int(stdin.readline().strip())


def arr_to_list(n, array):
    l = []
    tmp = array.split(',')
    if n == 0:
        l = []
    elif n == 1:
        l.append(array[1:-1])
    else:
        for i in range(n):
            if i == 0:
                l.append(int(tmp[i][1:]))
            elif i == n - 1:
                l.append(int(tmp[i][:-1]))
            else:
                l.append(int(tmp[i]))
    return l

def solution(l, command):
    queue = deque(l)
    start = 'F'
    for i in range(len(command)):
        if command[i] == 'R':
            if start == 'F':
                start = 'B'
            else:
                start = 'F'
        elif command[i] == 'D':
            # 실행불가하면 error출력, 종료
            if len(queue) == 0:
                print('error')
                return
            if start == 'F':
                queue.popleft()
            else:
                queue.pop()
    # 모두 실행 했으면 배열 출력
    if len(queue) == 0:
        print('[]')
    elif start == 'F':
        print('[', end = '')
        for i in range(len(queue)):
            print(queue[i], end = '')
            if i != len(queue) - 1:
                print(',', end = '')
            else:
                print(']')
    else:
        print('[', end = '')
        for i in range(len(queue)):
            print(queue[-1 - i], end = '')
            if i != len(queue) - 1:
                print(',', end = '')
            else:
                print(']')


for _ in range(t):
    p = str(stdin.readline().strip())
    n = int(stdin.readline().strip())
    array = str(stdin.readline().strip())
    l = arr_to_list(n, array)
    solution(l, p)