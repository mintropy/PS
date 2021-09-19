"""
Title : 싸지방에 간 준하
Link : https://www.acmicpc.net/problem/12764
"""

import sys, heapq
input = sys.stdin.readline

n = int(input())
schedual = [tuple(map(int, input().split())) for _ in range(n)]
# 시작시간 오름차순 정렬
schedual.sort(key=lambda x:x[0])

# 사용자를 앞에서부터 채웠을 때
heap = []
# 비어있는 pc
empty_pc = []
# idx번째 사용자가 몇번 컴퓨터를 사용하는지
# 기본은 0번 컴퓨터 사용
pc_num = [0] * n
for idx, (st, end) in enumerate(schedual):
    # 사용중인 컴퓨터가 없을 때
    if not heap:
        heapq.heappush(heap, (end, 0))
    # 사용중인 컴퓨터가 있을 때
    else:
        # 다음 사용자 입장시간 st와 heap[0] 비교
        # heap[0]가 더 작거나 같을 때 pop
        while heap and heap[0][0] <= st:
            _, i = heapq.heappop(heap)
            heapq.heappush(empty_pc, i)
        if empty_pc:
            pc_now = heapq.heappop(empty_pc)
            pc_num[idx] = pc_now
            heapq.heappush(heap, (end, pc_now))
        else:
            pc_num[idx] = len(heap)
            heapq.heappush(heap, (end, len(heap)))

max_pc = max(pc_num)
print(max_pc + 1)
for i in range(max_pc + 1):
    print(pc_num.count(i), end=' ')
