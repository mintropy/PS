"""
Title : K 물류창고
Link : https://www.acmicpc.net/problem/23350
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()

priority = [0 for _ in range(M + 1)]
works = deque()
for _ in range(N):
    P, W = MIIS()
    works.append((P, W))
    priority[P] += 1

# 먼저 쌓을 우선순위 확인
min_priority = M
for i in range(M, 0, -1):
    if priority[i]:
        min_priority = i
        break

robot_work = 0
container_in_priority = []
while works:
    p, w = works.popleft()
    # 지금 작업이 우선순위가 높다면 가장 뒤로 보내기
    if p < min_priority:
        robot_work += w
        works.append((p, w))
        continue
    # 같은 우선순위라면 무게순서로 쌓기
    if p == min_priority:
        priority[p] -= 1
        # 무게 순서로 쌓기
        tmp = []
        while True:
            if not container_in_priority or w < container_in_priority[-1]:
                robot_work += w
                container_in_priority.append(w)
                break
            else:
                robot_work += container_in_priority[-1]
                tmp.append(container_in_priority.pop())
        while tmp:
            container_in_priority.append(tmp.pop())
            robot_work += container_in_priority[-1]             
        # 해당 우선순위 모두 쌓았다면
        if priority[p] == 0:
            for i in range(p - 1, 0, -1):
                if priority[i]:
                    min_priority = i
                    container_in_priority = []
                    break

print(robot_work)
