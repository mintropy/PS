'''
Title : 구구단 1
'''

def gugudan(n):
    for i in range(1, 10):
        if n % i != 0:
            continue
        if 1 <= n // i <= 9:
            return True
    return False

test_case = int(input())
for tc in range(1, test_case + 1):
    if gugudan(int(input())):
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')