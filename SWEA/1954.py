'''
Title : 달팽이 숫자
'''

test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    num = [[0 for _ in range(n)] for _ in range(n)]
    # 지금 입력하고자 하는 칸
    x, y = 0, 0
    # 움직이는 방향, 1, 2, 3, 4, 순서대로 오른쪽, 아래, 왼쪽, 위
    direction = 1

    count = [n] + [] + [1]
    for i in range(1, n ** 2 + 1):
        num[x][y] = i
        if x == n - 1 or y == n - 1:
            
            if direction == 4:
                direction = 1
            else:
                direction += 1