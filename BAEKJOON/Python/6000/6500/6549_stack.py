import sys

input = sys.stdin.readline

def solution(n: int, array: list) -> int:
    answer = 0
    stack = []
    for i in range(n + 1):
        # 마지막 까지 다 꺼내면 -1로, 아니면 해당 높이로 설정
        if i != n:
            cur = array[i]
        else:
            cur = -1
        # 스택이 비어 있지 않고, 다음 막대 높이가 더 작을 때 실행
        while stack and array[stack[-1]] > cur:
            height = array[stack.pop()]
            # 스택이 비어있을 때
            if not stack:
                width = i
            # 스택이 비어있지 않을 때
            else:
                width = i - stack[-1] - 1
            # 영역의 최대 넓이
            area = width * height
            if answer < area:
                answer = area
        # 다음 막대 추가
        stack.append(i)
    return answer

while True:
    n, *array = map(int, input().split())
    if n == 0:
        break
    print(solution(n, array))